"""Installed command line for direct methods and all registered projects."""

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from .genomics import analyze_vcf
from .io import read_fasta
from .launcher import run_projects
from .sequence import align, sequence_summary


def find_repository(explicit: Path | None = None) -> Path:
    """Find project assets from --root, cwd, or an editable checkout."""
    candidates = (
        [explicit]
        if explicit is not None
        else [Path.cwd(), *Path.cwd().parents, Path(__file__).resolve().parents[2]]
    )
    for candidate in candidates:
        if candidate is not None and (candidate / "projects/registry.json").is_file():
            return candidate.resolve()
    raise ValueError(
        "Project assets not found. Clone the repository and use biolab --root PATH list."
    )


def main(argv: Sequence[str] | None = None, *, root: Path | None = None) -> int:
    p = argparse.ArgumentParser(description="Bioinformatics teaching and project tools")
    p.add_argument(
        "--root", type=Path, help="repository checkout containing projects and scripts"
    )
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="list all registered projects")
    run = sub.add_parser("run", help="run a registered project or all projects")
    run.add_argument("project")
    run.add_argument("--offline", action="store_true")
    dna = sub.add_parser("dna")
    dna.add_argument("fasta")
    aln = sub.add_parser("align")
    aln.add_argument("query")
    aln.add_argument("target")
    aln.add_argument("--mode", choices=["global", "local"], default="global")
    aln.add_argument("--backend", choices=["python", "numpy"], default="python")
    vcf = sub.add_parser("variants")
    vcf.add_argument("vcf")
    vcf.add_argument("--output", required=True)
    vcf.add_argument("--min-qual", type=float, default=20)
    args = p.parse_args(argv)
    try:
        if args.command in {"list", "run"}:
            return run_projects(args, find_repository(args.root or root))
        if args.command == "dna":
            out = {name: sequence_summary(seq) for name, seq in read_fasta(args.fasta)}
        elif args.command == "align":
            out = align(
                args.query, args.target, args.mode, backend=args.backend
            ).to_dict()
        else:
            table, out = analyze_vcf(args.vcf, args.min_qual)
            dest = Path(args.output)
            dest.parent.mkdir(parents=True, exist_ok=True)
            table.to_csv(dest, index=False)
        print(json.dumps(out, indent=2, ensure_ascii=False, allow_nan=False))
    except (ValueError, OSError) as exc:
        p.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
