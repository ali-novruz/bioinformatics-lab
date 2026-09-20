"""Run bounded sensitivity experiments on the existing GO and Khan analyses."""

import argparse
import itertools
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from biolab.reporting import recorded_run, write_json
from biolab.sensitivity import (
    nested_expression_cv,
    permutation_pvalue,
    singleton_enrichment,
)

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "experiments/controls/protocol.json"


def enrichment(protocol):
    source = ROOT / "results/raw-examples/rna-model/differential_expression.csv"
    annotations = ROOT / "datasets/examples/enrichment/sgd_go_slim_chrI.tsv"
    config = protocol["enrichment"]
    with recorded_run(
        ROOT, "enrichment-control", [source, annotations, PROTOCOL], config
    ) as out:
        de = pd.read_csv(source).set_index("gene_id")
        ann = pd.read_csv(annotations, sep="\t")
        universe = set(de.index[np.isfinite(de.padj)])
        rows = singleton_enrichment(
            universe,
            ann.groupby("go_id").gene_id.agg(set).to_dict(),
            alpha=config["alpha"],
            min_size=config["min_term_size"],
        )
        rows["observed_foreground"] = rows.gene_id.isin(
            de.index[de.padj < config["alpha"]]
        )
        rows.to_csv(out / "singletons.csv", index=False)
        write_json(
            out / "summary.json",
            {
                "universe_genes": len(universe),
                "eligible_terms": int(rows.tested_terms.iloc[0]),
                "observed_foreground_genes": int(rows.observed_foreground.sum()),
                "singletons_with_any_discovery": int((rows.discoveries > 0).sum()),
                "minimum_attainable_padj": float(rows.min_padj.min()),
                "observed_min_padj": rows.loc[
                    rows.observed_foreground, "min_padj"
                ].tolist(),
                "scope": "Exhaustive singleton attainability under a fixed gene universe and GO-slim term family; not power across biological effect sizes",
                "limitations": "Uniform gene selection is not a biological null model; annotation coverage and term dependence remain. No thresholds changed.",
            },
        )
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(rows.min_padj, bins=np.linspace(0, 1, 21), color="#157f83")
        ax.axvline(
            config["alpha"], color="#c23b4a", linestyle="--", label="BH threshold 0.05"
        )
        ax.set(
            xlabel="Smallest BH-adjusted p per singleton foreground",
            ylabel="Number of foreground genes",
            title="GO-slim: enumerate every possible one-gene selection",
        )
        ax.legend()
        fig.tight_layout()
        fig.savefig(out / "attainability.png", dpi=150)
        plt.close(fig)
    print(out, flush=True)


