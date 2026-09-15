# Comprehensive integration of single-cell data

**Authors:** Tim Stuart və həmmüəlliflər; tam siyahı mənbədə

**Year:** 2019

**Journal:** Cell

**DOI:** [10.1016/j.cell.2019.05.031](https://doi.org/10.1016/j.cell.2019.05.031)

**Primary source:** [birbaşa mənbə](https://pmc.ncbi.nlm.nih.gov/articles/PMC6687398/)

**Oxu vəziyyəti (2026-09-15):** Tam mətn: anchors, atlas integration, label transfer və Methods.

## Research Question

Fərqli single-cell dataset/modalities arasında uyğun hüceyrə vəziyyətlərini birləşdirmək olarmı?

## Background

Batch və platforma təsiri atlas qurmağı çətinləşdirir.

## Dataset

Müxtəlif scRNA-seq dataset-ləri, Tabula Muris, bone marrow CITE-seq və spatial nümunələr.

## Methodology

Anchor correspondence tap, score/weight hesabla, integration və label transfer et.

## Algorithms

CCA/nearest-neighbour anchors, weighting, imputation/transfer.

## Tools

Seurat v3; cari Seurat implementasiyası ayrıca versiyalanmalıdır.

## Results

Integration və reference→query cell-state transfer nümunələri göstərilir.

## Important Findings

Batch mixing yaxşılaşması biological structure preservation ilə birlikdə ölçülməlidir.

## Limitations

Yanlış anchors nadir və yeni vəziyyətləri silə bilər; inferred protein ölçülmüş protein deyil.

## Potential Improvements

Donor holdout, rare-state retention və unknown-label rejection.

## My Notes

Differential testing üçün integration embeddings-ni raw donor-level counts ilə qarışdırmamaq lazımdır.

## New Research Questions

Anchor confidence nadir hüceyrədə səhv label-i proqnozlaşdırırmı?

## Possible Project Ideas

Batch correction ablation və donor-aware pseudobulk.

**Reproduction status:** Original məqalənin benchmark/figure nəticələri burada reproduce edilməyib. “My Notes” bu laboratoriya üçün hazırlanmış analitik qeyddir.
