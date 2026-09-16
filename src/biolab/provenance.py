"""Verify recorded source bytes against current code or immutable source archives."""
import hashlib
import json
from pathlib import Path
import zipfile


def verify_outputs(out,record):
    """New sealed runs declare all output bytes; older records remain readable."""
    out=Path(out).resolve()
    hashes=record.get('outputs_sha256')
    if hashes is None:
        return 0
    for name,expected in hashes.items():
        path=(out/name).resolve()
        if not path.is_relative_to(out) or not path.is_file():
            raise ValueError(f'Missing or invalid recorded output: {name}')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            raise ValueError(f'Output checksum mismatch: {name}')
    actual={p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file() and p.name!='run.json'}
    if actual!=set(hashes):
        raise ValueError('Unrecorded outputs in sealed run')
    return len(hashes)


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
