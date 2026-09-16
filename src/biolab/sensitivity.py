"""Controls for existing analyses; no reuse of the published test cohort."""
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import balanced_accuracy_score
from .expression_ml import expression_pipeline
from .enrichment import over_representation


def singleton_enrichment(universe, gene_sets, alpha=.05, min_size=2):
    """Enumerate every size-one foreground, with the same term family and BH rule."""
    if not 0 < alpha < 1:
        raise ValueError('alpha must be between zero and one')
    universe = set(universe)
    rows = []
    for gene in sorted(universe):
        result = over_representation({gene}, universe, gene_sets, min_size=min_size)
        if result.empty:
            raise ValueError('No eligible terms')
        rows.append({'gene_id':gene, 'min_pvalue':float(result.pvalue.min()),
                     'min_padj':float(result.padj.min()),
                     'discoveries':int((result.padj < alpha).sum()), 'tested_terms':len(result)})
    if not rows:
        raise ValueError('Nonempty universe required')
    return pd.DataFrame(rows)


def nested_expression_cv(x, y, *, seed=42, outer_folds=5, inner_folds=3, grid=None):
    """Return outer-fold scores and out-of-fold predictions with full inner selection."""
    x=np.asarray(x,dtype=float);y=np.asarray(y)
    if x.ndim!=2 or y.ndim!=1 or len(x)!=len(y) or not np.isfinite(x).all():
        raise ValueError('Finite 2-D features and paired 1-D labels required')
    if len(np.unique(y))<2 or outer_folds<2 or inner_folds<2 or pd.Series(y).value_counts().min()<outer_folds:
        raise ValueError('Enough samples per class for stratified outer CV required')
    grid=grid or {'select__k':[25,100,500], 'classifier__C':[.01,.1,1.]}
    splitter=StratifiedKFold(outer_folds,shuffle=True,random_state=seed)
    rows=[];predictions=[]
    for fold,(train,test) in enumerate(splitter.split(x,y),1):
        if pd.Series(y[train]).value_counts().min()<inner_folds:
            raise ValueError('Too few training samples per class for inner CV')
        search=GridSearchCV(expression_pipeline(seed=seed),grid,
                            scoring='balanced_accuracy',n_jobs=1,error_score='raise',
                            cv=StratifiedKFold(inner_folds,shuffle=True,random_state=seed))
        search.fit(x[train],y[train])
        predicted=search.predict(x[test])
        model=search.best_estimator_
        surviving=np.flatnonzero(model.named_steps['variance'].get_support())
        selected=surviving[model.named_steps['select'].get_support()]
        rows.append({'fold':fold,'train_n':len(train),'validation_n':len(test),
                     'inner_selected_score':float(search.best_score_),
                     'balanced_accuracy':float(balanced_accuracy_score(y[test],predicted)),
                     'parameters':search.best_params_,'selected_feature_indices0':selected.tolist(),
                     'train_indices0':train.tolist(),'validation_indices0':test.tolist()})
        predictions.extend({'sample_index0':int(i),'fold':fold,'truth':int(truth),'prediction':int(pred)}
                           for i,truth,pred in zip(test,y[test],predicted))
    return rows,pd.DataFrame(predictions).sort_values('sample_index0')


def permutation_pvalue(observed, null_scores):
    null=np.asarray(null_scores,dtype=float)
    if null.ndim!=1 or not len(null) or not np.isfinite(null).all() or not np.isfinite(observed):
        raise ValueError('Finite observed score and nonempty finite null scores required')
    # Include the observed arrangement; Monte Carlo p is never reported as zero.
    return float((1+np.count_nonzero(null>=observed))/(1+len(null)))
