"""Retrieve the pinned ISLP Khan microarray split; preserve checksum failures."""
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def fetch():
    manifest = json.loads((ROOT / 'datasets/khan-manifest.json').read_text())
    for item in manifest['files']:
        path = ROOT / item['path']
        if path.exists():
            data = path.read_bytes()
        else:
            with urllib.request.urlopen(item['url'], timeout=90) as response:
                data = response.read()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError(f'Input integrity failed: {path.name}')
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print('Four pinned Khan input files verified')
    return ROOT / 'datasets/raw/khan'


if __name__ == '__main__':
    fetch()
