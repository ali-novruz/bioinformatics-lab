# Cancer subtype identification

**Status:** təklif; novelty və nəticə təsdiqlənməyib.

## Problem

Molecular clusters stage/tissue ilə qarışa bilər.

## Hypothesis

Subtypes matching clinical covariates daxilində də təkrarlanır.

## Why It Matters

Biological heterogeneity-ni təsvir etmək və candidate mexanizm seçmək.

## Available Datasets

GDC/TCGA open expression və TCGA-CDR metadata.

## Possible Methodology

Donor deduplication; unsupervised training clusters; frozen assignment external validation.

## Required Tools

scikit-learn, GDC API

## Expected Challenges

Outcome-informed cluster tuning və purity confounding.

## Evaluation Metrics

Cluster stability, silhouette ilə yanaşı adjusted covariate association, external consistency.

## Possible Outcomes

Clusters stable olsa da clinical relevance olmaya bilər.

## Future Extensions

Methylation/variant modality ablation.
