"""One entry point for listing, fetching and running the implemented projects."""

import argparse
import importlib.util
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from biolab.registry import load_registry
from biolab.reporting import finish_run, new_run, write_json


def run_projects(args: argparse.Namespace, root: Path) -> int:
    ROOT = root
    registry = ROOT / "projects/registry.json"
    projects = load_registry(ROOT)
    if args.command == "list":
        for p in projects:
            print(
                f"{p['id']:15} {'offline' if p['offline'] else 'download':8} {p['title']}"
            )
        return 0
    selected = (
        projects
        if args.project == "all"
        else [p for p in projects if p["id"] == args.project]
    )
    if not selected:
        raise ValueError("Unknown project; run biolab list")
    skipped = [p["id"] for p in selected if args.offline and not p["offline"]]
    if skipped and args.project != "all":
        raise ValueError("This project requires downloadable inputs; omit --offline")
    selected = [p for p in selected if p["id"] not in skipped]
    if (
        any(p.get("research") for p in selected)
        and importlib.util.find_spec("pydeseq2") is None
    ):
        raise ValueError(
            'RNA-seq requires research dependencies: python -m pip install -e ".[dev,research]"'
        )
    out = new_run(
        ROOT,
        "project-suite",
        [registry],
        {"project": args.project, "offline": args.offline},
    )
    report: dict[str, object] = {
        "status": "running",
        "selected": [p["id"] for p in selected],
        "skipped_requires_download": skipped,
        "projects": [],
    }
    write_json(out / "suite.json", report)
    suite_start = time.perf_counter()
    projects_report: list[dict[str, object]] = []
    report["projects"] = projects_report
    failures = 0
    for p in selected:
        print(f"Running {p['id']}...", flush=True)
        log = out / (p["id"] + ".log")
        commands = [
            [sys.executable, str(ROOT / "scripts/fetch_data.py"), "--dataset", dataset]
            for dataset in ([] if args.offline else p["fetch"])
        ]
        commands.append(
            [sys.executable, str(ROOT / "scripts" / p["script"]), *p["args"]]
        )
        status = 0
        start = time.perf_counter()
        receipt = out / (p["id"] + ".receipts.jsonl")
        environment = {**os.environ, "BIOLAB_RUN_RECEIPT": str(receipt)}
        executed = []
        error = None
        with log.open("w", encoding="utf-8", newline="\n") as handle:
            for command in commands:
                executed.append(command)
                try:
                    completed = subprocess.run(
                        command,
                        cwd=ROOT,
                        stdout=handle,
                        stderr=subprocess.STDOUT,
                        env=environment,
                    )
                    status = completed.returncode
                except OSError as exc:
                    status = 127
                    error = str(exc)
                    handle.write(error + "\n")
                if status:
                    break
        elapsed = time.perf_counter() - start
        run_paths = (
            [
                json.loads(line)["run_path"]
                for line in receipt.read_text(encoding="utf-8").splitlines()
            ]
            if receipt.exists()
            else []
        )
        if status == 0 and not run_paths:
            status = 1
            error = "Project exited without recording a run"
        for run_path in run_paths:
            finish_run(
                ROOT / run_path,
                status="complete" if status == 0 else "failed",
                elapsed_seconds=elapsed,
                error=error,
            )
        projects_report.append(
            {
                "id": p["id"],
                "exit_code": status,
                "log": log.name,
                "commands": executed,
                "elapsed_seconds": elapsed,
                "run_paths": run_paths,
                "error": error,
            }
        )
        if status:
            failures += 1
        print(f"{p['id']}: {'FAILED' if status else 'passed'}", flush=True)
        write_json(out / "suite.json", report)
    final_status = "failed" if failures else "complete"
    final_elapsed = time.perf_counter() - suite_start
    report["status"] = final_status
    report["elapsed_seconds"] = final_elapsed
    write_json(out / "suite.json", report)
    finish_run(out, status=final_status, elapsed_seconds=final_elapsed)
    print(out, flush=True)
    if skipped:
        print("Skipped downloadable projects: " + ", ".join(skipped))
    return int(failures > 0)
