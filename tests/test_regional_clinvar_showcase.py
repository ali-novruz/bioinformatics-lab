import json
from pathlib import Path

import pytest

from biolab.clinvar import (
    assigned_gene,
    classification_group,
    protein_consequence,
    review_stars,
)

ROOT = Path(__file__).resolve().parents[1]
STORED = ROOT / "results/showcase/regional-clinvar"


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        ("NM_000243.3(MEFV):c.2080A>G (p.Met694Val)", ("missense", 694, "M694V")),
        (
            "NM_000243.3(MEFV):c.2080_2082delinsGTA (p.Met694Val)",
            ("missense", 694, "M694V"),
        ),
        ("NM_000518.5(HBB):c.118C>T (p.Gln40Ter)", ("nonsense", 40, "Q40*")),
        ("NM_000518.5(HBB):c.17_18del (p.Pro6fs)", ("frameshift", 6, "P6fs")),
        ("NM_000243.3(MEFV):c.6C>T (p.Ala2=)", ("synonymous", 2, "A2=")),
        ("NM_000243.3(MEFV):c.2076_2078del (p.Ile692del)", ("inframe", 692, "I692del")),
        ("NM_000518.5(HBB):c.93-21G>A", ("noncoding", None, "")),
    ],
)
def test_protein_consequence(title, expected):
    assert protein_consequence(title) == expected


def test_gene_assignment_ignores_loc_elements():
    assert assigned_gene("HBB;LOC106099062;LOC107133510") == "HBB"
    assert assigned_gene("LOC126862264;MEFV") == "MEFV"
    assert assigned_gene("MEFV;MEFV") == "MEFV"
    assert assigned_gene("CLUAP1;MEFV") is None


def test_unknown_review_status_raises():
    assert review_stars("reviewed by expert panel") == 3
    with pytest.raises(ValueError):
        review_stars("")


def test_classification_groups():
    assert classification_group("Pathogenic; other") == "P/LP"
    assert (
        classification_group("Conflicting classifications of pathogenicity")
        == "Conflicting"
    )
    assert classification_group("not provided") == "Other"


def test_stored_showcase_summary():
    summary = json.loads((STORED / "summary.json").read_text(encoding="utf-8"))
    assert summary["records_total"] == 3458
    assert summary["in_scope"] == {"HBB": 1822, "MEFV": 1409}
    assert summary["composition"]["MEFV"]["P/LP"] == 25
    assert summary["composition"]["HBB"]["P/LP"] == 408
    hot = summary["hotspot_mefv"]
    assert (hot["plp_in_domain"], hot["plp_missense"]) == (9, 13)
    assert hot["p_label_permutation"] < 0.01
    assert [v["change"] for v in summary["frequency_tension"]["plp_above"]] == ["E7V"]
    assert (
        summary["clinical_use"] is False
        and summary["regional_prevalence_claim"] is False
    )
