import json
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from biolab.cli import main
from biolab.study_database import build_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_installed_cli_lists_all_projects() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "biolab.cli", "--root", str(ROOT), "list"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert len(result.stdout.splitlines()) == 13
    assert "alignment" in result.stdout


def test_cli_direct_methods_and_errors(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    fasta = tmp_path / "input.fa"
    fasta.write_text(">sample\nACGT\n", encoding="utf-8")
    assert main(["dna", str(fasta)]) == 0
    assert json.loads(capsys.readouterr().out)["sample"]["length"] == 4
    assert main(["align", "ACGT", "AGT", "--backend", "numpy"]) == 0
    assert json.loads(capsys.readouterr().out)["score"] == 4
    with pytest.raises(SystemExit) as error:
        main(["--root", str(ROOT), "run", "missing-project"])
    assert error.value.code == 2


def test_study_catalog_builds_relations_and_rejects_overwrite(tmp_path: Path) -> None:
    metadata = tmp_path / "metadata.csv"
    counts = tmp_path / "counts.tsv"
    database = tmp_path / "lab.sqlite"
    metadata.write_text(
        "sample_id,condition,biological_replicate\nA,treated,1\nB,untreated,1\n",
        encoding="utf-8",
    )
    counts.write_text("gene\tA\tB\ng1\t4\t7\ng2\t0\t2\n", encoding="utf-8")
    summary = build_catalog(database, counts, metadata)
    assert summary == {
        "samples": 2,
        "genes": 2,
        "count_records": 4,
        "integrity_check": "ok",
        "foreign_key_violations": [],
    }
    with sqlite3.connect(database) as connection:
        assert (
            connection.execute("SELECT sum(count) FROM gene_count").fetchone()[0] == 13
        )
    with pytest.raises(FileExistsError):
        build_catalog(database, counts, metadata)
