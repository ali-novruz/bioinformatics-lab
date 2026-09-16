"""Deterministic unique paired reads with one known haploid SNV, for CI only."""
import argparse
import gzip
import json
import random
from pathlib import Path


def create_fixture(output):
    output.mkdir(parents=True, exist_ok=False)
    rng = random.Random(20260916)
    reference = ''.join(rng.choices('ACGT', k=6000))
    position = 2500  # VCF uses one-based coordinates.
    ref = reference[position - 1]
    alt = next(base for base in 'ACGT' if base != ref)
    donor = reference[:position - 1] + alt + reference[position:]
    (output / 'reference.fa').write_text('>toy\n' + reference + '\n')
    (output / 'genes.gtf').write_text(
        'toy\tfixture\texon\t1001\t5000\t.\t+\t.\tgene_id "toy_gene"; transcript_id "toy_tx";\n'
    )
    starts = list(range(1050, 4000, 7))
    complement = str.maketrans('ACGT', 'TGCA')
    # Distinct fragment starts survive duplicate marking. Reads are 101 bp.
    for mate in (1, 2):
        with gzip.open(output / f'R{mate}.fastq.gz', 'wt', newline='\n') as handle:
            for index, start in enumerate(starts):
                read = donor[start:start + 101] if mate == 1 else donor[start + 149:start + 250].translate(complement)[::-1]
                handle.write(f'@fragment{index}/{mate}\n{read}\n+\n{"I" * len(read)}\n')
    (output / 'truth.json').write_text(json.dumps({
        'kind': 'synthetic software fixture; not biological evidence',
        'seed': 20260916, 'chrom': 'toy', 'position': position,
        'ref': ref, 'alt': alt, 'pairs': len(starts), 'gene': 'toy_gene',
    }, indent=2) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    create_fixture(parser.parse_args().output)
