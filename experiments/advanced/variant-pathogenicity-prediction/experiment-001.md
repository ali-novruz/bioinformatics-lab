# ADV-003 — Variant Pathogenicity Prediction

**Status:** planlaşdırılır, icra edilməyib.

## Hypothesis
Performance temporal holdout-da saxlanırmı? Null və alternativ hipotez data audit-dən sonra preregister ediləcək.
## Dataset
ClinVar dated releases + annotation. Accession/release və icazə hələ final deyil.
## Preprocessing
Biological unit, missingness, duplicate IDs və technical covariates audit. Pipeline: label curation → gene/time split → features → model.
## Method
scikit-learn, VEP. Baseline və ən azı bir ablation.
## Parameters
Seed 42 başlanğıc təklifi; split və tuning grid əvvəlcədən yazılacaq.
## Results
İcra edilməyib; nəticə yoxdur.
## Metrics
Plan: PR-AUC, calibration, review-status stratification.
## Observations
Hələ yoxdur.
## Errors
Hələ icra edilməyib; failure qeydi yoxdur.
## Interpretation
Nəticə əldə edilmədiyi üçün biological conclusion yoxdur.
## Next Experiment
Dataset access/QC tamamla, frozen evaluation plan qur. Genişlənmə: Functional assay validation.
