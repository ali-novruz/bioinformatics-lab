"""Transparent educational prioritization of curated ClinVar records."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

REVIEW_WEIGHT = {
    "practice guideline": 4,
    "reviewed by expert panel": 3,
    "criteria provided, multiple submitters, no conflicts": 2,
    "criteria provided, single submitter": 1,
}


def prioritize_clinvar(path: str | Path) -> tuple[pd.DataFrame, dict[str, object]]:
    """Rank already-curated records without claiming an ACMG classification."""
    table = pd.read_csv(path, sep="\t", dtype=str)
    required = {
        "gene",
        "clinvar_id",
        "accession",
        "rsid",
        "hgvs_c",
        "hgvs_p",
        "clinical_significance",
        "review_status",
        "condition",
        "inheritance",
        "gnomad_frequency",
        "source_url",
        "retrieved",
    }
    if table.empty or not required <= set(table.columns):
        raise ValueError("ClinVar table is empty or lacks required evidence columns")
    if table[["gene", "clinvar_id", "accession", "source_url"]].isna().any().any():
        raise ValueError("Variant identifiers and sources must be complete")
    frequency = pd.to_numeric(table["gnomad_frequency"], errors="raise")
    if ((frequency < 0) | (frequency > 1)).any():
        raise ValueError("Population frequency must be in [0,1]")
    review = table["review_status"].str.lower().map(REVIEW_WEIGHT).fillna(0).astype(int)
    pathogenic = table["clinical_significance"].str.contains("pathogenic", case=False)
    ranked = table.copy()
    ranked["review_weight"] = review
    ranked["population_frequency"] = frequency
    ranked["priority_score"] = review * 2 + pathogenic.astype(int) * 3
    ranked["interpretation_boundary"] = (
        "Educational evidence triage only; verify the current condition-specific ClinVar record, "
        "inheritance, zygosity, phenotype, ancestry-aware frequency and laboratory confirmation."
    )
    ranked = ranked.sort_values(["priority_score", "gene"], ascending=[False, True])
    summary = {
        "records": len(ranked),
        "genes": sorted(ranked["gene"].unique().tolist()),
        "source": "NCBI ClinVar ESummary snapshot",
        "clinical_use": False,
        "regional_prevalence_claim": False,
        "warning": "These two examples do not estimate prevalence in Azerbaijan or the Caucasus.",
    }
    return ranked.reset_index(drop=True), summary
