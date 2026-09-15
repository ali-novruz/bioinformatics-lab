# ADV-010 — Microbiome Association Study

**Status:** planlaşdırılır, icra edilməyib.

## Hypothesis
Cohort və antibiotic kovariatından sonra signal qalırmı? Null və alternativ hipotez data audit-dən sonra preregister ediləcək.
## Dataset
Public curated microbiome study + metadata. Accession/release və icazə hələ final deyil.
## Preprocessing
Biological unit, missingness, duplicate IDs və technical covariates audit. Pipeline: QC → taxa table → prevalence → compositional model → validation.
## Method
QIIME2, compositional statistics. Baseline və ən azı bir ablation.
## Parameters
Seed 42 başlanğıc təklifi; split və tuning grid əvvəlcədən yazılacaq.
## Results
İcra edilməyib; nəticə yoxdur.
## Metrics
Plan: Effect CI, FDR, leave-study-out performance.
## Observations
Hələ yoxdur.
## Errors
Hələ icra edilməyib; failure qeydi yoxdur.
## Interpretation
Nəticə əldə edilmədiyi üçün biological conclusion yoxdur.
## Next Experiment
Dataset access/QC tamamla, frozen evaluation plan qur. Genişlənmə: Longitudinal perturbation study.
