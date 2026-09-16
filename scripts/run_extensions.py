"""Execute three offline projects from real, versioned example inputs."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Bio import AlignIO,Phylo,SeqIO
from biolab.enrichment import over_representation
from biolab.phylogeny import alignment_matrix,bootstrap_tree
from biolab.orfs import find_orfs
from biolab.reporting import new_run,write_json

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'datasets/examples'


def enrichment():
    source=ROOT/'results/raw-examples/rna-model/differential_expression.csv'
    annotations=DATA/'enrichment/sgd_go_slim_chrI.tsv'
    out=new_run(ROOT,'go-enrichment',[source,annotations],{'foreground':'padj < 0.05','universe':'finite padj genes','test':'hypergeometric upper tail','correction':'BH across all eligible GO slim BP terms','min_term_size':2})
    de=pd.read_csv(source).set_index('gene_id')
    universe=set(de.index[np.isfinite(de.padj)])
    foreground=set(de.index[de.padj<.05])
    ann=pd.read_csv(annotations,sep='\t')
    sets=ann.groupby('go_id')['gene_id'].agg(set).to_dict()
    table=over_representation(foreground,universe,sets)
    names=ann.drop_duplicates('go_id').set_index('go_id')['term_name']
    table.insert(1,'term_name',table.term.map(names))
    table.to_csv(out/'enrichment.csv',index=False)
    pd.Series(sorted(universe),name='gene_id').to_csv(out/'universe.csv',index=False)
    pd.Series(sorted(foreground),name='gene_id').to_csv(out/'selected_genes.csv',index=False)
    annotated=set(ann.gene_id)&universe
    summary={'real_data':True,'universe_genes':len(universe),'foreground_genes':len(foreground),
             'annotated_universe_genes':len(annotated),'unannotated_universe_genes':len(universe-annotated),
             'tested_terms':len(table),'significant_terms_fdr_005':int((table.padj<.05).sum()),
             'scope':'GO-slim biological-process over-representation; chrI subsample; no pathway activation inference',
             'limitations':'One DE gene; low power. Unannotated measured genes remain in the universe. Overlapping GO terms induce dependence; exploratory BH analysis.'}
    write_json(out/'summary.json',summary)
    top=table.head(12).iloc[::-1]
    fig,ax=plt.subplots(figsize=(9,5));ax.barh(top.term_name,-np.log10(top.pvalue.clip(lower=1e-300)),color='#157f83')
    ax.set(xlabel='-log10 raw enrichment p-value',title=f'GO-slim: {len(foreground)} selected gene; {summary["significant_terms_fdr_005"]} FDR discoveries')
    fig.tight_layout();fig.savefig(out/'enrichment.png',dpi=150);plt.close(fig)
    return out


def phylogeny():
    source=DATA/'phylogeny/opuntia.aln'
    out=new_run(ROOT,'phylogeny',[source],{'distance':'uncorrected p-distance','gaps':'complete deletion across all taxa','tree':'neighbor joining, unrooted','bootstrap':200,'seed':42})
    alignment=AlignIO.read(source,'clustal')
    for record in alignment:record.id=record.id.split('|')[3]
    names,matrix,mask=alignment_matrix(alignment)
    tree,distances,support=bootstrap_tree(names,matrix)
    Phylo.write(tree,out/'tree.nwk','newick')
    pd.DataFrame(distances,index=names,columns=names).to_csv(out/'distances.csv')
    pd.DataFrame({'alignment_column1':np.arange(1,len(mask)+1),'retained':mask}).to_csv(out/'alignment_columns.csv',index=False)
    write_json(out/'bootstrap_splits.json',support)
    negative=sum(c.branch_length is not None and c.branch_length<0 for c in tree.find_clades())
    summary={'real_sequence_fragments':True,'taxa':len(names),'alignment_columns':len(mask),'complete_columns':int(mask.sum()),
             'removed_columns':int((~mask).sum()),'variable_complete_columns':int(np.any(matrix!=matrix[0],axis=0).sum()),
             'bootstrap_replicates':200,'negative_branch_lengths':negative,
             'scope':'Seven short Opuntia fragments from Biopython tutorial; not a full species phylogeny; no ancestral root inferred',
             'limitations':'Short alignment, limited signal, site independence assumed in bootstrap. NJ can yield negative lengths; raw lengths are preserved, not silently clipped.'}
    write_json(out/'summary.json',summary)
    fig,ax=plt.subplots(figsize=(9,5));Phylo.draw(tree,axes=ax,do_show=False,show_confidence=True,label_func=lambda clade: clade.name if clade.is_terminal() else None)
    ax.set(title='Opuntia fragments: unrooted NJ, 200 site bootstraps',xlabel='p-distance branch length (display root is arbitrary)')
    fig.tight_layout();fig.savefig(out/'tree.png',dpi=150);plt.close(fig)
    return out


def orfs():
    source=DATA/'orfs/NC_001422.1.fasta'
    out=new_run(ROOT,'orf-discovery',[source],{'min_amino_acids':30,'circular':True,'start':'ATG','stops':['TAA','TAG','TGA'],'translation_table':1})
    record=SeqIO.read(source,'fasta')
    found=find_orfs(str(record.seq),min_aa=30,circular=True)
    rows=[]
    with (out/'proteins.fasta').open('w',encoding='utf-8',newline='\n') as handle:
        for i,row in enumerate(found,1):
            name=f'orf_{i:03}'
            handle.write(f'>{name} strand={row["strand"]} candidate_only\n{row["protein"]}\n')
            rows.append({'orf_id':name,**{k:v for k,v in row.items() if k!='protein'},'segments0':json.dumps(row['segments0'])})
    pd.DataFrame(rows).to_csv(out/'orfs.csv',index=False)
    write_json(out/'orfs.json',found)
    write_json(out/'summary.json',{'accession':'NC_001422.1','length_nt':len(record),'candidate_orfs':len(found),
                                 'plus_strand':sum(r['strand']=='+' for r in found),'minus_strand':sum(r['strand']=='-' for r in found),
                                 'origin_spanning':sum(r['wraps_origin'] for r in found),'longest_aa':max((r['length_aa'] for r in found),default=0),
                                 'scope':'Real circular PhiX174 genome; canonical ORF candidates, not confirmed gene annotations',
                                 'limitations':'ATG starts only; no alternative starts, coding potential, splicing or experimental expression evidence. Nested candidates retained.'})
    fig,ax=plt.subplots(figsize=(9,4))
    for i,row in enumerate(found):
        for start,end in row['segments0']:
            ax.plot([start,end],[i,i],lw=3,color='#157f83' if row['strand']=='+' else '#c46a45')
    ax.set(xlabel='Reference position (0-based)',ylabel='ORF candidate',title='PhiX174 circular ORFs: teal + / orange -')
    fig.tight_layout();fig.savefig(out/'orfs.png',dpi=150);plt.close(fig)
    return out


RUNNERS={'enrichment':enrichment,'phylogeny':phylogeny,'orfs':orfs}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--project',choices=[*RUNNERS,'all'],required=True)
    args=parser.parse_args()
    for name in RUNNERS if args.project=='all' else [args.project]:
        out=RUNNERS[name]();print(out);print((out/'summary.json').read_text(encoding='utf-8'))
