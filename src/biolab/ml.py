"""Disease classification baseline with fold-local preprocessing."""
import numpy as np
import hashlib
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split,StratifiedKFold,cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import roc_auc_score,average_precision_score,balanced_accuracy_score,confusion_matrix,brier_score_loss
from .statistics import bootstrap_auc

def disease_classification(seed=42):
    data=load_breast_cancer(as_frame=True)
    X=data.data
    y=(data.target==0).astype(int)  # positive class = malignant
    train,test=train_test_split(np.arange(len(X)),test_size=.25,stratify=y,random_state=seed)
    models={
      'dummy':make_pipeline(SimpleImputer(),DummyClassifier(strategy='prior')),
      'logistic':make_pipeline(SimpleImputer(),StandardScaler(),LogisticRegression(C=1,max_iter=5000,random_state=seed)),
      'random_forest':make_pipeline(SimpleImputer(),RandomForestClassifier(n_estimators=300,min_samples_leaf=2,random_state=seed,n_jobs=1))}
    cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=seed)
    rows=[]
    for name,model in models.items():
        s=cross_validate(model,X.iloc[train],y.iloc[train],cv=cv,scoring={'roc_auc':'roc_auc','pr_auc':'average_precision','balanced_accuracy':'balanced_accuracy'},n_jobs=1)
        rows.append({'model':name,**{key:float(s['test_'+key].mean()) for key in ['roc_auc','pr_auc','balanced_accuracy']},'auc_fold_sd':float(s['test_roc_auc'].std(ddof=1))})
    cv_table=pd.DataFrame(rows).sort_values(['roc_auc','model'],ascending=[False,True])
    best=cv_table.iloc[0]['model'];model=models[best]
    model.fit(X.iloc[train],y.iloc[train])
    p=model.predict_proba(X.iloc[test])[:,1]; pred=(p>=.5).astype(int)
    truth=y.iloc[test].to_numpy()
    tn,fp,fn,tp=confusion_matrix(truth,pred,labels=[0,1]).ravel()
    summary={'dataset':'Wisconsin Diagnostic Breast Cancer, UCI DOI 10.24432/C5DW2B','features':'30 nuclear morphology features; NOT gene expression','samples':len(X),'train_samples':len(train),'test_samples':len(test),'positive_class':'malignant','seed':seed,'selected_using':'training-only 5-fold mean AUROC','selected_model':best,'test_roc_auc':float(roc_auc_score(truth,p)),'test_pr_auc':float(average_precision_score(truth,p)),'test_balanced_accuracy':float(balanced_accuracy_score(truth,pred)),'test_brier':float(brier_score_loss(truth,p)),'sensitivity':float(tp/(tp+fn)),'specificity':float(tn/(tn+fp)),'confusion_matrix':[[int(tn),int(fp)],[int(fn),int(tp)]],'test_auc_bootstrap_95':bootstrap_auc(truth,p,seed=seed)}
    canonical=X.assign(malignant=y).to_csv(index=False,float_format='%.12g',lineterminator='\n').encode()
    summary['dataset_canonical_csv_sha256']=hashlib.sha256(canonical).hexdigest()
    predictions=pd.DataFrame({'sample_index':test,'malignant':truth,'probability':p,'prediction':pred})
    split=pd.DataFrame({'sample_index':np.arange(len(X)),'split':['test' if i in set(test) else 'train' for i in range(len(X))]})
    return summary,cv_table,predictions,split
