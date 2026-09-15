# Expression pattern-dən disease classification

**Status:** təklif; novelty və nəticə təsdiqlənməyib.

## Problem

Eyni cohort-da yüksək accuracy platforma signal-ı ola bilər.

## Hypothesis

Leave-study-out split-də regularized baseline random split-dən zəif, lakin daha dürüst nəticə verir.

## Why It Matters

Generalization xəstəlik biomarkerinin əsas tələbindəndir.

## Available Datasets

GEO-da eyni xəstəlik/tissue üçün iki açıq study; accession-lar inclusion audit-dən sonra seçiləcək.

## Possible Methodology

Study daxilində QC; fold-local preprocessing; donor/study holdout; batch-only baseline.

## Required Tools

pandas, scikit-learn, PyDESeq2

## Expected Challenges

Platform fərqi, n≪p, phenotype definition.

## Evaluation Metrics

External AUROC/PR-AUC, sensitivity, calibration, CI.

## Possible Outcomes

Gene signal qala və ya tam platforma ilə izah oluna bilər.

## Future Extensions

Prospective cohort və signature stability.
