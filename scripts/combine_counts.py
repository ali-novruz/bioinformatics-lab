"""Combine featureCounts single-sample outputs; never align genes by row number."""
import argparse
from pathlib import Path
import pandas as pd

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--samples',required=True,help='TSV with sample_id and counts_path');p.add_argument('--output',required=True)
    a=p.parse_args();samples=pd.read_csv(a.samples,sep='\t')
    if samples.sample_id.duplicated().any():raise ValueError('Duplicate sample IDs')
    series=[];expected=None
    for r in samples.itertuples():
        path=Path(r.counts_path)
        if not path.is_absolute():path=Path(a.samples).resolve().parent/path
        table=pd.read_csv(path,sep='\t',comment='#',index_col=0)
        if table.index.has_duplicates or len(table.columns)!=6:raise ValueError('Expected single-sample featureCounts output')
        if expected is not None and set(table.index)!=expected:raise ValueError('Gene universes differ; check annotations')
        expected=set(table.index)
        series.append(table.iloc[:,-1].rename(r.sample_id))
    if not series:raise ValueError('No samples')
    output=Path(a.output);output.parent.mkdir(parents=True,exist_ok=True)
    pd.concat(series,axis=1).to_csv(output,sep='\t',index_label='gene_id')
