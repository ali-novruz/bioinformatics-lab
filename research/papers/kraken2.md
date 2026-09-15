# Improved metagenomic analysis with Kraken 2

**Authors:** Derrick E. Wood, Jennifer Lu, Ben Langmead

**Year:** 2019

**Journal:** Genome Biology

**DOI:** [10.1186/s13059-019-1891-0](https://doi.org/10.1186/s13059-019-1891-0)

**Primary source:** [birbaşa mənbə](https://pmc.ncbi.nlm.nih.gov/articles/PMC6883579/)

**Oxu vəziyyəti (2026-09-15):** Tam mətn: main results və Methods.

## Research Question

Taxonomic classification yaddaş və sürət baxımından necə yaxşılaşdırılır?

## Background

Reference database böyüdükcə k-mer yaddaş xərci artır.

## Dataset

Clade-exclusion və reference-derived simulated reads; prokaryotic/viral references.

## Methodology

Minimizer subsampling və compact hash table ilə taxonomic assignment.

## Algorithms

Lowest common ancestor, minimizers, spaced seeds, translated search variantı.

## Tools

Kraken2; Centrifuge, CLARK, Kraken1/KrakenUniq və Kaiju müqayisələri.

## Results

Məqalə yaddaş/sürət və classification accuracy kompromisini qiymətləndirir.

## Important Findings

Reference-də olmayan taxa üçün clade-exclusion real çətinliyə yaxın sınaqdır.

## Limitations

Reference contamination və absent species səhv assignment yaradır; read classification abundance deyil.

## Potential Improvements

Database-date holdout və unknown taxa rejection.

## My Notes

Microbiome relative abundance compositional-dır; total biomass nəticəsi deyil.

## New Research Questions

Database release dəyişməsi rare taxa false positives-i artırırmı?

## Possible Project Ideas

Mock community threshold sweep.

**Reproduction status:** Original məqalənin benchmark/figure nəticələri burada reproduce edilməyib. “My Notes” bu laboratoriya üçün hazırlanmış analitik qeyddir.
