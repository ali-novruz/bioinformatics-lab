"""Reject empty-success pipelines: require the planted variant and gene counts."""
import argparse
import csv
import json
import subprocess
from pathlib import Path


def validate(root):
    truth = json.loads((root / 'fixture/truth.json').read_text())
    variants = subprocess.check_output([
        'bcftools', 'query', '-f', '%CHROM\t%POS\t%REF\t%ALT\t%FILTER[\t%GT]\n',
        str(root / 'variants/filtered.vcf.gz'),
    ], text=True).splitlines()
    expected = '\t'.join(map(str, [truth['chrom'], truth['position'], truth['ref'], truth['alt'], 'PASS', 1]))
    if variants != [expected]:
        raise ValueError(f'Expected exactly the planted passing haploid SNV {expected}; observed {variants}')
    with (root / 'rnaseq/smoke-rna.counts.tsv').open() as handle:
        rows = list(csv.DictReader((line for line in handle if not line.startswith('#')), delimiter='\t'))
    observed = next(int(list(row.values())[-1]) for row in rows if row['Geneid'] == truth['gene'])
    if observed < .95 * truth['pairs']:
        raise ValueError(f'Insufficient assigned fragments: {observed} / {truth["pairs"]}')
    summary = {'variant_matches_truth': True, 'assigned_fragments': observed, 'input_pairs': truth['pairs']}
    (root / 'validation.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    validate(parser.parse_args().root)
