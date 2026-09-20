from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from biolab.genomics import allele_counts, analyze_vcf, variant_type
from biolab.io import read_fasta, read_vcf
from biolab.statistics import benjamini_hochberg
from biolab.transcriptomics import validate_counts

ROOT = Path(__file__).resolve().parents[1]


def test_vcf_genotypes_filters_and_multiallelic():
    table, summary = analyze_vcf(ROOT / "datasets/fixtures/toy.vcf")
    assert summary["input_records"] == 4
    assert summary["retained_alleles"] == 4
    assert summary["excluded_records"] == {"not_PASS": 1}
    assert table.iloc[0].sample_alt_frequency == 0.75
    multi = table[table.pos == 10]
    assert list(multi.sample_alt_frequency) == [0.5, 0.5]
    assert summary["transitions"] == 2 and summary["transversions"] == 1
    assert variant_type("A", "<DEL>") == "structural_or_symbolic"
    with pytest.raises(ValueError):
        allele_counts({"s": {"GT": "0/3"}}, 1)


def test_empty_vcf_rejected(tmp_path):
    p = tmp_path / "x.vcf"
    p.write_text("toy\t1\t.\tA\tG\t1\tPASS\t.\n")
    with pytest.raises(ValueError):
        list(read_vcf(p))


def test_duplicate_fasta_rejected(tmp_path):
    p = tmp_path / "x.fa"
    p.write_text(">a\nACG\n>a\nTTT\n")
    with pytest.raises(ValueError):
        list(read_fasta(p))


def test_bh_known_values_and_order():
    assert np.allclose(
        benjamini_hochberg([0.01, 0.04, 0.03, 0.002]), [0.02, 0.04, 0.04, 0.008]
    )
    assert len(benjamini_hochberg([])) == 0
    for p in [[-1], [2], [np.nan], [np.inf], [[0.5]]]:
        with pytest.raises(ValueError):
            benjamini_hochberg(p)


def test_counts_alignment_and_validation():
    counts = pd.DataFrame([[1, 2], [3, 4]], index=["a", "b"], columns=["g1", "g2"])
    meta = pd.DataFrame({"condition": ["treated", "untreated"]}, index=["b", "a"])
    _, aligned = validate_counts(counts, meta)
    assert list(aligned.index) == ["a", "b"]
    with pytest.raises(ValueError):
        validate_counts(counts + 0.5, meta)
    with pytest.raises(ValueError):
        validate_counts(counts * 0, meta)
    with pytest.raises(ValueError):
        validate_counts(counts, meta.rename(index={"a": "c"}))
