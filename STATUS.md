# Repository vəziyyəti — 2026-09-15

## Hazır və yoxlanmış

| Sahə | Vəziyyət |
|---|---|
| Arxitektura və README | Hazır, mərhələli Git tarixçəsi |
| Biologiya | 16 anlayış: rol, istifadə, nümunə və format |
| Data formatları | 11 format bələdçisi, Python nümunələri |
| Mövzu modulları | Sequence, genomics, transcriptomics, proteomics, structure, systems, ML, statistics və fundamentals |
| Databazalar | 18 database kartı; rəsmi mənbə və API giriş yolu |
| Məqalələr | 11 note; 9 tam mətn bölmələri əsasında, 2 abstract/metadata əsasında |
| Mini reviews | 9 məqsədli review; systematic review deyil |
| Layihə ideyaları | 30: 10 beginner + 10 intermediate + 10 advanced |
| DNA Analyzer | Real PhiX FASTA-da işlədi |
| Alignment Tool | Sintetik sequence-lərdə işlədi; NW/SW score-ları exhaustive kiçik testdə Biopython ilə tutuşduruldu |
| Variant Analysis | Real GIAB prefix VCF üzərində işlədi |
| RNA-seq | Real pasilla counts ilə PyDESeq2 modeli işlədi |
| Disease Classification | Real WDBC morphology data-da sızmasız training CV və holdout test işlədi |
| Protein nümunələri | UniProt P01308 və PDB 1CRN ayrıca analiz edildi |
| Notebook-lar | 5/5 başdan sona icra edildi |
| Qrafiklər | Tələb olunan 11 növ + contact map; real/sintetik status qeyd olunub |
| Yoxlamalar | 14 Python test keçdi; local links və notebook schemas keçdi |
| Raw workflow syntax | İki Bash faylı syntax check-dən keçdi |
| Raw workflow Linux smoke | GitHub Actions-də kiçik paired-read reference ilə BWA/SAMtools/BCFtools və STAR/featureCounts pipeline-ları avtomatik işlədilir |

## Hazır kod var, tam real icra hələ yoxdur

- **FASTQ → BWA → BAM → variant calling → annotation:** Kiçik Linux smoke dataset-i GitHub Actions-də hər push üçün icra edilir. Böyük real genom və klinik benchmark burada avtomatik işlədilmir; VCF-dən başlayan Python analizi faktiki işləyir.
- **FASTQ → STAR → featureCounts → RNA model:** Kiçik Linux smoke dataset-i GitHub Actions-də hər push üçün icra edilir. Real pasilla xam FASTQ-ları və böyük reference burada avtomatik endirilmir; hazır real count matrix-dən başlayan bütün analiz faktiki işləyir.
- **Pathway inference:** plotting nümunəsi konseptualdır; real gene-set enrichment eksperiment nəticəsi yoxdur.
- **Manhattan və filogenetik ağac:** qrafik API-si işləyir, data sintetik/illüstrativdir; real GWAS/tree inference başa çatdırılmış kimi göstərilmir.

## Tədqiqat üçün növbəti işlər

6 əsas research question və 10 advanced experiment protocol hazırdır; advanced layihələrin hamısı implementasiya/eksperiment kimi tamamlanmayıb. External cohort validation, full-scale raw pipeline run, R/PyDESeq2 comparison, AlphaFold training/CASP reproduction və klinik validasiya aparılmayıb. Raw pipeline komandalarının kiçik end-to-end smoke icrası CI-də tamamlanır.

Bu, işlək **ilk laboratoriya versiyasıdır**. Bütün bioinformatika mövzularının dərslik səviyyəsində tam əhatəsi və bütün gələcək research layihələrinin icrası kimi təqdim edilmir. [Roadmap](roadmap/README.md) dərinləşdirmə meyarlarını, [nəticələr](results/README.md) isə faktiki müşahidələri göstərir.
