# ADV-002 — Disease Gene Discovery

**Status:** planlaşdırılır, icra edilməyib.

## Hypothesis
Cross-cohort expression signal təkrarlanırmı? Null və alternativ hipotez data audit-dən sonra preregister ediləcək.
## Dataset
GEO studies + GTEx tissue context. Accession/release və icazə hələ final deyil.
## Preprocessing
Biological unit, missingness, duplicate IDs və technical covariates audit. Pipeline: cohort QC → within-study effects → meta-analysis → validation.
## Method
PyDESeq2, meta-analysis. Baseline və ən azı bir ablation.
## Parameters
Seed 42 başlanğıc təklifi; split və tuning grid əvvəlcədən yazılacaq.
## Results
İcra edilməyib; nəticə yoxdur.
## Metrics
Plan: Direction consistency, heterogeneity və external replication.
## Observations
Hələ yoxdur.
## Errors
Hələ icra edilməyib; failure qeydi yoxdur.
## Interpretation
Nəticə əldə edilmədiyi üçün biological conclusion yoxdur.
## Next Experiment
Dataset access/QC tamamla, frozen evaluation plan qur. Genişlənmə: Perturbation prioritization.
