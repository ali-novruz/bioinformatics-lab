# Protein sequence-dan function prediction

**Status:** təklif; novelty və nəticə təsdiqlənməyib.

## Problem

Homologların split-lərdə paylaşılması proqnozu şişirdir.

## Hypothesis

Cluster-separated embeddings composition baseline-dan üstün olsa da random split üstünlüyü azalır.

## Why It Matters

Unknown protein annotation üçün etibarlı prioritet yaratmaq.

## Available Datasets

UniProt experimentally supported GO terms; release pin edilir.

## Possible Methodology

Sequence clustering, multi-label baseline, embedding ablation və temporal holdout.

## Required Tools

MMseqs2, UniProt API, scikit-learn

## Expected Challenges

Incomplete negatives, GO hierarchy və label imbalance.

## Evaluation Metrics

Macro/micro PR-AUC, rare-label recall, cluster-distance strata.

## Possible Outcomes

Uzaq homologlarda modelin abstain etməsi daha uyğun ola bilər.

## Future Extensions

Domain-level interpretability və assay.
