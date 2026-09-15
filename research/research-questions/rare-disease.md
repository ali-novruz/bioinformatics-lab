# Rare disease variant prioritization

**Status:** təklif; novelty və nəticə təsdiqlənməyib.

## Problem

Mendelian candidate siyahısında phenotype və inheritance evidence birləşməlidir.

## Hypothesis

Phenotype similarity inheritance-compatible ranking-ə əlavə dəyər verir.

## Why It Matters

Tədqiqat üçün daha az, daha əsaslı candidate.

## Available Datasets

Public ClinVar/HPO curated examples; şəxsi patient data istifadə edilmir.

## Possible Methodology

Evidence-dated variant set; gene holdout; inheritance baseline + phenotype score.

## Required Tools

VEP, HPO, Python

## Expected Challenges

Label circularity, incomplete phenotype, penetrance və SV omission.

## Evaluation Metrics

Recall@k, rank distribution, provenance completeness.

## Possible Outcomes

Phenotype az olduqda yanlış prioritet arta bilər.

## Future Extensions

Trio və structural variant evidence.
