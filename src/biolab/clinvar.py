"""Parse ClinVar ESummary records for evidence-level teaching analyses."""

from __future__ import annotations

import re

# ClinVar review status -> review stars, as displayed by ClinVar.
REVIEW_STARS = {
    "practice guideline": 4,
    "reviewed by expert panel": 3,
    "criteria provided, multiple submitters, no conflicts": 2,
    "criteria provided, conflicting classifications": 1,
    "criteria provided, single submitter": 1,
    "no assertion criteria provided": 0,
    "no classification provided": 0,
    "no classification for the single variant": 0,
}
CLASS_GROUPS = {
    "Pathogenic": "P/LP",
    "Likely pathogenic": "P/LP",
    "Pathogenic/Likely pathogenic": "P/LP",
    "Uncertain significance": "VUS",
    "Likely benign": "B/LB",
    "Benign": "B/LB",
    "Benign/Likely benign": "B/LB",
    "Conflicting classifications of pathogenicity": "Conflicting",
}
_AA3 = {
    "Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E",
    "Gly": "G", "His": "H", "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F",
    "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V", "Ter": "*",
}
_P_HGVS = re.compile(r"\(p\.([A-Z][a-z]{2})(\d+)([A-Za-z]{2,}|=|\*)?")


def review_stars(status: str) -> int:
    if status not in REVIEW_STARS:
        raise ValueError(f"Unknown ClinVar review status: {status!r}")
    return REVIEW_STARS[status]


def classification_group(description: str) -> str:
    """Collapse aggregate germline classifications into five teaching groups."""
    head = description.split(";")[0].strip()
    return CLASS_GROUPS.get(head, "Other")


def assigned_gene(genes: str) -> str | None:
    """The single named gene of a record; LOC regulatory elements are ignored."""
    named = {g for g in genes.split(";") if g and not g.startswith("LOC")}
    return named.pop() if len(named) == 1 else None


def protein_consequence(title: str) -> tuple[str, int | None, str]:
    """Consequence class, protein position and short change from a ClinVar title.

    Reads the HGVS protein term on the record's canonical transcript, e.g.
    "NM_000243.3(MEFV):c.2080A>G (p.Met694Val)" -> ("missense", 694, "M694V").
    Records without a protein term are "noncoding" (intronic, UTR, splice region).
    """
    match = _P_HGVS.search(title)
    if not match:
        return "noncoding", None, ""
    ref, pos, rest = match.group(1), int(match.group(2)), match.group(3) or ""
    if ref not in _AA3:
        raise ValueError(f"Unknown amino acid {ref!r} in {title!r}")
    short_ref = _AA3[ref]
    if rest == "=":
        return "synonymous", pos, f"{short_ref}{pos}="
    if rest in {"Ter", "*"}:
        return "nonsense", pos, f"{short_ref}{pos}*"
    if rest.startswith("fs") or "fs" in title[match.end() : match.end() + 8]:
        return "frameshift", pos, f"{short_ref}{pos}fs"
    if rest in _AA3:
        return "missense", pos, f"{short_ref}{pos}{_AA3[rest]}"
    return "inframe", pos, f"{short_ref}{pos}{rest}"
