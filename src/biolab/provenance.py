"""Verify recorded source bytes against current code or immutable source archives."""
import hashlib
import json
from pathlib import Path
import zipfile


def verify_sources(root, record):
    root = Path(root)
    manifest = root / 'results/source-archives/manifest.json'
    archived = {}
    if manifest.exists():
        for entry in json.loads(manifest.read_text(encoding='utf-8'))['archives']:
            path = root / entry['path']
            if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
                raise ValueError(f'Source archive checksum mismatch: {path.name}')
            with zipfile.ZipFile(path) as z:
                for name in z.namelist():
                    archived.setdefault(name, set()).add(hashlib.sha256(z.read(name)).hexdigest())
    counts = {'current': 0, 'archived': 0}
    hashes = record.get('source_files_sha256')
    if not hashes:
        raise ValueError('No recorded source hashes')
    for name, expected in hashes.items():
        name = name.replace('\\', '/')
        path = root / name
        if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == expected:
            counts['current'] += 1
        elif expected in archived.get(name, set()):
            counts['archived'] += 1
        else:
            raise ValueError(f'Unverifiable recorded source: {name}')
    return counts
