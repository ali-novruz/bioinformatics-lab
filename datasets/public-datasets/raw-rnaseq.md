# GSE110004 — real xam RNA-seq nümunəsi

## Mənbə və seçim

**S. cerevisiae**, 101 bp paired-end, reverse-stranded RNA-seq. Altı biological
sample: üç Rap1-AID uninduced və üç Rap1-AID + IAA 30 dəqiqə.
Accession, qrup və təkrarlar [metadata CSV](../raw-rnaseq-samples.csv)-dədir.

İlkin iş: Wu et al., *Repression of Divergent Noncoding Transcription by a
Sequence-Specific Transcription Factor*, Molecular Cell (2018),
[DOI](https://doi.org/10.1016/j.molcel.2018.10.018),
[GEO GSE110004](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE110004).

İstifadə etdiyimiz kiçik fayllar
[nf-core mənbə qeydi](https://github.com/nf-core/test-datasets/blob/e07c1b158d1c4c9ea7978959d31e651098bec581/README.md)
əsasında chromosome I-ə Kraken2 ilə seçilmiş və seqtk seed 100 ilə hər sample
üçün 50,000 cütə azaldılmışdır. Reference yeast R64-1-1 chromosome I və onun
GTF annotasiyasıdır. Reverse strand seçimi
[nf-core samplesheet](https://github.com/nf-core/test-datasets/blob/e07c1b158d1c4c9ea7978959d31e651098bec581/samplesheet/samplesheet.csv)
ilə yoxlanıb. Oradakı bəzi təkrar nömrələri təkrarlanır; bizim biological replicate
mapping yuxarıdakı README accession cədvəlindən götürülüb.

Bu test GTF-də bir CDS sətri `not_in_genome` contig-ni göstərir; exon sətrləri
chromosome I-dədir. İcra exon annotation istifadə edir. Xam GTF dəyişdirilmir;
fayl başqa annotation məqsədləri üçün ayrıca yoxlanmalıdır.

## İcra

FastQC → STAR → coordinate-sorted BAM → featureCounts (paired, strand 2) →
gene ID əsasında sayım birləşməsi → PyDESeq2 (`~ condition`) → PCA, heatmap, volcano.

Bütün sample-lar paired-end olduğundan sabit `type` sütunu dizayna daxil edilmir.
Reference kiçikdir: STAR `genomeSAindexNbases=7`, `sjdbOverhang=100`.
Mapping yoxlaması hər sample-da 50,000 cüt, ən azı 50% unique mapping və 1,000
assigned fragment tələb edir. Bunlar bu kiçik inteqrasiya nümunəsinin yoxlama
hədləridir, bütün RNA-seq layihələri üçün keyfiyyət standartı deyil.

## Təkrar endirmə və provenance

```bash
python scripts/fetch_raw_examples.py --dataset rnaseq
```

[Manifest](../raw-examples-manifest.json) immutable Git commit URL-lərini, ölçü
və SHA-256-nı saxlayır. Xam FASTQ repoya əlavə edilmir.
Faylların ilkin data istifadəsi şərtləri qüvvədə qalır; repo lisenziyası ilə
yenidən lisenziyalaşdırılmır.

## Nəticənin sərhədi

Bu, real oxunuşlardan başlayan **chromosome I subsample** analizidir.
Kraken2 seçimi, azaldılmış dərinlik, yalnız bir chromosome və altı sample
nəticəyə təsir edir. Model FDR-i yalnız analiz edilən genlər ailəsinə aiddir.
Genom üzrə discovery, tam məqalə reproduksiyası və divergent noncoding
transcription mexanizminin təsdiqi kimi şərh edilməməlidir.
Gene-level exon sayımı orijinal işin bütün transkripsiya hadisələrini tutmur.
