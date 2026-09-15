"""Multiple testing and held-out AUROC uncertainty."""
import numpy as np
from sklearn.metrics import roc_auc_score

def benjamini_hochberg(pvalues):
    p=np.asarray(pvalues,dtype=float)
    if p.ndim!=1 or not np.isfinite(p).all() or ((p<0)|(p>1)).any():
        raise ValueError("Expected a finite one-dimensional array of p-values in [0,1]")
    if not len(p):return p.copy()
    order=np.argsort(p,kind='stable')
    adjusted=np.minimum.accumulate((p[order]*len(p)/np.arange(1,len(p)+1))[::-1])[::-1]
    out=np.empty_like(p);out[order]=np.minimum(adjusted,1)
    return out

def bootstrap_auc(y, probability, repeats=1000, seed=42):
    y=np.asarray(y); probability=np.asarray(probability)
    if y.ndim!=1 or y.shape!=probability.shape or len(np.unique(y))!=2 or not np.isfinite(probability).all():raise ValueError("Binary labels and finite paired probabilities required")
    if repeats<20:raise ValueError("At least 20 bootstrap replicates required")
    rng=np.random.default_rng(seed);values=[]
    for _ in range(repeats):
        idx=rng.integers(0,len(y),len(y))
        if len(np.unique(y[idx]))==2:values.append(roc_auc_score(y[idx],probability[idx]))
    if not values:raise ValueError("No valid bootstrap samples")
    lo,hi=np.quantile(values,[.025,.975])
    return {"low":float(lo),"high":float(hi),"valid_replicates":len(values),"scope":"fixed fitted model, held-out samples only"}
