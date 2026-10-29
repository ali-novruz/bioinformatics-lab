"""Showcase analyses for the Khan classifier: named classes, geometry, leakage.

Adds four views on top of run_expression_ml.py without changing its protocol:
PCA of all vs selected probes (fit on training only), a heatmap of the selected
probes, test-set decision scores, and a leakage experiment that contrasts
selection outside vs inside cross-validation on shuffled labels.
Requires datasets/annotations from scripts/build_khan_annotation.py.
"""

import json
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fetch_khan import fetch
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

from biolab.expression_ml import expression_pipeline, fit_training_only, load_khan
from biolab.reporting import finish_run, new_run, write_json

ROOT = Path(__file__).resolve().parents[1]
ANNOTATION = ROOT / "datasets/annotations"
COLORS = {"BL": "#d9822b", "EWS": "#2f6db5", "NB": "#3a9a5b", "RMS": "#b8344f"}
SHUFFLES = 100


def short_name(description: str) -> str:
    return description.split(",")[0].split("(")[0].strip()[:42]


def leakage_experiment(xtrain, ytrain, k, c, seed=42):
    """Balanced accuracy on shuffled labels: selection before vs inside CV."""
    rng = np.random.default_rng(seed)
    cv = StratifiedKFold(5, shuffle=True, random_state=seed)
    rows = []
    for i in range(SHUFFLES + 1):
        y = ytrain.to_numpy() if i == 0 else rng.permutation(ytrain.to_numpy())
        leaky_x = SelectKBest(f_classif, k=k).fit_transform(xtrain, y)
        leaky = make_pipeline(
            StandardScaler(),
            LinearSVC(C=c, class_weight="balanced", dual="auto", max_iter=20000),
        )
        rows.append(
            {
                "shuffle": i,
                "labels": "real" if i == 0 else "shuffled",
                "leaky_selection": cross_val_score(
                    leaky, leaky_x, y, cv=cv, scoring="balanced_accuracy"
                ).mean(),
                "selection_inside_cv": cross_val_score(
                    expression_pipeline(k=k, c=c, seed=seed),
                    xtrain,
                    y,
                    cv=cv,
                    scoring="balanced_accuracy",
                ).mean(),
            }
        )
    return pd.DataFrame(rows)


