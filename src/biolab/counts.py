"""Strict, identifier-aligned ingestion of single-sample featureCounts tables."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ANNOTATION = ["Chr", "Start", "End", "Strand", "Length"]


def combine_feature_counts(samples_path: str | Path) -> pd.DataFrame:
    samples_path = Path(samples_path).resolve()
    samples = pd.read_csv(samples_path, sep="\t", dtype=str, keep_default_na=False)
    if not {"sample_id", "counts_path"} <= set(samples.columns) or samples.empty:
        raise ValueError("A nonempty table with sample_id and counts_path is required")
    for column in ["sample_id", "counts_path"]:
        if samples[column].str.strip().eq("").any():
            raise ValueError(f"Blank {column}")
    if samples.sample_id.duplicated().any():
        raise ValueError("Duplicate sample IDs")
    series, reference = [], None
    for row in samples.itertuples():
        path = Path(str(row.counts_path))
        if not path.is_absolute():
            path = samples_path.parent / path
        table = pd.read_csv(
            path, sep="\t", comment="#", dtype=str, keep_default_na=False
        )
        if len(table.columns) != 7 or list(table.columns[:6]) != [
            "Geneid",
            *ANNOTATION,
        ]:
            raise ValueError(
                "Expected Geneid, Chr, Start, End, Strand, Length and one count column"
            )
        if (
            table.empty
            or table.Geneid.duplicated().any()
            or table.Geneid.str.strip().eq("").any()
        ):
            raise ValueError("Nonempty unique gene IDs required")
        table = table.set_index("Geneid").sort_index()
        annotation = table[ANNOTATION]
        if annotation.apply(lambda s: s.str.strip().eq("")).any().any():
            raise ValueError("Missing feature annotation")
        if reference is not None and not annotation.equals(reference):
            raise ValueError(
                "Gene universes or coordinates/strand/length differ; check annotations"
            )
        reference = annotation
        values = table.iloc[:, -1]
        # Direct integer parsing avoids rounding large counts through float64.
        if not values.str.fullmatch(r"\d+").all():
            raise ValueError(
                "Raw nonnegative integer counts required (fractional counts unsupported)"
            )
        integers = values.map(int)
        if any(value > 2**63 - 1 for value in integers):
            raise ValueError("Counts exceed signed 64-bit range")
        series.append(integers.astype("int64").rename(row.sample_id))
    return pd.concat(series, axis=1).rename_axis("gene_id")
