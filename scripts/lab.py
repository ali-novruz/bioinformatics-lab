"""Compatibility wrapper for the installed biolab project launcher."""

from pathlib import Path

from biolab.cli import main as cli_main

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    raise SystemExit(cli_main(root=ROOT))


if __name__ == "__main__":
    main()
