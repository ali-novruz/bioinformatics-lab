# PLINK BED/BIM/FAM

PLINK binary dataset `.bed` packed genotip, `.bim` variant metadata və `.fam` sample/pedigree metadata üçlüyüdür. `.bed` tək oxunmur. Allele order REF/ALT mənası verməyə bilər; build və strand harmonization ayrıca aparılır.

QC: duplicate ID, A/T və C/G ambiguity, sex check, missingness, heterozygosity, relatedness, HWE siyasəti və ancestry PCA. Case cohort-da sərt HWE filter-i real association-u silə bilər. `plink2 --bfile cohort --missing --freq --hardy --out qc`. [PLINK formats](https://www.cog-genomics.org/plink/2.0/formats).
