# ADV-006 — Single-cell RNA-seq Analysis

**Status:** planlaşdırılır, icra edilməyib.

## Hypothesis
Treatment effect donor səviyyəsində təkrarlanırmı? Null və alternativ hipotez data audit-dən sonra preregister ediləcək.
## Dataset
GEO/10x donor-annotated counts. Accession/release və icazə hələ final deyil.
## Preprocessing
Biological unit, missingness, duplicate IDs və technical covariates audit. Pipeline: cell QC → doublets → annotation → donor pseudobulk → DE.
## Method
Scanpy, Seurat, PyDESeq2. Baseline və ən azı bir ablation.
## Parameters
Seed 42 başlanğıc təklifi; split və tuning grid əvvəlcədən yazılacaq.
## Results
İcra edilməyib; nəticə yoxdur.
## Metrics
Plan: Donor-level FDR, cell-type preservation.
## Observations
Hələ yoxdur.
## Errors
Hələ icra edilməyib; failure qeydi yoxdur.
## Interpretation
Nəticə əldə edilmədiyi üçün biological conclusion yoxdur.
## Next Experiment
Dataset access/QC tamamla, frozen evaluation plan qur. Genişlənmə: Spatial transcriptomics.
