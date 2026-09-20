from pathlib import Path

import pandas as pd
import pytest

from biolab.clinical import prioritize_clinvar

ROOT = Path(__file__).resolve().parents[1]


def test_curated_clinvar_triage_has_explicit_boundary() -> None:
    table, summary = prioritize_clinvar(
        ROOT / "datasets/examples/regional/clinvar-2026-09-20.tsv"
    )
    assert table.gene.tolist() == ["HBB", "MEFV"]
    assert table.priority_score.tolist() == [9, 7]
    assert not summary["clinical_use"] and not summary["regional_prevalence_claim"]
    assert table.interpretation_boundary.str.contains("Educational").all()


def test_clinvar_triage_rejects_invalid_frequency(tmp_path: Path) -> None:
    source = ROOT / "datasets/examples/regional/clinvar-2026-09-20.tsv"
    table = pd.read_csv(source, sep="\t")
    table.loc[0, "gnomad_frequency"] = 2
    path = tmp_path / "bad.tsv"
    table.to_csv(path, sep="\t", index=False)
    with pytest.raises(ValueError, match="frequency"):
        prioritize_clinvar(path)
