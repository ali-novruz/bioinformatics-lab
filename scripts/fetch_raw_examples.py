"""Download immutable small raw-read examples and verify committed SHA-256 hashes."""

import argparse
import hashlib
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fetch(dataset, output):
    manifest = json.loads((ROOT / "datasets/raw-examples-manifest.json").read_text())
    selected = [
        entry
        for entry in manifest["files"]
        if dataset == "all" or entry["dataset"] == dataset
    ]
    for entry in selected:
        target = output / entry["path"]
        if target.exists():
            if hashlib.sha256(target.read_bytes()).hexdigest() != entry["sha256"]:
                raise ValueError(
                    f"Existing input changed: {target}. Restore it or choose a new directory."
                )
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        for attempt in range(3):
            try:
                with urllib.request.urlopen(entry["url"], timeout=90) as response:
                    data = response.read()
                break
            except OSError:
                if attempt == 2:
                    raise
                time.sleep(2**attempt)
        if (
            len(data) != entry["bytes"]
            or hashlib.sha256(data).hexdigest() != entry["sha256"]
        ):
            raise ValueError(f"Input integrity check failed: {entry['url']}")
        temporary = target.with_suffix(target.suffix + ".part")
        temporary.write_bytes(data)
        temporary.replace(target)
    (output / "verified-manifest.json").write_text(
        json.dumps({**manifest, "files": selected}, indent=2) + "\n"
    )
    print(f"Verified {len(selected)} inputs in {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset", choices=["rnaseq", "variants", "all"], default="all"
    )
    parser.add_argument("--output", type=Path, default=ROOT / "datasets/raw/examples")
    args = parser.parse_args()
    fetch(args.dataset, args.output.resolve())
