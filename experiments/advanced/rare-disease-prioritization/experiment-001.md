# ADV-008 — Rare Disease Prioritization

**Status:** planlaşdırılır, icra edilməyib.

## Hypothesis
Phenotype məlumatı variant sırasını yaxşılaşdırırmı? Null və alternativ hipotez data audit-dən sonra preregister ediləcək.
## Dataset
ClinVar public examples + HPO; controlled patient data yox. Accession/release və icazə hələ final deyil.
## Preprocessing
Biological unit, missingness, duplicate IDs və technical covariates audit. Pipeline: quality → inheritance → phenotype match → evidence ranking.
## Method
VEP, HPO ontology. Baseline və ən azı bir ablation.
## Parameters
Seed 42 başlanğıc təklifi; split və tuning grid əvvəlcədən yazılacaq.
## Results
İcra edilməyib; nəticə yoxdur.
## Metrics
Plan: Recall@k, gene holdout, evidence provenance.
## Observations
Hələ yoxdur.
## Errors
Hələ icra edilməyib; failure qeydi yoxdur.
## Interpretation
Nəticə əldə edilmədiyi üçün biological conclusion yoxdur.
## Next Experiment
Dataset access/QC tamamla, frozen evaluation plan qur. Genişlənmə: Trio analysis və long-read SV.
