# Bioinformatics Research Lab

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
python scripts/fetch_data.py --dataset all
python scripts/run_projects.py --project all
python scripts/make_visualizations.py
python scripts/check_repository.py
```

İlk iki layihə və testlər şəbəkəsiz işləyir. Real məlumatların ilk endirilməsi internet tələb edir. RNA-seq sayım analizi Python ilə işləyir; xam FASTQ üçün əlavə Linux/WSL/Conda alətləri lazımdır. Kiçik xam-read smoke testi GitHub Actions Linux mühitində hər push-da işləyir. Tam quraşdırma: [SETUP.md](SETUP.md). Faktiki icra vəziyyəti: [STATUS.md](STATUS.md).

## Repository xəritəsi

| Bölmə | Məqsəd |
|---|---|
| [docs](docs/README.md) | Biologiya, alqoritmlər, formatlar, omics və statistika |
| [resources](resources/README.md) | Databazalar, kitablar, kurslar və rəsmi alətlər |
| [research/papers](research/papers/README.md) | Mənbəsi yoxlanmış məqalə təhlilləri |
| [research/literature-reviews](research/literature-reviews/README.md) | Metod müqayisələri və açıq problemlər |
| [research/research-questions](research/research-questions/README.md) | Sınaqdan keçirilə bilən hipotezlər |
| [projects](projects/README.md) | 30 layihə ideyası və 5 işlək əsas layihə |
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

[STATUS](STATUS.md) icra edilmiş işləri, [CHANGELOG](CHANGELOG.md) səkkiz qurulma mərhələsini, [roadmap](roadmap/README.md) isə keçid meyarlarını saxlayır. Sonrakı elmi prioritetlər: müstəqil cohort validasiyası, variant truth-set benchmark, single-cell donor-aware analiz və multi-omics inteqrasiyası.

Töhfə vermək: [CONTRIBUTING.md](CONTRIBUTING.md). Mənbə və data istifadəsi: [DATA_POLICY.md](DATA_POLICY.md).
