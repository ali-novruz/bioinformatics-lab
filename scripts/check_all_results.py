"""Validate every published run, immutable snapshot and example input."""

import hashlib
import json
from pathlib import Path

from biolab.provenance import verify_outputs, verify_sources

ROOT = Path(__file__).resolve().parents[1]


def main():
    record_count = 0
    archived = 0
    current = 0
    for record_path in (ROOT / "results").rglob("run.json"):
        if "runs" in record_path.relative_to(ROOT / "results").parts:
            continue
        record = json.loads(record_path.read_text(encoding="utf-8"))
        if not record.get("source_files_sha256"):
            continue
        summary = verify_sources(ROOT, record)
        verify_outputs(record_path.parent, record)
        record_count += 1
        archived += summary["archived"]
        current += summary["current"]
    manifests = [ROOT / "datasets/examples/manifest.json"]
    for manifest in manifests:
        for item in json.loads(manifest.read_text(encoding="utf-8"))["files"]:
            path = ROOT / item["path"]
            assert path.stat().st_size == item["bytes"], path
            assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], path
    for path in (ROOT / "results").rglob("snapshot.json"):
        if "runs" in path.relative_to(ROOT / "results").parts:
            continue
        for name, expected in json.loads(path.read_text(encoding="utf-8"))[
            "sha256"
        ].items():
            assert (
                hashlib.sha256((path.parent / name).read_bytes()).hexdigest()
                == expected
            ), (path, name)
    print(
        f"{record_count} published runs; {current} current and {archived} archived source matches; example inputs and all snapshots verified"
    )


if __name__ == "__main__":
    main()
