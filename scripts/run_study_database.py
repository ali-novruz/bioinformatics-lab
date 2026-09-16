"""Build and query a real RNA-count SQLite catalog inspired by the UNEC DB course."""
from pathlib import Path
import sqlite3
import pandas as pd
from biolab.reporting import new_run, write_json
from biolab.study_database import build_catalog

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'results/raw-examples/rna-model'


if __name__ == '__main__':
    inputs = [INPUT / 'counts.tsv', INPUT / 'metadata.csv']
    out = new_run(ROOT, 'study-database', inputs, {'engine': 'SQLite', 'join': 'sample_id and gene_id'})
    summary = build_catalog(out / 'laboratory.sqlite', *inputs)
    with sqlite3.connect(out / 'laboratory.sqlite') as connection:
        query = """SELECT s.sample_id, s.condition, sum(c.count) AS assigned_fragments
                   FROM sample s JOIN gene_count c USING(sample_id)
                   GROUP BY s.sample_id, s.condition ORDER BY s.sample_id"""
        library = pd.read_sql_query(query, connection)
        library.to_csv(out / 'library_sizes.csv', index=False)
        assert int(library.assigned_fragments.sum()) == int(pd.read_csv(inputs[0], sep='\t', index_col=0).to_numpy().sum())
        (out / 'queries.sql').write_text(query + ';\n', encoding='utf-8')
    write_json(out / 'summary.json', summary)
    print(out)
    print(summary)
