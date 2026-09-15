# Salmon provides fast and bias-aware quantification of transcript expression

**Authors:** Rob Patro, Geet Duggal, Michael I. Love, Rafael A. Irizarry, Carl Kingsford

**Year:** 2017

**Journal:** Nature Methods

**DOI:** [10.1038/nmeth.4197](https://doi.org/10.1038/nmeth.4197)

**Primary source:** [birbaşa mənbə](https://pmc.ncbi.nlm.nih.gov/articles/PMC5600148/)

**Oxu vəziyyəti (2026-09-15):** Tam mətn: main results və Online Methods; PMC manuscript başlığı fərqli təqdimatdır.

## Research Question

Transcript bolluğunu sürətlə və technical bias-a həssas şəkildə hesablamaq olarmı?

## Background

Isoform multimapping və fragment bias differential expression-i dəyişə bilər.

## Dataset

Polyester/RSEM-sim, GEUVADIS və SEQC müqayisələri.

## Methodology

Online/offline inference ilə abundance və sample-specific bias modellərini qiymətləndirir.

## Algorithms

Equivalence classes, fragment-GC/sequence/position bias, probabilistic allocation.

## Tools

Salmon; müqayisələr kallisto və eXpress/Bowtie2.

## Results

Bias olan və ideal simulyasiyalarda metod fərqləri eyni deyil; texniki center contrast-da false DE azala bilər.

## Important Findings

Quantification seçimləri downstream DE-yə ötürülür.

## Limitations

Annotasiya olunmamış yeni transkriptləri özü assemble etmir; generative modelə uyğun simulyasiya üstünlüyü şişirdə bilər.

## Potential Improvements

Decoy-aware reference və annotation-release sensitivity.

## My Notes

Salmon abundance birbaşa DESeq2 raw integer matrix əvəzi deyil; uyğun aggregation lazımdır.

## New Research Questions

GC bias correction hansı transcript siniflərinə daha çox təsir edir?

## Possible Project Ideas

Quantifier dəyişməsi ilə isoform switch sabitliyi.

**Reproduction status:** Original məqalənin benchmark/figure nəticələri burada reproduce edilməyib. “My Notes” bu laboratoriya üçün hazırlanmış analitik qeyddir.
