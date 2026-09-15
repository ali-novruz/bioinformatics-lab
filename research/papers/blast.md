# Basic local alignment search tool

**Authors:** Stephen F. Altschul, Warren Gish, Webb Miller, Eugene W. Myers, David J. Lipman

**Year:** 1990

**Journal:** Journal of Molecular Biology

**DOI:** [10.1016/S0022-2836(05)80360-2](https://doi.org/10.1016/S0022-2836(05)80360-2)

**Primary source:** [birbaşa mənbə](https://pubmed.ncbi.nlm.nih.gov/2231712/)

**Oxu vəziyyəti (2026-09-15):** Abstract və bibliographic metadata; tam metod/benchmark oxunmayıb.

## Research Question

Böyük sequence bazasında local oxşarlığı sürətlə tapmaq mümkündürmü?

## Background

Tam pairwise DP hər database entry üçün bahadır.

## Dataset

Abstract DNA/protein database axtarışını təsvir edir; konkret benchmark dataset tərkibi bu qeyddə təsdiqlənməyib.

## Methodology

Local similarity üçün yüksək score segmentlərini heuristic axtarışla yaxınlaşdırmaq və statistik əhəmiyyətlə qiymətləndirmək.

## Algorithms

Maximal segment pair, seed/extension ideyası; exact DP-dən fərqli sensitivity–speed kompromisi.

## Tools

BLAST; müasir təcrübə üçün NCBI BLAST+ ayrıca versiyalanmalıdır.

## Results

Mənbə müqayisəli sürət üstünlüyü bildirir; burada rəqəmsal benchmark təkrar edilməyib.

## Important Findings

Database ölçüsü ilə statistik significance əlaqəsi sadəcə identity faizindən daha informativdir.

## Limitations

Heuristic bəzi zəif homologları qaçıra bilər; abstract-dan bütün parametr həssaslığını çıxarmaq olmaz.

## Potential Improvements

Composition-matched negative controls və coverage stratification.

## My Notes

Toy seed_search yalnız intuitiv seed mexanizmini göstərir.

## New Research Questions

GC və query length dəyişəndə false matches necə dəyişir?

## Possible Project Ideas

BLAST nəticəsi ilə Smith–Waterman score müqayisəsi.

**Reproduction status:** Original məqalənin benchmark/figure nəticələri burada reproduce edilməyib. “My Notes” bu laboratoriya üçün hazırlanmış analitik qeyddir.
