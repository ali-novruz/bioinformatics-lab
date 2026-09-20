"""Sequence operations and exact linear-gap dynamic programming.

Coordinates in Alignment are Python-style zero-based half-open intervals.
These O(m*n) algorithms are intended for short teaching sequences.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from itertools import product
from typing import Any

import numpy as np

DNA = frozenset("ACGTRYSWKMBDHVN")
COMPLEMENT = str.maketrans("ACGTRYSWKMBDHVN", "TGCAYRSWMKVHDBN")
IUPAC = dict(
    zip(
        "ACGTRYSWKMBDHVN",
        [
            "A",
            "C",
            "G",
            "T",
            "AG",
            "CT",
            "CG",
            "AT",
            "GT",
            "AC",
            "CGT",
            "AGT",
            "ACT",
            "ACG",
            "ACGT",
        ],
        strict=True,
    )
)


def clean_dna(seq: str) -> str:
    seq = "".join(seq.split()).upper()
    invalid = set(seq) - DNA
    if invalid:
        raise ValueError(f"Invalid DNA symbols: {sorted(invalid)}")
    return seq


def reverse_complement(seq: str) -> str:
    return clean_dna(seq).translate(COMPLEMENT)[::-1]


def gc_content(seq: str) -> float | None:
    """GC fraction among unambiguous A/C/G/T bases; None if none exist."""
    seq = clean_dna(seq)
    denom = sum(seq.count(b) for b in "ACGT")
    return (seq.count("G") + seq.count("C")) / denom if denom else None


def motif_positions(seq: str, motif: str) -> list[int]:
    """Overlapping IUPAC motif matches, 0-based; ambiguous input bases don't match."""
    seq, motif = clean_dna(seq), clean_dna(motif)
    if not motif:
        raise ValueError("Motif must not be empty")
    pattern = "".join(f"[{IUPAC[b]}]" for b in motif)
    return [m.start() for m in re.finditer(f"(?={pattern})", seq)]


def sequence_summary(seq: str) -> dict[str, Any]:
    seq = clean_dna(seq)
    return {
        "length": len(seq),
        "counts": dict(Counter(seq)),
        "gc_fraction_acgt_only": gc_content(seq),
        "ambiguous_bases": sum(b not in "ACGT" for b in seq),
        "rna": seq.replace("T", "U"),
        "reverse_complement": reverse_complement(seq),
        "frame0_codons": dict(
            Counter(seq[i : i + 3] for i in range(0, len(seq) - 2, 3))
        ),
        "untranslated_tail": len(seq) % 3,
    }


@dataclass(frozen=True)
class Alignment:
    query: str
    target: str
    score: float
    query_start: int
    query_end: int
    target_start: int
    target_end: int
    mode: str

    @property
    def identity(self) -> float | None:
        return (
            sum(
                a == b and a != "-"
                for a, b in zip(self.query, self.target, strict=True)
            )
            / len(self.query)
            if self.query
            else None
        )

    def to_dict(self) -> dict[str, Any]:
        return {**asdict(self), "identity_all_alignment_columns": self.identity}


