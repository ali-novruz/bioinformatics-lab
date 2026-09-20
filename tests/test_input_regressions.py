import sqlite3

import pytest

from biolab.io import read_vcf
from biolab.provenance import verify_sources
from biolab.study_database import initialize

BASE = "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO"
RECORD = "1\t1\t.\tA\tG\t30\tPASS\t."


@pytest.mark.parametrize(
    "header,tail",
    [
        ("FORMAT\ts\ts", "GT\t0/1\t1/1"),
        ("BROKEN\ts", "GT\t0/1"),
        ("FORMAT", "GT"),
        ("FORMAT\ts", "GT:GT\t0/1:0/1"),
        ("FORMAT\ts", "GT\t0/1:30"),
        ("FORMAT\ts", "DP:GT\t30:0/1"),
    ],
)
def test_malformed_vcf_sample_layout_is_rejected(tmp_path, header, tail):
    path = tmp_path / "invalid.vcf"
    path.write_text(BASE + "\t" + header + "\n" + RECORD + "\t" + tail + "\n")
    with pytest.raises(ValueError):
        list(read_vcf(path))


def test_omitted_trailing_format_value_is_missing(tmp_path):
    path = tmp_path / "valid.vcf"
    path.write_text(BASE + "\tFORMAT\ts\n" + RECORD + "\tGT:DP\t0/1\n")
    assert list(read_vcf(path))[0]["samples"]["s"] == {"GT": "0/1", "DP": "."}


@pytest.mark.parametrize("identifier", [None, "", "   "])
def test_sql_requires_nonempty_sample_identifiers(identifier):
    with sqlite3.connect(":memory:") as con:
        initialize(con)
        with pytest.raises(sqlite3.IntegrityError):
            con.execute(
                "INSERT INTO sample VALUES (?, ?, ?)", (identifier, "treated", 1)
            )


def test_sql_replicate_is_integer():
    with sqlite3.connect(":memory:") as con:
        initialize(con)
        with pytest.raises(sqlite3.IntegrityError):
            con.execute("INSERT INTO sample VALUES ('s','treated',1.5)")


def test_missing_historical_source_is_not_silently_accepted(tmp_path):
    with pytest.raises(ValueError, match="Unverifiable"):
        verify_sources(tmp_path, {"source_files_sha256": {"src/fake.py": "0" * 64}})
