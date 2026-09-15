# ADV-005 — Protein Function Prediction

**Status:** planlaşdırılır, icra edilməyib.

## Hypothesis
Embeddings homology baseline-ı keçirmi? Null və alternativ hipotez data audit-dən sonra preregister ediləcək.
## Dataset
UniProt experimentally supported GO labels. Accession/release və icazə hələ final deyil.
## Preprocessing
Biological unit, missingness, duplicate IDs və technical covariates audit. Pipeline: time/cluster split → features → multi-label prediction.
## Method
ESM embeddings, scikit-learn. Baseline və ən azı bir ablation.
## Parameters
Seed 42 başlanğıc təklifi; split və tuning grid əvvəlcədən yazılacaq.
## Results
İcra edilməyib; nəticə yoxdur.
## Metrics
Plan: Macro/micro PR-AUC, hierarchy consistency.
## Observations
Hələ yoxdur.
## Errors
Hələ icra edilməyib; failure qeydi yoxdur.
## Interpretation
Nəticə əldə edilmədiyi üçün biological conclusion yoxdur.
## Next Experiment
Dataset access/QC tamamla, frozen evaluation plan qur. Genişlənmə: Wet-lab test edilə bilən domain hipotezi.
