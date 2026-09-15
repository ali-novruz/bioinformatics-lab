# Xam data-dan analizə

**Status:** Bash workflow-ları yazılıb və sintaksis yoxlaması nəzərdə tutulub; bu Windows host-da işlək Linux/Docker olmadığı üçün real sequencing icrası edilməyib. Python VCF və RNA count analizləri ayrıca faktiki icra olunub. Bunları qarışdırmayın.

GitHub Actions Linux smoke job-u bu workflow-ları kiçik sintetik reference/read-lərlə icra edir. Bu job production-scale performance və biological accuracy benchmark-ı deyil, komandaların işləkliyini yoxlayan regression testidir. Windows/local yoxlaması üçün `SKIP_QC=1 SKIP_MULTIQC=1` mühit dəyişənləri ilə ağır report addımlarını keçmək mümkündür.

## Genomics — paired-end DNA

```bash
bash workflows/variants.sh reference.fa R1.fastq.gz R2.fastq.gz sample01 results/runs/raw-variant-001 2 compatible_genes.gff3
```
Raw QC → optional explicit adapters/quality trim → BWA-MEM → name sort/fixmate → coordinate sort/markdup → BAM → BCFtools pileup/call → normalization/filter → optional `bcftools csq` annotation → MultiQC.

- Ploidy 1 və ya 2 açıq verilir; mixed-ploidy whole human və somatic calling üçün bu sadə yol yetərli deyil.
- PCR duplicates burada mark edilir; UMI/amplicon assay üçün duplicate strategiyası yenidən seçilməlidir.
- `ADAPTER_R1`, `ADAPTER_R2` kit/QC əsasında verilir. Adapter bilinmədən sequence uydurulmur.
- `bcftools csq` uyğun GFF3 gene/transcript/CDS iyerarxiyası tələb edir. GenBank/GFF faylı avtomatik uyğun sayılmır. Alternativ VEP/SnpEff matching build/cache ilə işlədilə bilər.
- GIAB raw reads üçün [NIST source](https://github.com/genome-in-a-bottle/giab_data_indexes) daxilində HG001 platforma və assembly uyğun indeks seçin. Bu repo 120 MB benchmark VCF-in yalnız ilk 1000 qeydini avtomatik endirir; raw reads böyük olduğu üçün avtomatik endirilmir.
- Biological interpretation üçün consequence, population evidence, technical confidence və literature birlikdə audit olunur. PASS “pathogenic” deyil.

## RNA-seq — STAR + gene counts

```bash
SJDB_OVERHANG=99 bash workflows/rnaseq.sh genome.fa genes.gtf R1.fastq.gz R2.fastq.gz sample01 results/runs/raw-rna-001 0
# Single-end üçün ikinci oxunuş arqumenti NONE olmalıdır.
python scripts/combine_counts.py --samples counts_manifest.tsv --output datasets/processed/counts.tsv
python scripts/analyze_counts.py --counts datasets/processed/counts.tsv --metadata samples.csv --design "~ type + condition"
```
`SJDB_OVERHANG=read_length-1`, strand 0/1/2 isə assay metadata əsasında seçilir. STAR default index insan genomunda böyük RAM tələb edir; kiçik genomda genomeSAindexNbases tuning lazım ola bilər. Raw QC-dən adapter problemi çıxarsa Cutadapt tətbiq edib təmiz reads-i verin.

`counts_manifest.tsv`: `sample_id` və `counts_path`; paths manifest-ə nəzərən həll olunur. `samples.csv`: ilk sütun sample ID, sonra `condition` (`treated`/`untreated`) və `type` (`single-read`/`paired-end`). Bütün nümunələr eyni annotasiya ilə sayılmalıdır. Pasilla ilkin raw metadata [GEO GSE18508](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE18508) və paket vignette-dədir; raw run-ların biological sample ilə mapping-i avtomatik təxmin edilmir.

Gene count yolunun sonunda normalization, DE, PCA/heatmap/volcano və interpretasiya Python layihəsindədir. Salmon alternativi transcript quantification və uyğun tximport aggregation tələb edir; STAR count matrix-ə eyni sütun adı verərək əvəz etmək olmaz.
