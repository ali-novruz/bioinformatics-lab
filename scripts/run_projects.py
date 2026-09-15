"""Run one or all five projects from the repository root."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import RocCurveDisplay,ConfusionMatrixDisplay
from biolab.io import read_fasta
from biolab.sequence import sequence_summary,align
from biolab.genomics import analyze_vcf
from biolab.transcriptomics import load_pasilla,differential_expression
from biolab.ml import disease_classification
from biolab.reporting import new_run,write_json

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'datasets/raw'

def run_dna():
    source=RAW/'NC_001422.1.fasta'
    if not source.exists():source=ROOT/'datasets/fixtures/toy.fasta'
    out=new_run(ROOT,'dna',[source])
    records={name:sequence_summary(seq) for name,seq in read_fasta(source)}
    write_json(out/'summary.json',{'source':str(source.relative_to(ROOT)),'real_data':source.parent==RAW,'records':records})
    fig,ax=plt.subplots(figsize=(7,4))
    ax.bar(list(records),[r['gc_fraction_acgt_only'] or 0 for r in records.values()]);ax.set(ylabel='GC fraction (ACGT denominator)',ylim=(0,1),title='Sequence composition')
    fig.tight_layout();fig.savefig(out/'gc.png',dpi=150);plt.close(fig)
    return out

def run_alignment():
    from Bio.Align import PairwiseAligner
    out=new_run(ROOT,'alignment',parameters={'match':2,'mismatch':-1,'linear_gap':-2})
    result=[]
    for mode in ['global','local']:
        ours=align('ACGTTGAC','ACTTGACC',mode)
        ref=PairwiseAligner(mode=mode,match_score=2,mismatch_score=-1,open_gap_score=-2,extend_gap_score=-2)
        score=ref.score('ACGTTGAC','ACTTGACC')
        if ours.score!=score:raise AssertionError('Biopython score differs')
        result.append({**ours.to_dict(),'biopython_score':score})
    write_json(out/'summary.json',{'data':'synthetic teaching sequences','alignments':result})
    return out

def run_variants():
    source=RAW/'giab_hg001_first1000.vcf'
    if not source.exists():raise FileNotFoundError('Run fetch_data.py --dataset giab first')
    # GIAB benchmark QUAL is often 50; missing quality is kept only if explicitly requested.
    out=new_run(ROOT,'variants',[source],{'min_qual':20,'require_pass':True})
    table,summary=analyze_vcf(source)
    table.to_csv(out/'variants.csv',index=False);write_json(out/'summary.json',summary)
    fig,ax=plt.subplots(figsize=(7,4));table['type'].value_counts().plot.bar(ax=ax,color='#157f83')
    ax.set(ylabel='Retained ALT alleles',title='GIAB HG001: first 1000 records only');fig.tight_layout();fig.savefig(out/'variant_types.png',dpi=150);plt.close(fig)
    return out

def plot_expression(res,norm,meta,out):
    log=np.log1p(norm)
    coords=PCA(n_components=2,svd_solver='full').fit_transform(log)
    fig,ax=plt.subplots(figsize=(7,5))
    for group in ['untreated','treated']:
        mask=meta.loc[log.index,'condition'].eq(group)
        ax.scatter(coords[mask,0],coords[mask,1],label=group,s=65)
    for idx,name in enumerate(log.index):ax.annotate(name,(coords[idx,0],coords[idx,1]),fontsize=7)
    ax.set(xlabel='PC1',ylabel='PC2',title='Pasilla PCA: log1p normalized counts');ax.legend();fig.tight_layout();fig.savefig(out/'pca.png',dpi=150);plt.close(fig)
    selected=log.var(axis=0).nlargest(30).index
    z=log[selected].T
    z=z.sub(z.mean(axis=1),axis=0).div(z.std(axis=1).replace(0,1),axis=0)
    fig,ax=plt.subplots(figsize=(8,8));im=ax.imshow(z,aspect='auto',cmap='RdBu_r',vmin=-2,vmax=2)
    ax.set_xticks(range(len(z.columns)),z.columns,rotation=45,ha='right');ax.set_yticks(range(len(z)),z.index,fontsize=7);ax.set_title('Top 30 variable genes; row z-score');fig.colorbar(im,ax=ax);fig.tight_layout();fig.savefig(out/'heatmap.png',dpi=150);plt.close(fig)
    valid=res.dropna(subset=['padj','log2FoldChange']);sig=(valid.padj<.05)&(valid.log2FoldChange.abs()>1)
    fig,ax=plt.subplots(figsize=(7,5));ax.scatter(valid.log2FoldChange,-np.log10(valid.padj.clip(lower=1e-300)),c=np.where(sig,'#c23b4a','#75878b'),s=7,alpha=.6)
    ax.axhline(-np.log10(.05),ls='--',c='black',lw=.7);ax.set(xlabel='log2FC treated / untreated (unshrunken)',ylabel='-log10 adjusted p',title='Pasilla: type + condition');fig.tight_layout();fig.savefig(out/'volcano.png',dpi=150);plt.close(fig)
    return coords

def run_rnaseq():
    inputs=[RAW/'pasilla_gene_counts.tsv',RAW/'pasilla_sample_annotation.csv']
    out=new_run(ROOT,'rnaseq',inputs,{'design':'~ type + condition','seed':42})
    counts,metadata=load_pasilla(RAW)
    results,normalized,summary=differential_expression(counts,metadata)
    results.to_csv(out/'differential_expression.csv',index_label='gene_id');normalized.to_csv(out/'normalized_counts.csv')
    metadata.to_csv(out/'metadata.csv');write_json(out/'summary.json',summary)
    plot_expression(results,normalized,metadata,out)
    return out

def run_ml():
    out=new_run(ROOT,'ml',parameters={'seed':42,'test_fraction':.25,'cv_folds':5})
    summary,cv,pred,split=disease_classification()
    write_json(out/'summary.json',summary);cv.to_csv(out/'cv.csv',index=False);pred.to_csv(out/'predictions.csv',index=False);split.to_csv(out/'split.csv',index=False)
    fig,ax=plt.subplots();RocCurveDisplay.from_predictions(pred.malignant,pred.probability,ax=ax);ax.set_title('Held-out WDBC: malignant positive');fig.tight_layout();fig.savefig(out/'roc.png',dpi=150);plt.close(fig)
    fig,ax=plt.subplots();ConfusionMatrixDisplay.from_predictions(pred.malignant,pred.prediction,display_labels=['benign','malignant'],ax=ax);fig.tight_layout();fig.savefig(out/'confusion.png',dpi=150);plt.close(fig)
    return out

RUNNERS={'dna':run_dna,'alignment':run_alignment,'variants':run_variants,'rnaseq':run_rnaseq,'ml':run_ml}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--project',choices=[*RUNNERS,'all'],required=True);args=parser.parse_args()
    for name in RUNNERS if args.project=='all' else [args.project]:
        print('Running',name,flush=True); print(RUNNERS[name](),flush=True)
