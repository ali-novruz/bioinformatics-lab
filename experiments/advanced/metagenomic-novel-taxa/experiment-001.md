# ADV-009 — Metagenomic Novel Taxa

**Status:** planlaşdırılır, icra edilməyib.

## Hypothesis
Database-də olmayan taxa necə aşkar edilir? Null və alternativ hipotez data audit-dən sonra preregister ediləcək.
## Dataset
ENA mock communities, dated reference DB. Accession/release və icazə hələ final deyil.
## Preprocessing
Biological unit, missingness, duplicate IDs və technical covariates audit. Pipeline: read QC → classify → confidence sweep → unknown detection.
## Method
Kraken2, Bracken. Baseline və ən azı bir ablation.
## Parameters
Seed 42 başlanğıc təklifi; split və tuning grid əvvəlcədən yazılacaq.
## Results
İcra edilməyib; nəticə yoxdur.
## Metrics
Plan: Species precision/recall, abundance error, contamination controls.
## Observations
Hələ yoxdur.
## Errors
Hələ icra edilməyib; failure qeydi yoxdur.
## Interpretation
Nəticə əldə edilmədiyi üçün biological conclusion yoxdur.
## Next Experiment
Dataset access/QC tamamla, frozen evaluation plan qur. Genişlənmə: Strain-resolved assembly.
