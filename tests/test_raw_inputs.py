"""Regression checks for malformed FASTQ and silently changed downloaded inputs."""
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

from Bio import SeqIO
import pytest

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_generated_pairs_are_valid_fastq_with_matching_names(tmp_path):
    folder = tmp_path / 'fixture'
    load_script('create_raw_fixture').create_fixture(folder)
    truth = json.loads((folder / 'truth.json').read_text())
    mates = []
    for mate in (1, 2):
        with gzip.open(folder / f'R{mate}.fastq.gz', 'rt') as handle:
            # Independent parser rejects unequal sequence/quality lengths.
            records = list(SeqIO.parse(handle, 'fastq'))
        assert len(records) == truth['pairs']
        assert all(len(record.seq) == 101 for record in records)
        mates.append([record.id.rsplit('/', 1)[0] for record in records])
    assert mates[0] == mates[1]


def test_existing_raw_input_corruption_is_rejected_without_download(tmp_path, monkeypatch):
    downloader = load_script('fetch_raw_examples')
    manifest = json.loads((ROOT / 'datasets/raw-examples-manifest.json').read_text())
    entry = next(item for item in manifest['files'] if item['dataset'] == 'rnaseq')
    target = tmp_path / entry['path']
    target.parent.mkdir(parents=True)
    target.write_bytes(b'corrupted input')

    def unexpected_download(*args, **kwargs):
        pytest.fail('Changed existing input must fail before network access')

    monkeypatch.setattr(downloader.urllib.request, 'urlopen', unexpected_download)
    with pytest.raises(ValueError, match='Existing input changed'):
        downloader.fetch('rnaseq', tmp_path)


def test_cache_and_local_manifest_cannot_override_reference(tmp_path, monkeypatch):
    downloader=load_script('fetch_data')
    monkeypatch.setattr(downloader,'RAW',tmp_path)
    name='NC_001422.1.fasta'
    corrupt=b'>changed\nACGT\n'
    (tmp_path/name).write_bytes(corrupt)
    (tmp_path/'provenance.json').write_text(json.dumps({name:{'sha256':hashlib.sha256(corrupt).hexdigest()}}))
    with pytest.raises(ValueError,match='reference snapshot'):
        downloader.intact([name])
