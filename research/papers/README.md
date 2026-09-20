# Məqalə təhlilləri

Bu ilkin seçmə systematic review və ya 2026-cı ilin tam “state of the art” icmalı deyil. Əsas metod ailələrini öyrənmək üçün məqsədli seçilmiş ilkin mənbələrdir. DOI/metadata və əlçatan mətn hissələri yoxlanıb.

| Qeyd | İl | Oxu səviyyəsi |
|---|---|---|
| [Basic local alignment search tool](blast.md) | 1990 | Abstract və bibliographic metadata; tam metod/benchmark oxunmayıb. |
| [Fast and accurate short read alignment with Burrows–Wheeler transform](bwa.md) | 2009 | Tam mətn: Methods, Results, Discussion. |
| [The Genome Analysis Toolkit: A MapReduce framework for analyzing next-generation DNA sequencing data](gatk.md) | 2010 | Tam mətn: architecture, Results, Discussion. |
| [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](deseq2.md) | 2014 | Tam mətn: Background, Results, model bölmələri. |
| [Salmon provides fast and bias-aware quantification of transcript expression](salmon.md) | 2017 | Tam mətn: main results və Online Methods; PMC manuscript başlığı fərqli təqdimatdır. |
| [Highly accurate protein structure prediction with AlphaFold](alphafold2.md) | 2021 | Tam mətn: CASP14 nəticələri, arxitektura və confidence bölmələri. |
| [Comprehensive integration of single-cell data](seurat.md) | 2019 | Tam mətn: anchors, atlas integration, label transfer və Methods. |
| [Improved metagenomic analysis with Kraken 2](kraken2.md) | 2019 | Tam mətn: main results və Methods. |
| [An Integrated TCGA Pan-Cancer Clinical Data Resource to Drive High-Quality Survival Outcome Analytics](tcga-cdr.md) | 2018 | Tam mətn: Summary, endpoints, cohort və statistical limitations. |
| [A universal SNP and small-indel variant caller using deep neural networks](deepvariant.md) | 2018 | Abstract, citation və author metadata; əsas mətn giriş məhdudiyyətlidir. |
| [A Deep Learning Approach to Antibiotic Discovery](antibiotic-ai.md) | 2020 | Tam mətn: model, chemical validation, Results və Discussion. |

## Genişləndirilmiş analitik kataloq

Əlavə 26 qeyd eyni şablonla research question, metod, evidence scope, məhdudiyyət, repo əlaqəsi və növbəti eksperimenti ayırır.

- **Alignment və əsas alqoritmlər:** [Needleman–Wunsch](needleman-wunsch.md), [Smith–Waterman](smith-waterman.md), [Clustal Omega](clustal-omega.md), [HMMER3](hmmer3.md)
- **Read mapping və genom alətləri:** [Bowtie 2](bowtie2.md), [STAR](star.md), [HISAT2](hisat2.md), [SAMtools](samtools.md), [BEDTools](bedtools.md), [minimap2](minimap2.md)
- **Expression və single-cell:** [edgeR](edger.md), [limma-voom](limma-voom.md), [t-SNE](tsne.md), [UMAP](umap.md), [Scanpy](scanpy.md), [Harmony](harmony.md), [scVI](scvi.md)
- **Assembly və metagenomika:** [SPAdes](spades.md), [Flye](flye.md), [MetaPhlAn2](metaphlan2.md), [QIIME 2](qiime2.md)
- **Populyasiya və genom resursları:** [PLINK](plink.md), [Human Genome](human-genome.md), [T2T-CHM13](t2t-chm13.md)
- **Bioloji foundation modelləri:** [ESM-2](esm2.md), [Enformer](enformer.md)

Beləliklə kataloqda **37 primary-source note** var. Bu say systematic review mənasına gəlmir; seçim tədris əhatəsini genişləndirmək üçündür.

Search trace: DESeq2, Salmon və AlphaFold başlıqları ilə paper-index sorğuları; metod ailələri üçün geniş sorğu; DESeq2 related-papers sorğusu nəticə qaytarmadığı üçün müəllif/jurnal primary səhifələrinə keçildi. Geniş sorğudakı əlaqəsiz və təsdiqlənməmiş nəticələr daxil edilmədi. Publisher content və PMC arasında başlıq fərqləri note-da açıqlanır.
