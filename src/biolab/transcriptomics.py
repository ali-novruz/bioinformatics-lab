"""Bulk count analysis with an explicit sequencing-type covariate."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


def validate_counts(
    counts: pd.DataFrame, metadata: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if (
        counts.index.has_duplicates
        or counts.columns.has_duplicates
        or metadata.index.has_duplicates
    ):
        raise ValueError("Duplicate sample/gene identifiers")
    if set(counts.index) != set(metadata.index):
        raise ValueError("Counts and metadata sample IDs differ")
    x = counts.to_numpy(dtype=float)
    if not np.isfinite(x).all() or (x < 0).any() or not np.equal(x, np.floor(x)).all():
        raise ValueError("Raw nonnegative integer counts required")
    if (x.sum(axis=1) == 0).any():
        raise ValueError("Zero-library sample")
    if "condition" not in metadata or metadata["condition"].isna().any():
        raise ValueError("condition metadata required")
    return counts.astype(int), metadata.loc[counts.index].copy()


def load_pasilla(folder: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    counts = pd.read_csv(folder / "pasilla_gene_counts.tsv", sep="\t", index_col=0).T
    metadata = pd.read_csv(folder / "pasilla_sample_annotation.csv", index_col=0)
    metadata.index = metadata.index.str.replace(r"fb$", "", regex=True)
    if "type" not in metadata:
        raise ValueError("Sequencing type covariate missing")
    return validate_counts(counts, metadata)


def differential_expression(
    counts: pd.DataFrame, metadata: pd.DataFrame, design: str = "~ type + condition"
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    from pydeseq2.dds import DeseqDataSet
    from pydeseq2.ds import DeseqStats

    counts, metadata = validate_counts(counts, metadata)
    if set(metadata["condition"]) != {"treated", "untreated"}:
        raise ValueError("Expected treated/untreated conditions")
    if metadata.groupby("condition").size().min() < 2:
        raise ValueError("At least 2 biological samples per group required")
    keep = counts.sum(axis=0) >= 10
    counts = counts.loc[:, keep]
    dds = DeseqDataSet(
        counts=counts,
        metadata=metadata,
        design=design,
        refit_cooks=True,
        n_cpus=1,
        quiet=True,
    )
    dds.deseq2()
    stat = DeseqStats(
        dds,
        contrast=["condition", "treated", "untreated"],
        alpha=0.05,
        n_cpus=1,
        quiet=True,
    )
    stat.summary()
    results = stat.results_df.copy().sort_values("padj")
    normalized = pd.DataFrame(
        dds.layers["normed_counts"], index=counts.index, columns=counts.columns
    )
    summary = {
        "input_genes": int(len(keep)),
        "tested_genes": int(keep.sum()),
        "samples": len(counts),
        "design": design,
        "contrast": "treated / untreated",
        "prefilter": "total count >= 10 across all samples",
        "significant_fdr_005": int((results.padj < 0.05).sum()),
        "significant_fdr_005_abs_lfc_gt1": int(
            ((results.padj < 0.05) & (results.log2FoldChange.abs() > 1)).sum()
        ),
        "missing_padj": int(results.padj.isna().sum()),
        "lfc_shrinkage": "not applied; unshrunken coefficients",
        "implementation": "PyDESeq2 0.5.4, not a byte-identical reproduction of R DESeq2",
    }
    return results, normalized, summary
