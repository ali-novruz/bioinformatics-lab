import numpy as np
import pytest
from biolab.statistics import bootstrap_auc
from biolab.ml import disease_classification

def test_heldout_split_and_report_contract():
    summary,cv,pred,split=disease_classification(seed=42)
    train=set(split.loc[split.split=='train','sample_index'])
    test=set(split.loc[split.split=='test','sample_index'])
    assert not train&test and len(train|test)==569
    assert set(pred.sample_index)==test
    assert summary['selected_model']==cv.sort_values(['roc_auc','model'],ascending=[False,True]).iloc[0]['model']
    assert len(pred)==summary['test_samples']==143
    assert np.asarray(summary['confusion_matrix']).sum()==143
    assert pred.probability.between(0,1).all()
    assert len(summary['dataset_canonical_csv_sha256'])==64

def test_bootstrap_binary_guard_and_perfect_ranking():
    result=bootstrap_auc([0,0,1,1],[.1,.2,.8,.9],repeats=50)
    assert result['low']==result['high']==1
    with pytest.raises(ValueError):bootstrap_auc([1,1],[.1,.2])
