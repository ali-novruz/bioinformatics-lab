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
    "Ala": "A",
    "Arg": "R",
    "Asn": "N",
    "Asp": "D",
    "Cys": "C",
    "Gln": "Q",
    "Glu": "E",
    "Gly": "G",
    "His": "H",
    "Ile": "I",
    "Leu": "L",
    "Lys": "K",
    "Met": "M",
    "Phe": "F",
    "Pro": "P",
    "Ser": "S",
    "Thr": "T",
    "Trp": "W",
    "Tyr": "Y",
    "Val": "V",
    "Ter": "*",
}
_P_TERM = re.compile(r"\(p\.([^)]*)\)")
_START = re.compile(r"^([A-Z][a-z]{2})(\d+)")
_INFRAME = re.compile(r"^(_[A-Z][a-z]{2}\d+)?(del|dup|ins[A-Za-z]+|delins[A-Za-z]+)$")
OTHER_CLASSIFICATIONS = {
    "other",
    "not provided",
    "no classification for the single variant",
}


def review_stars(status: str) -> int:
    if status not in REVIEW_STARS:
        raise ValueError(f"Unknown ClinVar review status: {status!r}")
    return REVIEW_STARS[status]


def classification_group(description: str) -> str:
    """Collapse aggregate germline classifications into five teaching groups."""
    head = description.split(";")[0].strip()
    if head in CLASS_GROUPS:
        return CLASS_GROUPS[head]
    if head in OTHER_CLASSIFICATIONS:
        return "Other"
    raise ValueError(f"Unknown ClinVar classification: {description!r}")


def assigned_gene(genes: str) -> str | None:
    """The single named gene of a record; LOC regulatory elements are ignored."""
    named = {g for g in genes.split(";") if g and not g.startswith("LOC")}
    return named.pop() if len(named) == 1 else None


def protein_consequence(title: str) -> tuple[str, int | None, str]:
    """Consequence class, first protein position and short change from a ClinVar title.

    Reads the HGVS protein term on the record's transcript, e.g.
    "NM_000243.3(MEFV):c.2080A>G (p.Met694Val)" -> ("missense", 694, "M694V").
    Titles without a protein term (intronic, UTR, splice region, large deletions)
    are "no_protein_term". Unrecognised protein terms raise.
    """
    match = _P_TERM.search(title)
    if not match:
        return "no_protein_term", None, ""
    term = match.group(1)
    repeat = re.fullmatch(r"(\d+)([A-Z]+)\[(\d+)\]", term)
    if repeat:
        return "inframe", int(repeat.group(1)), term
    head = _START.match(term)
    if not head or head.group(1) not in _AA3:
        raise ValueError(f"Unrecognised HGVS protein term {term!r} in {title!r}")
    ref, pos, rest = head.group(1), int(head.group(2)), term[head.end() :]
    short = f"{_AA3[ref]}{pos}"
    if ref == "Ter" or re.search(r"_Ter\d+del", rest):
        return "stop_loss", pos, f"{short}ext"
    if rest.endswith("="):
        return "synonymous", pos, f"{short}="
    if "fs" in rest:
        return "frameshift", pos, f"{short}fs"
    if rest in {"Ter", "*"} or (rest.endswith("Ter") and ("ins" in rest)):
        return "nonsense", pos, f"{short}*"
    if rest in _AA3:
        return "missense", pos, f"{short}{_AA3[rest]}"
    if _INFRAME.fullmatch(rest):
        return "inframe", pos, f"{short}{rest}"
    raise ValueError(f"Unrecognised HGVS protein change {term!r} in {title!r}")
