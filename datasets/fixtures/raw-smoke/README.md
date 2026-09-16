# Deterministic raw-read fixture

Generate with `python scripts/create_raw_fixture.py --output /tmp/biolab-raw/fixture`.
Seed 20260916 produces a nonrepetitive 6 kb reference, 422 distinct paired fragments
(101 bp reads, 250 bp inserts), one haploid SNV at position 2500, and one exon.
Quality strings are generated from read lengths.

CI requires exactly the known PASS variant and at least 95% of fragments assigned
to the gene. This catches malformed FASTQ, empty alignments and empty VCF/count
outputs. These sequences are synthetic and provide software verification only.