def align(
    query: str,
    target: str,
    mode: str = "global",
    match: float = 2.0,
    mismatch: float = -1.0,
    gap: float = -2.0,
    max_cells: int = 4_000_000,
    *,
    backend: str = "python",
) -> Alignment:
    if mode not in {"global", "local"}:
        raise ValueError("mode must be global or local")
    if not all(math.isfinite(v) for v in (match, mismatch, gap)) or gap > 0:
        raise ValueError("Scoring must be finite, with a nonpositive gap penalty")
    query, target = clean_dna(query), clean_dna(target)
    n, m = len(query), len(target)
    if (n + 1) * (m + 1) > max_cells:
        raise ValueError("DP matrix too large; use a production aligner")
    if backend not in {"python", "numpy"}:
        raise ValueError("backend must be python or numpy")
    scores: Any
    scores = (
        np.zeros((n + 1, m + 1))
        if backend == "numpy"
        else [[0.0] * (m + 1) for _ in range(n + 1)]
    )
    trace = [bytearray(m + 1) for _ in range(n + 1)]
    if mode == "global":
        for i in range(1, n + 1):
            scores[i][0], trace[i][0] = i * gap, 2
        for j in range(1, m + 1):
            scores[0][j], trace[0][j] = j * gap, 3
    best, best_pos = 0.0, (0, 0)
    if backend == "numpy":
        q, t = np.array(list(query)), np.array(list(target))
        for diagonal in range(2, n + m + 1):
            ii = np.arange(max(1, diagonal - m), min(n, diagonal - 1) + 1)
            jj = diagonal - ii
            np_options = np.stack(
                [
                    scores[ii - 1, jj - 1]
                    + np.where(q[ii - 1] == t[jj - 1], match, mismatch),
                    scores[ii - 1, jj] + gap,
                    scores[ii, jj - 1] + gap,
                ]
            )
            vals = np_options.max(axis=0)
            dirs = np_options.argmax(axis=0) + 1
            if mode == "local":
                dirs[vals <= 0] = 0
                vals = np.maximum(vals, 0)
            scores[ii, jj] = vals
            for row, col, direction in zip(ii, jj, dirs, strict=True):
                trace[row][col] = int(direction)
        # np.argmax is row-major: same first-max cell as the Python loop.
        found_pos = np.unravel_index(np.argmax(scores), scores.shape)
        best_pos = (int(found_pos[0]), int(found_pos[1]))
    else:
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                py_options = [
                    scores[i - 1][j - 1]
                    + (match if query[i - 1] == target[j - 1] else mismatch),
                    scores[i - 1][j] + gap,
                    scores[i][j - 1] + gap,
                ]
                val = max(py_options)
                if mode == "local" and val <= 0:
                    val, direction = 0.0, 0
                else:
                    direction = py_options.index(val) + 1
                scores[i][j], trace[i][j] = val, direction
                if val > best:
                    best, best_pos = val, (i, j)
    i, j = (n, m) if mode == "global" else best_pos
    end_i, end_j = i, j
    final = scores[i][j]
    a, b = [], []
    while i > 0 or j > 0:
        d = trace[i][j]
        if not d:
            break
        if d == 1:
            a.append(query[i - 1])
            b.append(target[j - 1])
            i -= 1
            j -= 1
        elif d == 2:
            a.append(query[i - 1])
            b.append("-")
            i -= 1
        else:
            a.append("-")
            b.append(target[j - 1])
            j -= 1
    return Alignment(
        "".join(reversed(a)), "".join(reversed(b)), final, i, end_i, j, end_j, mode
    )


def kmer_counts(sequences: Iterable[str], k: int = 3) -> Counter[str]:
    if not isinstance(k, int) or k < 1 or k > 10:
        raise ValueError("k must be an integer from 1 to 10")
    counts = Counter()
    for seq in sequences:
        seq = clean_dna(seq)
        counts.update(
            seq[i : i + k]
            for i in range(len(seq) - k + 1)
            if set(seq[i : i + k]) <= set("ACGT")
        )
    return counts


def motif_enrichment(
    foreground: Iterable[str],
    background: Iterable[str],
    k: int = 3,
    pseudocount: float = 1.0,
) -> list[dict[str, Any]]:
    if k > 6:
        raise ValueError("Use k<=6 for this exhaustive teaching method")
    if not math.isfinite(pseudocount) or pseudocount <= 0:
        raise ValueError("Positive pseudocount required")
    fg, bg = kmer_counts(foreground, k), kmer_counts(background, k)
    space = 4**k
    rows = []
    for letters in product("ACGT", repeat=k):
        word = "".join(letters)
        p = (fg[word] + pseudocount) / (sum(fg.values()) + pseudocount * space)
        q = (bg[word] + pseudocount) / (sum(bg.values()) + pseudocount * space)
        rows.append(
            {
                "kmer": word,
                "foreground": fg[word],
                "background": bg[word],
                "log2_enrichment": math.log2(p / q),
            }
        )
    return sorted(rows, key=lambda r: (-r["log2_enrichment"], r["kmer"]))


def seed_search(
    query: str, database: Mapping[str, str], k: int = 3
) -> list[dict[str, Any]]:
    """Exact distinct k-mer overlap baseline; NOT BLAST, no E-values."""
    q = set(kmer_counts([query], k))
    return sorted(
        [
            {"id": name, "shared_distinct_kmers": len(q & set(kmer_counts([seq], k)))}
            for name, seq in database.items()
        ],
        key=lambda r: (-r["shared_distinct_kmers"], r["id"]),
    )
