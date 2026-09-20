# ADV-003 — Variant Pathogenicity Prediction

**Status:** mərhələ 1 icra edilib; temporal ML mərhələsi planlaşdırılır.

## Hypothesis
Performance temporal holdout-da saxlanırmı? Null və alternativ hipotez data audit-dən sonra preregister ediləcək.
## Dataset
ClinVar ESummary 2026-09-20 snapshot-u: VCV000002540.168 və VCV000015333.180. Mənbə URL-ləri və seçilmiş sahələr versiyalanmış TSV-dədir.
## Preprocessing
Biological unit, missingness, duplicate IDs və technical covariates audit. Pipeline: label curation → gene/time split → features → model.
## Method
Mərhələ 1: aggregate significance və review status üçün şəffaf rule-based triage. Bu ACMG classifier deyil. Sonrakı mərhələ üçün dated release, gene/time split, VEP və calibration ayrıca preregister edilməlidir.
## Parameters
Seed 42 başlanğıc təklifi; split və tuning grid əvvəlcədən yazılacaq.
## Results
İki record uğurla oxundu və mənbədəki review səviyyəsinə görə sıralandı. HBB expert-panel record-u 9, MEFV multiple-submitter record-u 7 tədris balı aldı. Bal klinik patogenlik ehtimalı deyil.
## Metrics
Hazır: schema, frequency bounds, mənbə və sərhəd testləri. Plan: temporal holdout PR-AUC, calibration, review-status stratification.
## Observations
Aggregate VCV birdən çox condition-i birləşdirir; condition-specific RCV, zygosity və phenotype olmadan klinik nəticə çıxarmaq olmaz. İki variant regional prevalence sübutu deyil.
## Errors
İcra uğurludur. ClinVar həftəlik dəyişdiyi üçün snapshot köhnələ bilər; yeni istifadə canlı record-la müqayisə edilməlidir.
## Interpretation
Layihə sübut sahələrinin oxunmasını göstərir. Fərdi risk, diaqnoz və ya müalicə nəticəsi vermir.
## Next Experiment
Dated ClinVar buraxılışları ilə label dəyişməsini audit et, gene/time split-i dondur, sonra VEP feature-ləri və calibration qiymətləndir. Functional assay yalnız ayrıca sübut mənbəyidir.
