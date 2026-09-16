# Bioinformatics Research Lab

[![Validate lab](https://github.com/ali-novruz/bioinformatics-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/ali-novruz/bioinformatics-lab/actions/workflows/ci.yml)

[Buradan başlayın](docs/START_HERE.md) · [İcra vəziyyəti](STATUS.md) · [Nəticələr](results/README.md) · [30 layihə](projects/IDEAS.md)

**Öyrən → kodlaşdır → real data ilə yoxla → nəticəni izah et → yeni sual yarat.**

Azərbaycan dilində şəxsi bioinformatika laboratoriyası: biologiyanın əsaslarından reproducible tədqiqat layihələrinə qədər. Kod və standart terminlər ingiliscədir. Bu repo birdəfəlik konspekt deyil; hər eksperiment məlumatın mənşəyini, parametrləri, nəticələri və məhdudiyyətləri saxlayır.

## Başlamaq

Python 3.12 tövsiyə olunur. Əmrləri repository kökündə icra edin.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -e ".[dev,research]"
python -m pytest
python scripts/lab.py list
python scripts/lab.py run all
python scripts/make_visualizations.py
python scripts/check_repository.py
```

Səkkiz layihə `python scripts/lab.py run all --offline` ilə şəbəkəsiz işləyir. Qalan dörd layihənin ilk endirilməsi internet tələb edir. RNA-seq sayım analizi Python ilə işləyir; xam FASTQ üçün əlavə Linux/WSL/Conda alətləri lazımdır. Offline CI hər push/PR-də, endirməli integration və Linux smoke isə main push və manual icrada işləyir. Tam quraşdırma: [SETUP.md](SETUP.md). Faktiki icra vəziyyəti: [STATUS.md](STATUS.md).

## Repository xəritəsi

| Bölmə | Məqsəd |
|---|---|
| [docs](docs/README.md) | Biologiya, alqoritmlər, formatlar, omics və statistika |
| [resources](resources/README.md) | Databazalar, kitablar, kurslar və rəsmi alətlər |
| [research/papers](research/papers/README.md) | Mənbəsi yoxlanmış məqalə təhlilləri |
| [research/literature-reviews](research/literature-reviews/README.md) | Metod müqayisələri və açıq problemlər |
| [research/research-questions](research/research-questions/README.md) | Sınaqdan keçirilə bilən hipotezlər |
| [projects](projects/README.md) | 12 işlək layihə, vahid başladıcı və 30 gələcək eksperiment ideyası |
| [datasets](datasets/README.md) | Məlumat kartları, endirmə və provenance |
| [src](src/biolab) | Təkrar istifadə olunan Python paketi |
| [notebooks](notebooks/README.md) | Problem–nəticə–interpretasiya ardıcıllığı |
| [experiments](experiments/README.md) | Parametrlər, xətalar və növbəti eksperiment |
| [results](results/README.md) | Hesabatlar, metriklər və interpretasiyalar |
| [visualizations](visualizations/README.md) | Reproduksiya olunan qrafiklər |
| [roadmap](roadmap/README.md) | 10 mərhələli öyrənmə proqramı |

## İlk beş layihə

1. [DNA Sequence Analyzer](projects/beginner/dna-analyzer/README.md): FASTA, GC, reverse complement, transkripsiya, kodonlar, motiflər.
2. [Sequence Alignment Tool](projects/beginner/sequence-alignment/README.md): Needleman–Wunsch, Smith–Waterman və Biopython ilə yoxlama.
3. [Genomic Variant Analysis](projects/intermediate/variant-analysis/README.md): VCF keyfiyyət və variant xülasəsi; ayrıca FASTQ → BWA → BCFtools workflow.
4. [RNA-Seq Gene Expression](projects/intermediate/rnaseq/README.md): real pasilla count matrix, dizayn kovariatı, PyDESeq2, PCA, heatmap və volcano.
5. [Disease Classification](projects/intermediate/disease-classification/README.md): real Wisconsin breast cancer məlumatı, sızmasız cross-validation, ayrıca test dəsti və etibar intervalı.

**Xam məlumatla işləyən əlavə icra:** altı real yeast RNA-seq sample-ında
FASTQ → FastQC → STAR → featureCounts → PyDESeq2 → qrafiklər tamamlanıb.
Xarici DNA test dəstində FASTQ → trimming → BWA → variant calling də işlədi.
[Nəticələr və təkrar icra](results/raw-examples/README.md).

## Tədqiqat istiqamətləri

Genomics, transcriptomics, proteomics, sequence analysis, structural bioinformatics, systems biology, computational biology və machine learning. [Layihə kataloqu](projects/IDEAS.md) bu sahələri beginner → intermediate → research ardıcıllığına bağlayır.

## Elmi iş qaydası

- Xam data dəyişdirilmir; böyük fayllar Git-ə daxil edilmir.
- Hər data mənbəsi accession/versiya, lisenziya vəziyyəti, ölçü və SHA-256 ilə qeyd olunur.
- Tədris datası, real analiz, təklif olunan tədqiqat və reproduce edilmiş məqalə ayrı statuslardır.
- P-value effektin ölçüsü deyil; FDR, effekt ölçüsü, sample size və batch təsirləri birlikdə şərh edilir.
- Modelin bütün preprocessing addımları training fold daxilində öyrənilir.
- Klinik və ya səbəb-nəticə iddiası yalnız bu notebook-lardan çıxarılmır.

## Texnologiyalar

Python, Biopython, NumPy, pandas, SciPy, matplotlib, scikit-learn, statsmodels, PyDESeq2, Jupyter. Genişlənmə: pysam, Scanpy/AnnData, NetworkX, R/Bioconductor (DESeq2, edgeR, limma, Seurat), FastQC, MultiQC, Cutadapt, BWA, SAMtools, BCFtools, STAR, Salmon, GATK, VEP və SnpEff.

## İnkişaf və gələcək iş

[STATUS](STATUS.md) icra edilmiş işləri, [CHANGELOG](CHANGELOG.md) qurulma mərhələlərini, [roadmap](roadmap/README.md) isə keçid meyarlarını saxlayır. Sonrakı elmi prioritetlər: müstəqil cohort validasiyası, variant truth-set benchmark, single-cell donor-aware analiz və multi-omics inteqrasiyası.

Töhfə vermək: [CONTRIBUTING.md](CONTRIBUTING.md). Mənbə və data istifadəsi: [DATA_POLICY.md](DATA_POLICY.md). Citation məlumatı: [CITATION.cff](CITATION.cff).

## UNEC praktikum paketi

[8 dərs və 15 həftəlik proqram](docs/unec/README.md), [68 fayllıq mənbə kataloqu](resources/unec/README.md), [4 PDF kitab](resources/books/README.md) və [24 cavablı tapşırıq](docs/unec/exercises.md) əlavə olunub. Üç yeni işlək layihə gen ifadəsi təsnifatı, real RNA sayımları üçün SQLite və çoxsaylı statistik testləri əhatə edir. [Nəticələr](results/course-projects/README.md) · [PDF praktikum](resources/unec/bioinformatika-praktikum.pdf).

## Tam layihə paketi

[12 işlək layihə](projects/README.md) vahid başladıcısı ilə idarə olunur. Yeni real analizlər: GO-slim enrichment, bootstrap filogeniya və dairəvi genom ORF axtarışı. [Yenidən baxış və düzəlişlər](docs/REPOSITORY_AUDIT.md), [saxlanmış icra hesabatı](results/expanded-projects/README.md).

## Tənqidi elmi audit

[12 baxış üzrə audit](docs/RESEARCH_AUDIT.md) mövcud nəticələri nəzarət təcrübələri ilə sınayır: Khan training-only nested CV və 99 label permutation; GO üçün bütün 84 singleton seçiminin statistik çatımlılığı. [Faktiki nəticələr](results/research-audit/README.md) və [təkrar icra](experiments/controls/README.md). Yeni probe stability nəticəsi yüksək prediction score-un sabit biomarker siyahısı olmadığını göstərir.