def main():
    started = time.perf_counter()
    folder = fetch()
    xtrain, xtest, ytrain, ytest = load_khan(folder)
    annotation = pd.read_csv(ANNOTATION / "khan_probe_annotation.csv")
    verification = json.loads(
        (ANNOTATION / "khan_annotation_verification.json").read_text()
    )
    names = {int(k): v for k, v in verification["class_map"].items()}
    if list(annotation["probe_column"]) != list(xtrain.columns):
        raise ValueError("Annotation does not follow the probe column order")
    out = new_run(
        ROOT,
        "khan-showcase",
        [*sorted(folder.glob("*.csv")), *sorted(ANNOTATION.glob("khan_*"))],
        {"seed": 42, "shuffles": SHUFFLES, "pca": "fit on training only"},
    )
    search = fit_training_only(xtrain, ytrain)
    model = search.best_estimator_
    k = search.best_params_["select__k"]
    c = search.best_params_["classifier__C"]
    kept = model.named_steps["variance"].get_support(indices=True)
    chosen = kept[model.named_steps["select"].get_support(indices=True)]
    scores = model.named_steps["select"].scores_[
        model.named_steps["select"].get_support(indices=True)
    ]
    genes = annotation.iloc[chosen].assign(anova_f=scores)
    ytr_name = ytrain.map(names)
    yte_name = ytest.map(names)
    class_means = xtrain.iloc[:, chosen].groupby(ytr_name.to_numpy()).mean()
    genes["highest_class"] = class_means.idxmax().to_numpy()
    genes["short_name"] = genes["description"].map(short_name)
    genes = genes.sort_values(["highest_class", "anova_f"], ascending=[True, False])
    genes.to_csv(out / "selected_genes.csv", index=False, lineterminator="\n")

    # PCA geometry: all probes vs selected probes, both fit on training only.
    pca_views = {}
    for label, columns in [("all", slice(None)), ("selected", genes.index)]:
        scaler = StandardScaler().fit(xtrain.iloc[:, columns])
        pca = PCA(2, random_state=42).fit(scaler.transform(xtrain.iloc[:, columns]))
        pca_views[label] = {
            "explained": pca.explained_variance_ratio_.round(4).tolist(),
            "train": pca.transform(scaler.transform(xtrain.iloc[:, columns])).round(3),
            "test": pca.transform(scaler.transform(xtest.iloc[:, columns])).round(3),
        }

    prediction = pd.Series(model.predict(xtest)).map(names)
    decision = pd.DataFrame(
        model.decision_function(xtest),
        columns=[names[i] for i in model.classes_],
    ).round(4)
    decision.insert(0, "prediction", prediction)
    decision.insert(0, "truth", yte_name.to_numpy())
    decision.insert(0, "sample_id", [f"test_{i:02d}" for i in range(1, 21)])
    decision.to_csv(out / "test_decision_scores.csv", index=False, lineterminator="\n")

    leakage = leakage_experiment(xtrain, ytrain, k, c)
    leakage.to_csv(out / "leakage_experiment.csv", index=False, lineterminator="\n")
    shuffled = leakage[leakage["labels"] == "shuffled"]

    # Figures for the repository.
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax, (label, view) in zip(axes, pca_views.items(), strict=True):
        for name, color in COLORS.items():
            mask = ytr_name.to_numpy() == name
            ax.scatter(*view["train"][mask].T, c=color, label=name, s=28)
            mask = yte_name.to_numpy() == name
            ax.scatter(*view["test"][mask].T, facecolor="white", edgecolor=color, s=46)
        ax.set_title(f"PCA, {'2308' if label == 'all' else len(chosen)} probes")
        ax.set_xlabel(f"PC1 ({view['explained'][0]:.0%})")
        ax.set_ylabel(f"PC2 ({view['explained'][1]:.0%})")
    axes[0].legend(frameon=False)
    fig.tight_layout()
    fig.savefig(out / "pca.png", dpi=160)
    plt.close(fig)

    order = np.argsort(ytr_name.to_numpy(), kind="stable")
    block = xtrain.iloc[order, genes.index]
    z = ((block - block.mean()) / block.std()).T
    fig, ax = plt.subplots(figsize=(11, 6.2))
    ax.imshow(z, aspect="auto", cmap="RdBu_r", vmin=-2.5, vmax=2.5)
    ax.set_yticks(range(len(genes)), genes["short_name"], fontsize=7)
    edges = np.flatnonzero(np.diff(pd.factorize(ytr_name.iloc[order])[0])) + 0.5
    for edge in edges:
        ax.axvline(edge, color="black", lw=1)
    ax.set_xticks([])
    ax.set_title("Selected probes, z-scored per probe; training samples by class")
    fig.tight_layout()
    fig.savefig(out / "heatmap.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4.2))
    bins = np.linspace(0, 1, 41)
    ax.hist(
        shuffled["leaky_selection"],
        bins,
        color="#b8344f",
        alpha=0.75,
        label="selection before CV",
    )
    ax.hist(
        shuffled["selection_inside_cv"],
        bins,
        color="#2f6db5",
        alpha=0.75,
        label="selection inside CV",
    )
    ax.axvline(0.25, color="black", ls="--", lw=1)
    ax.set_xlabel("CV balanced accuracy on shuffled labels")
    ax.set_ylabel("shuffles")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(out / "leakage.png", dpi=160)
    plt.close(fig)

    summary = {
        "class_map": verification["class_map"],
        "selected_parameters": search.best_params_,
        "test_accuracy": float((prediction == yte_name).mean()),
        "misclassified": decision[decision["truth"] != decision["prediction"]][
            ["sample_id", "truth", "prediction"]
        ].to_dict("records"),
        "pca_explained_all": pca_views["all"]["explained"],
        "pca_explained_selected": pca_views["selected"]["explained"],
        "leakage": {
            "shuffles": SHUFFLES,
            "leaky_mean": round(float(shuffled["leaky_selection"].mean()), 4),
            "leaky_min": round(float(shuffled["leaky_selection"].min()), 4),
            "inside_cv_mean": round(float(shuffled["selection_inside_cv"].mean()), 4),
            "inside_cv_max": round(float(shuffled["selection_inside_cv"].max()), 4),
            "real_labels_leaky": round(float(leakage["leaky_selection"].iloc[0]), 4),
            "real_labels_inside_cv": round(
                float(leakage["selection_inside_cv"].iloc[0]), 4
            ),
        },
        "selected_gene_classes": genes["highest_class"].value_counts().to_dict(),
    }
    write_json(out / "summary.json", summary)

    # Compact data bundle consumed by the HTML presentations.
    write_json(
        out / "presentation_data.json",
        {
            "classes": ["BL", "EWS", "NB", "RMS"],
            "train_counts": ytr_name.value_counts().sort_index().to_dict(),
            "test_counts": yte_name.value_counts().sort_index().to_dict(),
            "pca": {
                label: {
                    "explained": view["explained"],
                    "train": [
                        [*p, n]
                        for p, n in zip(view["train"].tolist(), ytr_name, strict=True)
                    ],
                    "test": [
                        [*p, t, q]
                        for p, t, q in zip(
                            view["test"].tolist(), yte_name, prediction, strict=True
                        )
                    ],
                }
                for label, view in pca_views.items()
            },
            "genes": [
                {
                    "probe": r.probe_column,
                    "image_id": None if pd.isna(r.image_id) else int(r.image_id),
                    "name": r.short_name,
                    "description": r.description,
                    "f": round(float(r.anova_f), 2),
                    "high": r.highest_class,
                    "means": class_means[r.probe_column].round(3).to_dict(),
                }
                for r in genes.itertuples()
            ],
            "heatmap": {
                "samples": ytr_name.iloc[order].tolist(),
                "z": z.round(2).to_numpy().tolist(),
            },
            "decision": decision.to_dict("records"),
            "confusion": pd.crosstab(yte_name, prediction)
            .reindex(index=list(COLORS), columns=list(COLORS), fill_value=0)
            .to_numpy()
            .tolist(),
            "cv_grid": pd.DataFrame(search.cv_results_)[
                ["param_select__k", "param_classifier__C", "mean_test_score"]
            ]
            .rename(columns=lambda s: s.split("__")[-1])
            .astype(float)
            .round(4)
            .to_dict("records"),
            "leakage": {
                "leaky": shuffled["leaky_selection"].round(4).tolist(),
                "inside": shuffled["selection_inside_cv"].round(4).tolist(),
            },
            "summary": summary,
        },
    )
    finish_run(
        out, status="passed", elapsed_seconds=round(time.perf_counter() - started, 2)
    )
    print(json.dumps(summary, indent=2))
    print(out)


if __name__ == "__main__":
    main()
