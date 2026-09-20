import itertools

import pytest
from Bio.Align import PairwiseAligner
from Bio.Seq import Seq

from biolab.sequence import (
    align,
    clean_dna,
    gc_content,
    motif_enrichment,
    motif_positions,
    reverse_complement,
    seed_search,
)


def test_iupac_reverse_complement():
    seq = "ACGTRYSWKMBDHVN"
    assert reverse_complement(seq) == str(Seq(seq).reverse_complement())
    assert reverse_complement(reverse_complement(seq)) == seq


def test_gc_missing_and_ambiguous():
    assert gc_content("NN") is None
    assert gc_content("aNgC") == pytest.approx(2 / 3)
    with pytest.raises(ValueError):
        clean_dna("ACGU")


def test_overlapping_motif():
    assert motif_positions("AAAA", "AA") == [0, 1, 2]
    assert motif_positions("ACGT", "RY") == [0, 2]
    with pytest.raises(ValueError):
        motif_positions("ACG", "")


@pytest.mark.parametrize("mode", ["global", "local"])
def test_dp_exhaustive_against_biopython(mode):
    ref = PairwiseAligner(
        mode=mode,
        match_score=2,
        mismatch_score=-1,
        open_gap_score=-2,
        extend_gap_score=-2,
    )
    words = ["".join(x) for n in range(1, 4) for x in itertools.product("AC", repeat=n)]
    for a in words:
        for b in words:
            result = align(a, b, mode)
            assert result.score == ref.score(a, b)
            assert (
                result.query.replace("-", "")
                == a[result.query_start : result.query_end]
            )
            assert (
                result.target.replace("-", "")
                == b[result.target_start : result.target_end]
            )
            score = sum(
                -2 if "-" in (x, y) else 2 if x == y else -1
                for x, y in zip(result.query, result.target, strict=True)
            )
            assert score == result.score


def test_empty_and_limits():
    assert align("", "AC").score == -4
    assert align("", "AC", "local").score == 0
    assert align("A", "C", "local").identity is None
    with pytest.raises(ValueError):
        align("A", "C", "invalid")
    with pytest.raises(ValueError):
        align("AAA", "CCC", max_cells=2)
    with pytest.raises(ValueError):
        align("A", "A", gap=1)


def test_motif_background_and_seed():
    top = motif_enrichment(["AAAAAA"], ["CCCCCC"], k=2)[0]
    assert top["kmer"] == "AA" and top["log2_enrichment"] > 0
    assert (
        seed_search("ACGT", {"same": "ACGT", "different": "AAAA"}, k=2)[0]["id"]
        == "same"
    )
