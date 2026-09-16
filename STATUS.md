# Repository vəziyyəti — 2026-09-16

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
| Yoxlamalar | 16 Python test; local links və notebook schemas keçdi |
| Raw workflow syntax | İki Bash faylı syntax check-dən keçdi |
| Raw workflow Linux smoke | Keçdi: məlum tək PASS SNV və 422/422 gene-assigned fragment |
| Real xam RNA-seq | GSE110004: 6 sample, 300,000 pair; FastQC → STAR → featureCounts → PyDESeq2; 84 tested gene və 3 qrafik |
| Xarici xam DNA nümunəsi | nf-core/sarek fixture: QC → trimming → BWA → BCFtools; 32 variant record, 27 PASS |
| İcra sübutları | [Raw nəticələr və QC](results/raw-examples/README.md), [positive control](results/linux-smoke/README.md) |

## İcranın əhatəsi və qalan iş

- **DNA:** FASTQ-dan VCF-ə qədər iki kiçik dataset-də Linux icrası tamamlanıb. Consequence annotation, müstəqil truth-set accuracy ölçülməsi və böyük genom icrası hələ aparılmayıb. Xarici test dataset-inin donor provenance-i təsdiqlənməyib.
- **RNA:** Real GSE110004 chromosome I subsample-ında xam oxunuşdan model və qrafiklərə qədər yol tamamlanıb. Pasilla count analizi də ayrıca işləyir. Tam genom, tam məqalə reproduksiyası və pasilla raw FASTQ icrası ilə eyni deyil.
- **Pathway inference:** plotting nümunəsi konseptualdır; real gene-set enrichment eksperiment nəticəsi yoxdur.
- **Manhattan və filogenetik ağac:** qrafik API-si işləyir, data sintetik/illüstrativdir; real GWAS/tree inference başa çatdırılmış kimi göstərilmir.

## Tədqiqat üçün növbəti işlər

6 əsas research question və 10 advanced experiment protocol hazırdır; advanced layihələrin hamısı implementasiya/eksperiment kimi tamamlanmayıb. External cohort validation, full-scale raw pipeline run, R/PyDESeq2 comparison, AlphaFold training/CASP reproduction və klinik validasiya aparılmayıb. Kiçik raw pipeline icraları tamamlanıb və [Actions sübutu](https://github.com/ali-novruz/bioinformatics-lab/actions/runs/35045137065) saxlanılıb.

Bu, işlək **ilk laboratoriya versiyasıdır**. Bütün bioinformatika mövzularının dərslik səviyyəsində tam əhatəsi və bütün gələcək research layihələrinin icrası kimi təqdim edilmir. [Roadmap](roadmap/README.md) dərinləşdirmə meyarlarını, [nəticələr](results/README.md) isə faktiki müşahidələri göstərir.
