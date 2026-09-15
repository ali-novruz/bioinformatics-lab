"""Generate a provenance-labelled bioinformatics visualization gallery."""
from pathlib import Path
import json,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from Bio import Phylo
from io import StringIO
from biolab.io import read_fasta
from biolab.sequence import gc_content

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'visualizations/gallery'

def latest(project):
    runs=sorted((ROOT/'results/runs'/project).glob('*/summary.json'))
    if not runs:raise FileNotFoundError(f'Run {project} project first')
    return runs[-1].parent

def save(fig,name):
    fig.tight_layout();fig.savefig(OUT/name,dpi=160);plt.close(fig)

def main():
    OUT.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(42)
    _,seq=next(read_fasta(ROOT/'datasets/raw/NC_001422.1.fasta'))
    starts=list(range(0,len(seq)-199,100));vals=[gc_content(seq[s:s+200]) for s in starts]
    fig,ax=plt.subplots(figsize=(9,4));ax.plot(starts,vals,c='#157f83');ax.set(xlabel='0-based window start',ylabel='GC fraction',title='Real PhiX NC_001422.1: 200 nt windows, 100 nt step');save(fig,'sequence.png')
    variants=__import__('pandas').read_csv(latest('variants')/'variants.csv')
    fig,ax=plt.subplots(figsize=(9,3))
    for row,(kind,color) in enumerate([('SNV','#157f83'),('indel','#d9654b')]):
        ax.hlines(row,variants.pos.min(),variants.pos.max(),color='#dbe3e5',lw=3,zorder=1)
        positions=variants.loc[variants.type.eq(kind),'pos']
        ax.scatter(positions,np.full(len(positions),row),marker='|',s=50,c=color,zorder=3)
    ax.set(yticks=[0,1],yticklabels=['SNV','indel'],ylim=(-.5,1.5),xlabel='VCF 1-based position',title='GIAB HG001 genomic prefix: variants on '+str(variants.chrom.iloc[0]));save(fig,'chromosome.png')
    for src,dst in [('pca.png','pca.png'),('heatmap.png','heatmap.png'),('volcano.png','volcano.png')]:shutil.copy2(latest('rnaseq')/src,OUT/dst)
    X=StandardScaler().fit_transform(load_breast_cancer().data);y=load_breast_cancer().target
    from umap import UMAP
    for label,coords in [('tsne',TSNE(n_components=2,perplexity=30,init='pca',learning_rate='auto',random_state=42).fit_transform(X)),('umap',UMAP(n_components=2,n_neighbors=15,min_dist=.1,random_state=42,n_jobs=1).fit_transform(X))]:
        fig,ax=plt.subplots(figsize=(7,5))
        for value,name in [(0,'malignant'),(1,'benign')]:ax.scatter(coords[y==value,0],coords[y==value,1],s=10,label=name,alpha=.7)
        ax.set(title=f'WDBC exploratory {label.upper()}; all samples',xlabel='Dimension 1',ylabel='Dimension 2');ax.legend();save(fig,label+'.png')
    # Manhattan example is intentionally synthetic, independent of the real VCF.
    n=1200;chrom=np.repeat(np.arange(1,7),200);p=rng.uniform(size=n);p[[130,490,830]]=[1e-10,1e-8,1e-11]
    fig,ax=plt.subplots(figsize=(10,4));ax.scatter(np.arange(n),-np.log10(p),s=8,c=np.where(chrom%2,'#157f83','#869da4'));ax.axhline(-np.log10(.05/n),ls='--',c='#be465a');ax.set(xticks=np.arange(100,n,200),xticklabels=np.arange(1,7),xlabel='Synthetic chromosome',ylabel='-log10 p',title='SIMULATED Manhattan plot; no real GWAS association');save(fig,'manhattan.png')
    tree=Phylo.read(StringIO('((A:0.1,B:0.2):0.1,(C:0.15,D:0.2):0.15);'),'newick')
    fig,ax=plt.subplots(figsize=(8,4));Phylo.draw(tree,axes=ax,do_show=False);ax.set_title('ILLUSTRATIVE Newick tree; not inferred from real species');save(fig,'phylogenetic_tree.png')
    for name in ['contact_map.png','protein_structure.png']:shutil.copy2(latest('proteins')/name,OUT/name)
    import networkx as nx
    graph=nx.DiGraph([('Signal','Receptor'),('Receptor','Kinase'),('Kinase','TF'),('TF','RNA'),('RNA','Protein')])
    fig,ax=plt.subplots(figsize=(10,3));nx.draw_networkx(graph,pos={n:(i,0) for i,n in enumerate(graph)},ax=ax,node_color='#bce1d9',node_size=2000,arrows=True,font_size=9);ax.set_title('CONCEPTUAL pathway; not a curated Reactome network');ax.axis('off');save(fig,'pathway.png')
    meta={'seed':42,'exploratory_embeddings':'All WDBC samples standardized together for visualization ONLY; never fed back into classifier evaluation','sources':{'sequence':'NC_001422.1','chromosome':'GIAB first 1000 VCF records; not whole chromosome','pca_heatmap_volcano':'real pasilla PyDESeq2 run','umap_tsne':'real WDBC morphology','manhattan':'synthetic','phylogenetic_tree':'illustrative Newick','protein_structure_contact':'real PDB 1CRN','pathway':'conceptual synthetic network'}}
    (OUT/'provenance.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(OUT)

if __name__=='__main__':main()
