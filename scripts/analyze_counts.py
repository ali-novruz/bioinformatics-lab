"""Analyze user-supplied bulk RNA counts with the same tested model engine."""
import argparse
from pathlib import Path
import pandas as pd
from biolab.transcriptomics import differential_expression
from biolab.reporting import new_run,write_json
from run_projects import plot_expression

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--counts',required=True,help='genes x samples TSV');p.add_argument('--metadata',required=True,help='CSV indexed by sample ID');p.add_argument('--design',default='~ type + condition')
    p.add_argument('--dataset-name',default='User-supplied RNA-seq')
    a=p.parse_args();root=Path(__file__).resolve().parents[1]
    counts=pd.read_csv(a.counts,sep='\t',index_col=0).T;meta=pd.read_csv(a.metadata,index_col=0)
    out=new_run(root,'custom-rnaseq',[a.counts,a.metadata],parameters={'design':a.design,'dataset':a.dataset_name,'counts':str(Path(a.counts).resolve()),'metadata':str(Path(a.metadata).resolve())})
    import hashlib
    write_json(out/'input_hashes.json',{str(Path(p).resolve()):hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in [a.counts,a.metadata]})
    res,norm,summary=differential_expression(counts,meta,a.design)
    res.to_csv(out/'differential_expression.csv');norm.to_csv(out/'normalized_counts.csv');write_json(out/'summary.json',summary)
    plot_expression(res,norm,meta,out,dataset=a.dataset_name,design=a.design);print(out)
