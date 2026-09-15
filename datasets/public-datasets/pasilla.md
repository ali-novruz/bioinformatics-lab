# Pasilla RNA-seq gene counts

**Source / version:** Bioconductor pasilla 1.40.0; original Brooks et al., Genome Research 2011; GEO GSE18508

**Dataset description:** Drosophila melanogaster pasilla RNAi knockdown və untreated müqayisəsi; paket per-gene read sayımlarını verir.

**Files:** pasilla_gene_counts.tsv, pasilla_sample_annotation.csv

**Columns/features və biological meaning:** 14,599 genes × 7 libraries; counts sütunları sample ID, sətirlər FlyBase gene ID. Metadata: condition, type, lanes, reads, exon counts.

**License / access:** Paket səhifəsində LGPL göstərilir. İlkin data/submitter şərtləri ayrıca qüvvədədir; burada raw files Git-də yayılmır.

**Size / checksum (faktiki endirilən məzmun):** pasilla_gene_counts.tsv: 498,373 bytes; SHA-256 `ea0dafbfcc600559644cfe7dd5cc8de809d631eb64ba3089aaa25c2fa0954dad`; pasilla_sample_annotation.csv: 527 bytes; SHA-256 `1844f871ca5d750f41685c73b87bd7dda291ec0d52304c1afb46a17ae88db745`

## Download instructions
```bash
python scripts/fetch_data.py --dataset pasilla
```
Raw fayllar `datasets/raw/` daxilində saxlanır və Git-ə daxil edilmir. [Reference manifest](../reference-manifest.json) ilk doğrulanmış snapshot-u göstərir; local manifest hər run-da yoxlanır.

## Məhdudiyyətlər
7 library, 4 untreated və 3 treated; single-read/paired-end kovariatını saxlayın. Paketin gene-level count dataset-i exon-splicing nəticələrinin tam təkrarı deyil.

Rəsmi mənbə: [Pasilla RNA-seq gene counts](https://bioconductor.org/packages/release/data/experiment/html/pasilla.html).
