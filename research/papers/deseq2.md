# Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2

**Authors:** Michael I. Love, Wolfgang Huber, Simon Anders

**Year:** 2014

**Journal:** Genome Biology

**DOI:** [10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8)

**Primary source:** [birbaşa mənbə](https://pmc.ncbi.nlm.nih.gov/articles/PMC4302049/)

**Oxu vəziyyəti (2026-09-15):** Tam mətn: Background, Results, model bölmələri.

## Research Question

Kiçik replikatlı count data-da effekt və dispersion necə sabit qiymətləndirilə bilər?

## Background

Count discreteness, böyük dynamic range, outliers və mean–variance əlaqəsi sadə testləri çətinləşdirir.

## Dataset

Məqalə real RNA-seq nümunələri və simulyasiyalar istifadə edir; repo pasilla gene counts ilə ayrıca tətbiq edir.

## Methodology

Negative binomial GLM, size factors, dispersion trend/shrinkage və hypothesis testing.

## Algorithms

Empirical Bayes shrinkage, Wald/LRT seçimləri və multiple-testing düzəlişi.

## Tools

R/Bioconductor DESeq2; repo-da Python PyDESeq2 0.5.4.

## Results

Shrinkage sabit effect estimates üçün əsaslandırılır; repo nəticələri ayrıca results-dədir.

## Important Findings

Böyük fold-change çox az count olduqda etibarsız ola bilər.

## Limitations

Model və experimental design uyğunsuzluğu shrinkage ilə düzəlmir. PyDESeq2 nəticəsi original figure reproduksiyası deyil.

## Potential Improvements

Covariate sensitivity və outlier audit; R/Python müqayisəsi.

## My Notes

Repo coefficient-lərə əlavə LFC shrinkage tətbiq etmir; bunu çıxışda qeyd edir.

## New Research Questions

Sequencing type nəzərə alınmadıqda hansı genes dəyişir?

## Possible Project Ideas

Pasilla treated/untreated, type-adjusted analysis.

**Reproduction status:** Original məqalənin benchmark/figure nəticələri burada reproduce edilməyib. “My Notes” bu laboratoriya üçün hazırlanmış analitik qeyddir.
