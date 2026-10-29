import json
from pathlib import Path

from Bio import SeqIO

from biolab.orfs import find_orfs

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets/examples/orfs"
STORED = ROOT / "results/showcase/phix174-orf"


def test_genbank_sequence_matches_analysed_fasta():
    record = SeqIO.read(DATA / "NC_001422.1.gb", "genbank")
    fasta = SeqIO.read(DATA / "NC_001422.1.fasta", "fasta")
    assert str(record.seq).upper() == str(fasta.seq).upper()
    assert sum(f.type == "CDS" for f in record.features) == 11


def test_orf_scan_contains_every_curated_cds_exactly():
    record = SeqIO.read(DATA / "NC_001422.1.gb", "genbank")
    candidates = find_orfs(str(record.seq), min_aa=30, circular=True)
    found = {(c["strand"], tuple(map(tuple, c["segments0"]))) for c in candidates}
    for feature in record.features:
        if feature.type != "CDS":
            continue
        segments = tuple((int(p.start), int(p.end)) for p in feature.location.parts)
        assert ("+", segments) in found, feature.qualifiers["locus_tag"]


def test_stored_showcase_summary():
    summary = json.loads((STORED / "summary.json").read_text(encoding="utf-8"))
    assert summary["candidates"] == 114
    assert summary["loci"] == 36
    assert summary["gene_loci_recovered"] == summary["curated_gene_loci"] == 10
    assert summary["exact_starts_recovered"] == 11
    assert summary["overlapping_pairs"] == summary["overlapping_pairs_other_frame"] == 8
    assert summary["null"]["real_loci_ge_100aa"] > summary["null"]["null_max_loci_ge_100aa"]


def test_live_lab_bundle_matches_stored_results():
    text = (ROOT / "projects/beginner/orf-discovery/live/data.js").read_text(encoding="utf-8")
    bundle = json.loads(text.removeprefix("window.PHIX=").rstrip().rstrip(";"))
    fasta = SeqIO.read(DATA / "NC_001422.1.fasta", "fasta")
    stored = json.loads((STORED / "summary.json").read_text(encoding="utf-8"))
    assert bundle["sequence"] == str(fasta.seq).upper()
    assert bundle["summary"] == stored
