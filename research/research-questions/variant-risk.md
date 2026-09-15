# Variant prioriteti və xəstəlik riski

**Status:** təklif; novelty və nəticə təsdiqlənməyib.

## Problem

Nadir variantın association ilə pathogenicity-si fərqli anlayışlardır.

## Hypothesis

Review-status və phenotype evidence əlavə ediləndə gene-held-out ranking yaxşılaşır.

## Why It Matters

Yanlış prioritization araşdırma resursunu itirir.

## Available Datasets

ClinVar dated public release, HPO; riski ölçmək üçün ayrıca ancestry-matched case/control cohort tələb olunur.

## Possible Methodology

Temporal və gene split; baseline frequency/consequence; əlavə phenotype evidence ablation.

## Required Tools

VEP, pandas, scikit-learn

## Expected Challenges

Conflicting labels, ancestry və gene leakage.

## Evaluation Metrics

PR-AUC, recall@10, calibration və review-status stratification.

## Possible Outcomes

Yaxşılaşma olmaya bilər; risk association nəticəsi bu ranking-dən çıxmır.

## Future Extensions

Functional assay ilə orthogonal validation.
