"""One-sided over-representation analysis with an explicit measured universe."""
import pandas as pd
from scipy.stats import hypergeom
from .statistics import benjamini_hochberg


def over_representation(foreground, universe, gene_sets, min_size=2):
    universe, foreground = set(universe), set(foreground)
    if not universe or not foreground <= universe:
        raise ValueError('A nonempty universe containing all selected genes is required')
    if min_size < 1:
        raise ValueError('min_size must be positive')
    rows=[]
    for term, members in sorted(gene_sets.items()):
        members=set(members) & universe
        if len(members)<min_size or len(members)==len(universe):
            continue
        overlap=foreground & members
        expected=len(foreground)*len(members)/len(universe)
        rows.append({'term':term,'universe_size':len(universe),'selected_size':len(foreground),
                     'term_size':len(members),'overlap':len(overlap),'expected_overlap':expected,
                     'fold_enrichment':len(overlap)/expected if expected else None,
                     'pvalue':float(hypergeom.sf(len(overlap)-1,len(universe),len(members),len(foreground))),
                     'overlap_genes':';'.join(str(g) for g in sorted(overlap,key=str))})
    columns=['term','universe_size','selected_size','term_size','overlap','expected_overlap','fold_enrichment','pvalue','overlap_genes']
    frame=pd.DataFrame(rows,columns=columns)
    frame['padj']=benjamini_hochberg(frame.pvalue)
    return frame.sort_values(['padj','pvalue','term']).reset_index(drop=True)
