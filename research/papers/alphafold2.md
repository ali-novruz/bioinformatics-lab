# Highly accurate protein structure prediction with AlphaFold

**Authors:** John Jumper və həmmüəlliflər; tam müəllif siyahısı mənbədə

**Year:** 2021

**Journal:** Nature

**DOI:** [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)

**Primary source:** [birbaşa mənbə](https://www.nature.com/articles/s41586-021-03819-2)

**Oxu vəziyyəti (2026-09-15):** Tam mətn: CASP14 nəticələri, arxitektura və confidence bölmələri.

## Research Question

Sequence və evolution məlumatı atom səviyyəsinə yaxın struktur proqnozu verə bilərmi?

## Background

Eksperimental struktur coverage sequence məkanından geri qalırdı.

## Dataset

PDB training strukturları, sequence/MSA resursları və blind CASP14 test target-ları.

## Methodology

MSA və residue-pair representations, structure module və iterative refinement.

## Algorithms

Evoformer, attention, invariant point attention və recycling.

## Tools

AlphaFold2; struktur qiymətləndirmə üçün CASP metrikləri.

## Results

CASP14 domain-lərində məqalə 0.96 Å median Cα r.m.s.d.95 bildirir; bu bütün protein/komplekslərə ümumi rəqəm deyil.

## Important Findings

Confidence region üzrə qiymətləndirilməlidir; predicted structure ilə biological mechanism ayrıdır.

## Limitations

Disorder, alternativ states, ligand və kompleks konteksti ayrıca yoxlanmalıdır.

## Potential Improvements

Temporal/sequence-separated struktur benchmark və confidence calibration.

## My Notes

Repo struktur oxuma/contact map yaradır; AlphaFold training və CASP təkrarı etmir.

## New Research Questions

Aşağı pLDDT model səhvi ilə disorder-i nə qədər ayırır?

## Possible Project Ideas

Experimental/predicted contact map comparison.

**Reproduction status:** Original məqalənin benchmark/figure nəticələri burada reproduce edilməyib. “My Notes” bu laboratoriya üçün hazırlanmış analitik qeyddir.
