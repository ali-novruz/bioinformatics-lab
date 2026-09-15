# Genomics + ML: caller transfer

**Status:** təklif; novelty və nəticə təsdiqlənməyib.

## Problem

Model bir sequencing platformasını öyrənib digərində səhv edə bilər.

## Hypothesis

Platforma dəyişikliyi indel/repeat error-larını SNV-lərdən daha çox artırır.

## Why It Matters

Caller accuracy-nin istifadə kontekstinə uyğunluğunu qiymətləndirmək.

## Available Datasets

GIAB HG001/HG002 truth regions və platforma-uyğun açıq reads.

## Possible Methodology

Eyni referens, caller version və confident regions; sample/platform holdout.

## Required Tools

BWA, DeepVariant/BCFtools, hap.py

## Expected Challenges

Compute xərci, normalized representation, training overlap.

## Evaluation Metrics

Stratified precision/recall/F1, calibration və runtime.

## Possible Outcomes

Ümumi F1 yüksək olsa da çətin region zəif qala bilər.

## Future Extensions

Pangenome və long-read müqayisəsi.
