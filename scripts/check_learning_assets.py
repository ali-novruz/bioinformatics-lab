"""Verify curated source inventory, unchanged books, and course result snapshots."""

import hashlib
import json
from pathlib import Path

from biolab.provenance import verify_sources

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    catalog = json.loads(
        (ROOT / "resources/unec/catalog.json").read_text(encoding="utf-8")
    )
    files = catalog["files"]
    assert len(files) == catalog["total"] == 68
    assert len({f["sha256"] for f in files}) == catalog["byte_unique"] == 61
    by_id = {f["id"]: f for f in files}
    assert len(by_id) == 68
    for row in files:
        if row["duplicate_of"]:
            assert by_id[row["duplicate_of"]]["sha256"] == row["sha256"]
    books = json.loads(
        (ROOT / "resources/books/pdf-manifest.json").read_text(encoding="utf-8")
    )["books"]
    for book in books:
        path = ROOT / book["path"]
        assert path.stat().st_size == book["bytes"], path
        assert digest(path) == book["sha256"], path
        assert path.read_bytes().startswith(b"%PDF-"), path
    base = ROOT / "results/course-projects"
    snapshot = json.loads((base / "snapshot.json").read_text(encoding="utf-8"))
    for name, expected in snapshot["sha256"].items():
        assert digest(base / name) == expected, name
    references = json.loads((base / "references.json").read_text(encoding="utf-8"))[
        "references"
    ]
    assert len(references) == 13
    for old_name, canonical_name in references.items():
        assert not (base / old_name).exists(), old_name
        canonical = ROOT / canonical_name
        assert canonical.is_file(), canonical_name
        assert canonical_name.startswith("results/expanded-projects/")
    for run in base.glob("*/run.json"):
        record = json.loads(run.read_text(encoding="utf-8"))
        verify_sources(ROOT, record)
    print(
        f"{len(files)} source records, {len(books)} original PDFs, {len(snapshot['sha256'])} unique course files, {len(references)} canonical result references and recorded source hashes verified"
    )


if __name__ == "__main__":
    main()
