# Fast and accurate short read alignment with Burrows–Wheeler transform

**Authors:** Heng Li, Richard Durbin

**Year:** 2009

**Journal:** Bioinformatics

**DOI:** [10.1093/bioinformatics/btp324](https://doi.org/10.1093/bioinformatics/btp324)

**Primary source:** [birbaşa mənbə](https://pmc.ncbi.nlm.nih.gov/articles/PMC2705234/)

**Oxu vəziyyəti (2026-09-15):** Tam mətn: Methods, Results, Discussion.

## Research Question

Short read alignment yaddaş və vaxt baxımından necə ölçülə bilər?

## Background

Hash və əvvəlki aligner-lər speed/memory kompromisi yaradırdı.

## Dataset

Human genome-dan simulyasiya; real sequencing reads və human–chicken referenslə səhv mapping yoxlaması.

## Methodology

Referensi BWT ilə indekslə; backward search və bounded backtracking ilə inexact alignment; mapping quality.

## Algorithms

Burrows–Wheeler transform, suffix-array intervals, paired-end mapping.

## Tools

Məqalədəki BWA; burada workflow BWA-MEM istifadə edir, 2009 BWA-aln benchmark-ı ilə eyni deyil.

## Results

Simulyasiya və real reads-də vaxt, yaddaş və alignment accuracy müqayisə edilir.

## Important Findings

Referens indeksinin strukturu geniş miqyaslı analizi mümkün edir.

## Limitations

Simulyasiya noise və repetition-u tam əks etdirməyə bilər; cross-species yanlış mapping estimate-i də fərziyyələr daşıyır.

## Potential Improvements

Repeat-stratified və indel-length-stratified benchmark.

## My Notes

Mapper və caller-i eyni anda dəyişmək fərqin mənbəyini gizlədir.

## New Research Questions

Mapping ambiguity hansı regionlarda variant çağırışına keçir?

## Possible Project Ideas

BWA və Bowtie2 eyni truth-set üzrə müqayisə.

**Reproduction status:** Original məqalənin benchmark/figure nəticələri burada reproduce edilməyib. “My Notes” bu laboratoriya üçün hazırlanmış analitik qeyddir.
