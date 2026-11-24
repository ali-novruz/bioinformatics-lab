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
        ("NM_000518.5(HBB):c.93-21G>A", ("no_protein_term", None, "")),
        ("NM_000518.5(HBB):c.55del (p.Lys18_Val19insTer)", ("nonsense", 18, "K18*")),
        ("NM_000518.5(HBB):c.x (p.Glu121delinsLeuTer)", ("nonsense", 121, "E121*")),
        ("NM_000518.5(HBB):c.x (p.Ter148ThrextTer?)", ("stop_loss", 148, "*148ext")),
        ("NM_000518.5(HBB):c.x (p.His3_Leu4=)", ("synonymous", 3, "H3=")),
        ("NM_000518.5(HBB):c.x (p.125EGN[3])", ("inframe", 125, "125EGN[3]")),
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
    with pytest.raises(ValueError):
        classification_group("risk factor")


def test_unrecognised_protein_term_raises():
    with pytest.raises(ValueError):
        protein_consequence("NM_000518.5(HBB):c.x (p.Xyz12Abc)")


def test_stored_showcase_summary():
    summary = json.loads((STORED / "summary.json").read_text(encoding="utf-8"))
    assert summary["records_total"] == 3458
    assert summary["in_scope"] == {"HBB": 1822, "MEFV": 1409}
    assert summary["composition"]["MEFV"]["P/LP"] == 25
    assert summary["composition"]["HBB"]["P/LP"] == 408
    hot = summary["hotspot_mefv"]
    assert hot["unit"] == "distinct protein change"
    assert (hot["plp_records_in_domain"], hot["plp_records"]) == (9, 13)
    assert (hot["plp_in_domain"], hot["plp_missense"]) == (6, 10)
    assert (hot["all_in_domain"], hot["all_classified_missense"]) == (105, 439)
    assert hot["p_label_permutation"] < 0.05
    assert [v["change"] for v in summary["frequency_tension"]["plp_above"]] == ["E7V"]
    assert (
        summary["clinical_use"] is False
        and summary["regional_prevalence_claim"] is False
    )


def test_live_explorer_bundle_matches_stored_results():
    text = (ROOT / "projects/advanced/regional-variant-interpretation/live/data.js").read_text(encoding="utf-8")
    bundle = json.loads(text.removeprefix("window.CVDEMO=").rstrip().rstrip(";"))
    stored = json.loads((STORED / "summary.json").read_text(encoding="utf-8"))
    assert bundle["summary"] == stored
    group = bundle["columns"].index("group")
    gene = bundle["columns"].index("gene")
    for name, counts in stored["composition"].items():
        rows = [r for r in bundle["rows"] if r[gene] == name]
        assert {g: sum(r[group] == g for r in rows) for g in counts} == counts
