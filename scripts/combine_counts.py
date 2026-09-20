"""Combine featureCounts single-sample outputs; never align genes by row number."""

import argparse
from pathlib import Path

from biolab.counts import combine_feature_counts

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument(
        "--samples", required=True, help="TSV with sample_id and counts_path"
    )
    p.add_argument("--output", required=True)
    a = p.parse_args()
    counts = combine_feature_counts(a.samples)
    output = Path(a.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    counts.to_csv(output, sep="\t", index_label="gene_id")
