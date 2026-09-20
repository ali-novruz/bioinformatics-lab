"""Run directories never overwrite an earlier experiment."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import uuid
from collections.abc import Iterable, Iterator, Mapping
from contextlib import contextmanager
from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any


def write_json(path: str | Path, value: Any) -> None:
    path = Path(path)
    staged = path.with_name(path.name + ".tmp")
    staged.write_bytes(
        (
            json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
        ).encode("utf-8")
    )
    staged.replace(path)


def input_record(root: str | Path, path: str | Path) -> dict[str, Any]:
    path = Path(path).resolve()
    root = Path(root).resolve()
    local = path.is_relative_to(root)
    return {
        "path": path.relative_to(root).as_posix() if local else str(path),
        "external": not local,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bytes": path.stat().st_size,
    }


def new_run(
    root: Path,
    project: str,
    inputs: Iterable[str | Path] = (),
    parameters: Mapping[str, Any] | None = None,
) -> Path:
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:6]
    out = Path(root) / "results/runs" / project / stamp
    out.mkdir(parents=True)
    packages = {}
    for name in [
        "bioinformatics-lab",
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn",
        "biopython",
        "pydeseq2",
        "matplotlib",
    ]:
        try:
            packages[name] = version(name)
        except PackageNotFoundError:
            pass
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True
    )
    dirty = subprocess.run(
        ["git", "status", "--porcelain"], cwd=root, capture_output=True, text=True
    )
    code_files = sorted(
        list((Path(root) / "src").rglob("*.py"))
        + list((Path(root) / "scripts").glob("*.py"))
        + list((Path(root) / "workflows").glob("*.sh"))
        + [
            p
            for p in [
                Path(root) / "pyproject.toml",
                Path(root) / "projects/registry.json",
            ]
            if p.exists()
        ]
    )
    source_hashes = {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in code_files
    }
    write_json(
        out / "run.json",
        {
            "project": project,
            "created_utc": stamp,
            "python": platform.python_version(),
            "platform": platform.platform(),
            "packages": packages,
            "git_commit": commit.stdout.strip() if commit.returncode == 0 else None,
            "working_tree_dirty": bool(dirty.stdout.strip()),
            "source_files_sha256": source_hashes,
            "command": [sys.executable, *sys.argv],
            "parameters": parameters or {},
            "inputs": [input_record(root, p) for p in inputs],
        },
    )
    receipt = os.environ.get("BIOLAB_RUN_RECEIPT")
    if receipt:
        with Path(receipt).open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(
                json.dumps({"run_path": out.relative_to(root).as_posix()}) + "\n"
            )
    return out


def finish_run(
    out: str | Path, *, status: str, elapsed_seconds: float, error: str | None = None
) -> None:
    """Seal outputs after execution; run.json is excluded to avoid a circular hash."""
    out = Path(out)
    record = json.loads((out / "run.json").read_text(encoding="utf-8"))
    record.update(
        {
            "status": status,
            "finished_utc": datetime.now(UTC).isoformat(),
            "elapsed_seconds": elapsed_seconds,
            "error": error,
            "outputs_sha256": {
                p.relative_to(out).as_posix(): hashlib.sha256(
                    p.read_bytes()
                ).hexdigest()
                for p in sorted(out.rglob("*"))
                if p.is_file() and p.name != "run.json"
            },
        }
    )
    write_json(out / "run.json", record)


@contextmanager
def recorded_run(
    root: Path,
    project: str,
    inputs: Iterable[str | Path] = (),
    parameters: Mapping[str, Any] | None = None,
) -> Iterator[Path]:
    out = new_run(root, project, inputs, parameters)
    start = time.perf_counter()
    try:
        yield out
    except BaseException as exc:
        finish_run(
            out,
            status="failed",
            elapsed_seconds=time.perf_counter() - start,
            error=str(exc),
        )
        raise
    else:
        finish_run(out, status="complete", elapsed_seconds=time.perf_counter() - start)