def expression(protocol):
    folder = ROOT / "datasets/raw/khan"
    inputs = [folder / "Khan_xtrain.csv", folder / "Khan_ytrain.csv"]
    if not all(p.exists() for p in inputs):
        raise FileNotFoundError(
            "First run python scripts/fetch_khan.py; control itself never downloads or opens test files"
        )
    # Verify the pinned source bytes even when a local cache already exists.
    import hashlib

    manifest = json.loads(
        (ROOT / "datasets/khan-manifest.json").read_text(encoding="utf-8")
    )
    hashes = {item["path"]: item["sha256"] for item in manifest["files"]}
    for path in inputs:
        if (
            hashlib.sha256(path.read_bytes()).hexdigest()
            != hashes[path.relative_to(ROOT).as_posix()]
        ):
            raise ValueError(f"Khan source checksum mismatch: {path.name}")
    x = pd.read_csv(inputs[0])
    y = pd.read_csv(inputs[1])["x"]
    if x.shape != (63, 2308) or y.value_counts().sort_index().tolist() != [
        8,
        23,
        12,
        20,
    ]:
        raise ValueError("Unexpected pinned Khan training dimensions or labels")
    config = {**protocol["expression"], "seed": protocol["seed"]}
    kwargs = {
        "seed": protocol["seed"],
        "outer_folds": config["outer_folds"],
        "inner_folds": config["inner_folds"],
        "grid": {"select__k": config["k_grid"], "classifier__C": config["C_grid"]},
    }
    with recorded_run(
        ROOT,
        "expression-control",
        [*inputs, ROOT / "datasets/khan-manifest.json", PROTOCOL],
        config,
    ) as out:
        folds, predictions = nested_expression_cv(x, y, **kwargs)
        predictions.to_csv(out / "out_of_fold_predictions.csv", index=False)
        write_json(out / "folds.json", folds)
        observed = float(np.mean([r["balanced_accuracy"] for r in folds]))
        rng = np.random.default_rng(protocol["seed"])
        null = []
        null_folds = []
        for repeat in range(config["permutations"]):
            permuted = rng.permutation(y)
            shuffled, _ = nested_expression_cv(x, permuted, **kwargs)
            score = float(np.mean([r["balanced_accuracy"] for r in shuffled]))
            null.append(score)
            null_folds.append(
                {
                    "permutation": repeat + 1,
                    "labels": permuted.tolist(),
                    "folds": shuffled,
                }
            )
            pd.DataFrame(
                {"permutation": np.arange(1, len(null) + 1), "balanced_accuracy": null}
            ).to_csv(out / "permutations.csv", index=False)
            if (repeat + 1) % 10 == 0:
                print(
                    f"Expression permutations {repeat + 1}/{config['permutations']}",
                    flush=True,
                )
        write_json(out / "permutation_folds.json", null_folds)
        selections = [set(r["selected_feature_indices0"]) for r in folds]
        jaccards = [
            len(a & b) / len(a | b) for a, b in itertools.combinations(selections, 2)
        ]
        write_json(
            out / "summary.json",
            {
                "training_samples": len(y),
                "test_samples_opened": 0,
                "mean_outer_balanced_accuracy": observed,
                "fold_balanced_accuracy": [r["balanced_accuracy"] for r in folds],
                "dummy_balanced_accuracy": 0.25,
                "effect_above_dummy": observed - 0.25,
                "permutations": len(null),
                "permutation_pvalue": permutation_pvalue(observed, null),
                "null_mean": float(np.mean(null)),
                "null_central_95_range": np.quantile(null, [0.025, 0.975]).tolist(),
                "minimum_pvalue_resolution": 1 / (1 + len(null)),
                "mean_pairwise_selected_probe_jaccard": float(np.mean(jaccards)),
                "selected_probe_counts": [len(s) for s in selections],
                "scope": "Training-only nested CV and full-pipeline permutation control; post-hoc robustness audit",
                "limitations": [
                    "Outer folds share training data: fold range is not a confidence interval.",
                    "The null range describes permutation scores, not uncertainty of clinical performance.",
                    "Unknown donor dependence or upstream preprocessing can violate exchangeability; no external cohort.",
                    "Selection overlap is descriptive and is not a gene-level biomarker claim.",
                    "99 permutations give coarse 0.01 p-value resolution; this protocol was written before this audit run but after earlier benchmark results.",
                ],
            },
        )
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(null, bins=15, color="#157f83", label="Refit shuffled-label controls")
        ax.axvline(observed, color="#c23b4a", label="Observed nested CV")
        ax.set(
            xlim=(0, 1.02),
            xlabel="Mean outer-fold balanced accuracy",
            ylabel="Permutation count",
            title="Khan training only: selection repeated inside every fold",
        )
        ax.legend()
        fig.tight_layout()
        fig.savefig(out / "permutation_control.png", dpi=150)
        plt.close(fig)
    print(out, flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--experiment", choices=["enrichment", "expression", "all"], default="all"
    )
    args = parser.parse_args()
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    for name in (
        ["enrichment", "expression"] if args.experiment == "all" else [args.experiment]
    ):
        globals()[name](protocol)
