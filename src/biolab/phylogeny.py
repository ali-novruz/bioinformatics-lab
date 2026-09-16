"""Complete-case p-distance neighbor joining and unrooted split bootstrap."""
from collections import Counter
import numpy as np
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor


def alignment_matrix(records):
    names=[r.id for r in records]
    sequences=[str(r.seq).upper() for r in records]
    if len(names)<4 or len(set(names))!=len(names):
        raise ValueError('At least four uniquely named sequences required')
    if len({len(s) for s in sequences})!=1:
        raise ValueError('Aligned sequences must have equal length')
    matrix=np.array([list(s) for s in sequences])
    usable=np.isin(matrix,list('ACGT')).all(axis=0)
    if not usable.any():raise ValueError('No complete ACGT alignment columns')
    return names,matrix[:,usable],usable


def nj_tree(names,matrix):
    distances=np.mean(matrix[:,None,:]!=matrix[None,:,:],axis=2)
    lower=[distances[i,:i+1].tolist() for i in range(len(names))]
    return DistanceTreeConstructor().nj(DistanceMatrix(names,lower)),distances


def canonical_split(side,all_names):
    side=frozenset(side); other=frozenset(all_names)-side
    if min(len(side),len(other))<2:return None
    a,b=tuple(sorted(side)),tuple(sorted(other))
    return min(a,b,key=lambda x:(len(x),x))


def tree_splits(tree):
    names={leaf.name for leaf in tree.get_terminals()}
    return {split for clade in tree.get_nonterminals() if (split:=canonical_split([x.name for x in clade.get_terminals()],names)) is not None}


def bootstrap_tree(names,matrix,repeats=200,seed=42):
    if repeats<1:raise ValueError('Positive bootstrap count required')
    tree,distances=nj_tree(names,matrix)
    rng=np.random.default_rng(seed);support=Counter()
    for _ in range(repeats):
        sampled=matrix[:,rng.integers(0,matrix.shape[1],matrix.shape[1])]
        replicate,_=nj_tree(names,sampled)
        support.update(tree_splits(replicate))
    all_names=set(names)
    for clade in tree.get_nonterminals():
        split=canonical_split([x.name for x in clade.get_terminals()],all_names)
        if split is not None:clade.confidence=100*support[split]/repeats
    tree.rooted=False
    return tree,distances,{';'.join(k):100*support[k]/repeats for k in sorted(tree_splits(tree))}
