# A Deep Learning Approach to Antibiotic Discovery

**Authors:** Jonathan M. Stokes və həmmüəlliflər; tam siyahı mənbədə

**Year:** 2020

**Journal:** Cell

**DOI:** [10.1016/j.cell.2020.01.021](https://doi.org/10.1016/j.cell.2020.01.021)

**Primary source:** [birbaşa mənbə](https://www.cell.com/cell/fulltext/S0092-8674(20)30102-1)

**Oxu vəziyyəti (2026-09-15):** Tam mətn: model, chemical validation, Results və Discussion.

## Research Question

Model mövcud antibiotiklərə strukturca fərqli antibacterial molekullar seçə bilərmi?

## Background

Antibiotic resistance yeni kimyəvi namizədlər tələb edir.

## Dataset

Antibacterial activity assay, Drug Repurposing Hub və ZINC15 candidate library.

## Methodology

Molecular graph model ilə screening, sonra seçilmiş namizədlərin eksperimental yoxlanması.

## Algorithms

Directed message passing neural network və əlavə molecular features; RF/SVM baseline-ları.

## Tools

D-MPNN, RDKit, scikit-learn və wet-lab assay-lər.

## Results

Halicin və başqa namizədlərdə eksperimental antibacterial fəaliyyət göstərilir; repo həmin nəticəni reproduce etmir.

## Important Findings

ML ranking bioloji assay ilə təsdiqlənməlidir.

## Limitations

Curated candidate seçimində selection bias; in-vitro/murine nəticə insan klinik effektivliyi deyil.

## Potential Improvements

Scaffold-separated və prospective blind validation.

## My Notes

Sırf docking score bu məqalədəki validation səviyyəsini əvəz etməz.

## New Research Questions

Model uncertainty yeni scaffold hit-rate ilə əlaqəlidirmi?

## Possible Project Ideas

Scaffold split və uncertainty-aware prioritization.

**Reproduction status:** Original məqalənin benchmark/figure nəticələri burada reproduce edilməyib. “My Notes” bu laboratoriya üçün hazırlanmış analitik qeyddir.
