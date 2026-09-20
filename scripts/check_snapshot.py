"""Verify that published Linux result files retain their original SHA-256 bytes."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "results/raw-examples"


def check_snapshot(root=ROOT):
    manifest = json.loads((root / "snapshot.json").read_text())
    for name, expected in manifest["sha256"].items():
        target = (root / name).resolve()
        if not target.is_relative_to(root.resolve()):
            raise ValueError(f"Snapshot path escapes its directory: {name}")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(
                f"Snapshot bytes changed: {name}: expected {expected}, got {actual}"
            )
    print(f"{len(manifest['sha256'])} published result hashes verified")


if __name__ == "__main__":
    check_snapshot()
