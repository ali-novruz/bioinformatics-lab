"""A small relational laboratory catalog built from real example RNA counts."""
import csv
import hashlib
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE sample (
 sample_id TEXT NOT NULL PRIMARY KEY CHECK(length(trim(sample_id)) > 0),
 condition TEXT NOT NULL CHECK(condition IN ('treated','untreated')),
 biological_replicate INTEGER NOT NULL CHECK(typeof(biological_replicate)='integer' AND biological_replicate > 0)
);
CREATE TABLE gene (gene_id TEXT NOT NULL PRIMARY KEY CHECK(length(trim(gene_id)) > 0));
CREATE TABLE gene_count (
 sample_id TEXT NOT NULL REFERENCES sample(sample_id),
 gene_id TEXT NOT NULL REFERENCES gene(gene_id),
 count INTEGER NOT NULL CHECK(typeof(count)='integer' AND count >= 0),
 PRIMARY KEY(sample_id, gene_id)
);
CREATE TABLE source_file (
 name TEXT PRIMARY KEY,
 sha256 TEXT NOT NULL CHECK(length(sha256)=64)
);
"""


def initialize(connection):
    connection.execute('PRAGMA foreign_keys=ON')
    connection.executescript(SCHEMA)


def build_catalog(destination, counts_path, metadata_path):
    destination = Path(destination)
    if destination.exists():
        raise FileExistsError('Choose a new database path')
    connection = sqlite3.connect(destination)
    try:
        initialize(connection)
        with connection:
            with open(metadata_path, encoding='utf-8', newline='') as handle:
                for row in csv.DictReader(handle):
                    connection.execute('INSERT INTO sample VALUES (?,?,?)',
                                       (row['sample_id'], row['condition'], int(row['biological_replicate'])))
            with open(counts_path, encoding='utf-8', newline='') as handle:
                reader = csv.DictReader(handle, delimiter='\t')
                samples = reader.fieldnames[1:]
                expected = {row[0] for row in connection.execute('SELECT sample_id FROM sample')}
                if set(samples) != expected or len(samples) != len(set(samples)):
                    raise ValueError('Count and metadata sample IDs differ')
                for row in reader:
                    gene = row[reader.fieldnames[0]]
                    connection.execute('INSERT INTO gene VALUES (?)', (gene,))
                    for sample in samples:
                        connection.execute('INSERT INTO gene_count VALUES (?,?,?)',
                                           (sample, gene, int(row[sample])))
            for path in [Path(counts_path), Path(metadata_path)]:
                connection.execute('INSERT INTO source_file VALUES (?,?)',
                                   (path.name, hashlib.sha256(path.read_bytes()).hexdigest()))
        return {
            'samples': connection.execute('SELECT count(*) FROM sample').fetchone()[0],
            'genes': connection.execute('SELECT count(*) FROM gene').fetchone()[0],
            'count_records': connection.execute('SELECT count(*) FROM gene_count').fetchone()[0],
            'integrity_check': connection.execute('PRAGMA integrity_check').fetchone()[0],
            'foreign_key_violations': connection.execute('PRAGMA foreign_key_check').fetchall(),
        }
    finally:
        connection.close()
