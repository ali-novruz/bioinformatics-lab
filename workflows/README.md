# Xam data-dan analizə

**Status:** Linux positive-control sınağı keçib: tək məlum variant düzgün tapılıb, 422/422 fragment genə sayılıb. [İcra sübutu](https://github.com/ali-novruz/bioinformatics-lab/actions/runs/35044952917). Real və xarici dataset icralarının nəticələri [STATUS](../STATUS.md)-da saxlanılır.

GitHub Actions Linux smoke job-u hər push-da deterministik sintetik reference/read-lərlə variant truth-u və assigned count hədlərini yoxlayır. Bu, production-scale performance benchmark-ı deyil. `SKIP_QC=1 SKIP_MULTIQC=1` yalnız hesabat addımlarını keçir; BWA/STAR üçün yenə Linux alətləri lazımdır.

## Sabit kiçik dataset-lərlə tam icra

```bash
python -m pip install -e '.[research]' 'multiqc>=1.27,<2'
python scripts/run_raw_examples.py --output results/runs/raw-examples-001
```

FastQC, STAR, featureCounts, BWA, SAMtools, BCFtools və Cutadapt PATH-da olmalıdır.
Skript 25 hash-yoxlanmış faylı (təxminən 28.5 MB) endirir. Altı real yeast RNA
sample-ı və ayrıca xarici DNA test dataset-i işləyir. Bütün QC/MultiQC addımları açıqdır.
Mövcud output qovluğu üzərinə yazılmır.

GitHub-da **Actions → Real raw-read examples → Run workflow** eyni işi Linux-da
icra edir. Artifact-də tool versiyaları, input/source hash-ləri, QC hesabatları,
counts, VCF və qrafiklər saxlanılır; böyük BAM/index/FASTQ çıxarılıb.
Artifact saxlanma müddəti 14 gündür; daimi kiçik nəticələr repoda ayrıca saxlanılır.
[RNA data kartı](../datasets/public-datasets/raw-rnaseq.md) və
[DNA data kartı](../datasets/public-datasets/raw-variants.md) interpretasiya şərtlərini göstərir.

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
