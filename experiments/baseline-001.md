# Experiment BASELINE-001

## Hypothesis
Modular analizlər real kiçik dataset-lərdə icra oluna və input/method/output əlaqəsini saxlaya bilər. Elmi istiqamətlər exploratory-dir.
## Dataset
PhiX NC_001422.1, pasilla 1.40.0, GIAB HG001 prefix, WDBC, UniProt P01308, PDB 1CRN. Hash-lar datasets/reference-manifest.json və run.json-da.
## Preprocessing
DNA IUPAC validation; VCF PASS/QUAL>=20; RNA total count>=10 və sequencing-type covariate; ML fold-local imputation/scaling.
## Method
NW/SW, VCF descriptive stats, PyDESeq2 NB GLM və classical ML CV.
## Parameters
DNA alignment 2/-1/-2; RNA ~type+condition, alpha .05; ML seed 42, test .25, CV 5, bootstrap 1000.
## Results
RNA 1113 FDR discoveries; WDBC AUROC 0.996226; VCF 1003 ALT alleles. Ətraflı nəticə və scope: results/README.md.
## Metrics
İcra edilmiş nəticələr results/example-runs/*/summary.json. Model fit metric klinik validation deyil.
## Observations
VCF record/ALT sayları fərqlidir; RNA library type kovariatı var; ML morphology cohort-dur.
## Errors
Python layihələri uğurla tamamlandı. Notebook runtime Windows event-loop/transport xəbərdarlığı verdi; execution error olmadı. Raw BWA/STAR workflow-ları Linux/Docker runtime olmadığı üçün icra edilmədi. Firecrawl rate limit olduqda qalan mənbələr sonrakı sorğuda alındı.
## Interpretation
Pipeline-lar təkrar icra olunan baseline yaradır; original papers benchmark-ları reproduce edilməyib. Məhdudiyyətlər results/README.md-də.
## Next Experiment
RNA design ablation, independent ML cohort və raw variant truth-region benchmark.
