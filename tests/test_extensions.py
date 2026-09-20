import numpy as np
import pytest
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from scipy.stats import fisher_exact

from biolab.enrichment import over_representation
from biolab.orfs import find_orfs
from biolab.phylogeny import alignment_matrix, bootstrap_tree, canonical_split


def test_enrichment_matches_fisher_and_tests_zero_overlap_terms():
    universe = set(range(20))
    selected = {0, 1, 2, 3}
    sets = {"hit": {0, 1, 2, 4, 5}, "zero": {10, 11, 12}}
    result = over_representation(selected, universe, sets).set_index("term")
    expected = fisher_exact([[3, 1], [2, 14]], alternative="greater").pvalue
    assert np.isclose(result.loc["hit", "pvalue"], expected)
    assert result.loc["zero", "pvalue"] == 1
    assert result.loc["hit", "padj"] >= expected


def test_empty_selection_and_unmeasured_selected_gene():
    result = over_representation([], range(5), {"a": {1, 2}})
    assert result.pvalue.iloc[0] == 1
    with pytest.raises(ValueError):
        over_representation({9}, range(5), {})


def test_orf_stops_at_first_stop_and_translates_correctly():
    found = find_orfs("CCCATGAAATAAATGCCCTAG", min_aa=2)
    plus = [r for r in found if r["strand"] == "+"]
    assert [r["protein"] for r in plus] == ["MK", "MP"]
    assert plus[0]["segments0"] == [(3, 12)]


@pytest.mark.parametrize("reverse", [False, True])
def test_circular_orf_coordinates_reconstruct_translation(reverse):
    # Rotate a complete ATG AAA TAA ORF so it crosses the reference origin.
    sequence = "AAATAACCCATG"
    if reverse:
        sequence = str(Seq(sequence).reverse_complement())
    strand = "-" if reverse else "+"
    hits = [
        r
        for r in find_orfs(sequence, min_aa=2, circular=True)
        if r["strand"] == strand and r["wraps_origin"]
    ]
    assert len(hits) == 1
    row = hits[0]
    parts = [sequence[a:b] for a, b in row["segments0"]]
    coding = (
        "".join(str(Seq(p).reverse_complement()) for p in parts)
        if reverse
        else "".join(parts)
    )
    assert coding == "ATGAAATAA"
    assert row["protein"] == "MK"
    assert not any(
        r["strand"] == strand for r in find_orfs(sequence, min_aa=2, circular=False)
    )


def test_ambiguous_or_empty_orf_input_rejected():
    for sequence in ["", "ATGNNTAA"]:
        with pytest.raises(ValueError):
            find_orfs(sequence)


def test_phylogeny_known_split_and_complete_deletion():
    records = [
        SeqRecord(Seq(s), id=n)
        for n, s in [("a", "AAAA-N"), ("b", "AAAAAN"), ("c", "TTTTAN"), ("d", "TTTTAN")]
    ]
    names, matrix, mask = alignment_matrix(records)
    assert mask.tolist() == [True, True, True, True, False, False]
    tree, distances, support = bootstrap_tree(names, matrix, repeats=20)
    assert support["a;b"] == 100
    assert distances[0, 1] == 0 and distances[0, 2] == 1
    assert canonical_split({"c", "d"}, set(names)) == ("a", "b")
    assert not tree.rooted


def test_uninformative_alignment_rejected():
    with pytest.raises(ValueError):
        alignment_matrix([SeqRecord(Seq("NN--"), id=str(i)) for i in range(4)])
