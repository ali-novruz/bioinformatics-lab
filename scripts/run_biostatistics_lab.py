"""Simulate multiple testing and summarize the real yeast libraries for teaching."""

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

from biolab.reporting import new_run, write_json
from biolab.statistics import benjamini_hochberg

ROOT = Path(__file__).resolve().parents[1]


if __name__ == "__main__":
    source = ROOT / "results/raw-examples/rna-model/counts.tsv"
    out = new_run(
        ROOT,
        "biostatistics-lab",
        [source],
        {
            "seed": 20260916,
            "null_genes": 1000,
            "samples_per_group": 20,
            "data_types": "real RNA library summaries + explicitly synthetic null experiment",
        },
    )
    counts = pd.read_csv(source, sep="\t", index_col=0)
    libraries = counts.sum()
    libraries.rename("assigned_fragments").to_csv(out / "library_sizes.csv")
    rng = np.random.default_rng(20260916)
    a = rng.normal(size=(20, 1000))
    b = rng.normal(size=(20, 1000))
    p = ttest_ind(a, b, axis=0, equal_var=False).pvalue
    adjusted = benjamini_hochberg(p)
    pd.DataFrame(
        {"synthetic_gene": np.arange(1000), "p": p, "padj_bh": adjusted}
    ).to_csv(out / "null_tests.csv", index=False)
    summary = {
        "simulation": "All 1000 null hypotheses are true by construction; one seeded realization",
        "uncorrected_p_below_005": int((p < 0.05).sum()),
        "bh_adjusted_p_below_005": int((adjusted < 0.05).sum()),
        "expected_uncorrected_false_positives_if_calibrated": 50,
        "library_mean": float(libraries.mean()),
        "library_median": float(libraries.median()),
        "library_sample_sd": float(libraries.std(ddof=1)),
        "interpretation": "A nonsignificant result does not prove H0. BH controls expected false discovery proportion under its assumptions, not every realized dataset.",
    }
    write_json(out / "summary.json", summary)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].hist(p, bins=20, color="#2c7c88")
    axes[0].set(title="Synthetic all-null p-values", xlabel="p-value", ylabel="Tests")
    axes[1].bar(
        ["p < .05", "BH < .05"],
        [summary["uncorrected_p_below_005"], summary["bh_adjusted_p_below_005"]],
        color=["#ac5a44", "#2c7c88"],
    )
    axes[1].set(
        title="False positives in one seeded simulation", ylabel="Tests selected"
    )
    fig.tight_layout()
    fig.savefig(out / "multiple_testing.png", dpi=150)
    plt.close(fig)
    print(out)
    print(summary)
