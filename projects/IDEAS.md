# 30 bioinformatika layihəsi

10 beginner, 10 intermediate, 10 advanced/research. Bunların hamısı hazır proqram deyil; [13 işlək layihənin dəqiq kataloqu](README.md) ayrıca göstərilir. Epigenomika, GWAS, survival, assembly, long-read, HMM, annotasiya, deep learning, docking, batch correction, API, workflow və immunoinformatika üçün [sahə boşluqları üzrə icra xəritəsi](../roadmap/domain-gaps.md) ayrıca verilir.

## 01. DNA Sequence Analyzer

**Level:** beginner

**Goal:** Sequence keyfiyyətini və kompozisiyanı anlamaq üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Sequence keyfiyyətini və kompozisiyanı anlamaq.

**Research Question:** Ambiguous bazalar GC hesabını nə qədər dəyişir?

**Dataset:** PhiX NC_001422.1. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Biopython.

**Bioinformatics Tools:** Biopython; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** FASTA → validation → GC/reverse-complement → report.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) FASTA mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Base counts və uzunluğu Biopython ilə tutuşdurmaq. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `dna-sequence-analyzer` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Base counts və uzunluğu Biopython ilə tutuşdurmaq.

**Potential Research Extension:** GC skew və pəncərə uzunluğu sensitivity.

**Status:** Əsas implementasiya mövcuddur; layihə README/STATUS-a baxın.

## 02. GC Content Calculator

**Level:** beginner

**Goal:** Sequence compositional variation üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Sequence compositional variation.

**Research Question:** Genom pəncərələrində GC sabitdirmi?

**Dataset:** NC_000913.3, NCBI. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, NumPy, Biopython.

**Bioinformatics Tools:** NumPy, Biopython; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** FASTA → sliding windows → GC profile.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) FASTA mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Window coverage və ambiguous denominator tests. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `gc-content-calculator` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Window coverage və ambiguous denominator tests.

**Potential Research Extension:** Replication origin və gene density konteksti.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 03. FASTA Parser Audit

**Level:** beginner

**Goal:** Sequence metadata bütövlüyü üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Sequence metadata bütövlüyü.

**Research Question:** Duplicate IDs neçə entry-ni yanlış birləşdirir?

**Dataset:** Repo sintetik fixtures; sonra GenBank FASTA. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Biopython.

**Bioinformatics Tools:** Biopython; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** FASTA → streaming parser → validation errors.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) FASTA mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Boş record, duplicate ID və multiline testləri. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `fasta-parser-audit` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Boş record, duplicate ID və multiline testləri.

**Potential Research Extension:** Large-file memory benchmark.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 04. DNA to RNA Converter

**Level:** beginner

**Goal:** Central dogma və strand üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Central dogma və strand.

**Research Question:** Template strand ilə coding strand necə fərqlənir?

**Dataset:** Sintetik DNA; annotated CDS. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Biopython.

**Bioinformatics Tools:** Biopython; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** strand selection → reverse complement if needed → T/U.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) strand selection mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Məlum coding/template pair gözlənən RNA-sı. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `dna-to-rna-converter` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Məlum coding/template pair gözlənən RNA-sı.

**Potential Research Extension:** Alternative genetic codes.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 05. Alignment Visualizer

**Level:** beginner

**Goal:** Homology müqayisəsi üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Homology müqayisəsi.

**Research Question:** Gap penalty optimal alignment-i dəyişirmi?

**Dataset:** Qısa toy sequences və UniProt cütləri. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Biopython, matplotlib.

**Bioinformatics Tools:** Biopython, matplotlib; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** DP score → traceback → annotated columns.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) DP score mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Exact score parity və sequence reconstruction. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `alignment-visualizer` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Exact score parity və sequence reconstruction.

**Potential Research Extension:** Affine gaps və protein BLOSUM62.

**Status:** Əsas implementasiya mövcuddur; layihə README/STATUS-a baxın.

## 06. Codon Analyzer

**Level:** beginner

**Goal:** Translation və codon usage üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Translation və codon usage.

**Research Question:** Genlər arasında kodon istifadəsi fərqlidirmi?

**Dataset:** NCBI CDS FASTA. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Biopython, pandas.

**Bioinformatics Tools:** Biopython, pandas; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** CDS/frame validation → codon counts → relative usage.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) CDS/frame validation mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Incomplete CDS və stop codon audit. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `codon-analyzer` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Incomplete CDS və stop codon audit.

**Potential Research Extension:** Expression/codon usage əlaqəsi.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 07. Mutation Detector

**Level:** beginner

**Goal:** Referensə nisbətən dəyişiklik üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Referensə nisbətən dəyişiklik.

**Research Question:** Eyni mövqedə hansı substitution-lar var?

**Dataset:** Sintetik equal-length sequences. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Python.

**Bioinformatics Tools:** Python; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** coordinate check → differences → table.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) coordinate check mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Known substitutions; unequal-length rejection. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `mutation-detector` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Known substitutions; unequal-length rejection.

**Potential Research Extension:** Indel-aware alignment-based detection.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 08. FASTQ Quality Explorer

**Level:** beginner

**Goal:** Sequencing uncertainty üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Sequencing uncertainty.

**Research Question:** Read sonunda keyfiyyət azalırmı?

**Dataset:** ENA public run-dan bounded FASTQ subset. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Biopython, FastQC.

**Bioinformatics Tools:** Biopython, FastQC; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** FASTQ → Phred per-cycle → QC plot.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) FASTQ mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Encoding və read/quality length checks. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `fastq-quality-explorer` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Encoding və read/quality length checks.

**Potential Research Extension:** Platformlararası QC comparison.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 09. Motif Scanner

**Level:** beginner

**Goal:** Regulatory patterns üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Regulatory patterns.

**Research Question:** Motif tezliyi matched background-dan fərqlənirmi?

**Dataset:** NCBI promoter sequence + shuffled controls. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Python, Biopython.

**Bioinformatics Tools:** Python, Biopython; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** IUPAC motif → overlapping scan → background comparison.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) IUPAC motif mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Known motif locations və permutation null. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `motif-scanner` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Known motif locations və permutation null.

**Potential Research Extension:** PWM və de novo motif discovery.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 10. Protein Composition Explorer

**Level:** beginner

**Goal:** Protein family fərqləri üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Protein family fərqləri.

**Research Question:** Hidrofob residue payı sequence-lər arasında dəyişirmi?

**Dataset:** UniProt P01308 və seçilmiş ailə. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Biopython, UniProt API.

**Bioinformatics Tools:** Biopython, UniProt API; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** FASTA → composition → length/domain context.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) FASTA mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Sequence length və residue totals. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `protein-composition-explorer` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Sequence length və residue totals.

**Potential Research Extension:** Membrane protein enrichment.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 11. BLAST-like Seed Search

**Level:** intermediate

**Goal:** Böyük sequence kolleksiyasında oxşarlıq üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Böyük sequence kolleksiyasında oxşarlıq.

**Research Question:** Seed uzunluğu hit sayı və sensitivity-ni necə dəyişir?

**Dataset:** UniProt kiçik sequence paneli. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Python, BLAST+.

**Bioinformatics Tools:** Python, BLAST+; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** k-mer index → seed hits → local extension → rank.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) k-mer index mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) BLAST+ overlap, runtime; E-value iddiası yox. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `blast-like-seed-search` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** BLAST+ overlap, runtime; E-value iddiası yox.

**Potential Research Extension:** Composition bias və spaced seeds.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 12. Genomic Variant Pipeline

**Level:** intermediate

**Goal:** Reference fərqlərinin aşkarlanması üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Reference fərqlərinin aşkarlanması.

**Research Question:** Filtr seçimi SNV/indel tərkibini dəyişirmi?

**Dataset:** GIAB HG001 v4.2.1; uyğun raw reads. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, BWA, SAMtools, BCFtools.

**Bioinformatics Tools:** BWA, SAMtools, BCFtools; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** FASTQ → QC → mapping → calling → normalization → annotation.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) FASTQ mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) GIAB confident regions precision/recall; subset summary accuracy deyil. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `genomic-variant-pipeline` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** GIAB confident regions precision/recall; subset summary accuracy deyil.

**Potential Research Extension:** Caller/platform stratified benchmark.

**Status:** Əsas implementasiya mövcuddur; layihə README/STATUS-a baxın.

## 13. Gene Expression Analysis

**Level:** intermediate

**Goal:** Treatment transcriptome cavabı üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Treatment transcriptome cavabı.

**Research Question:** Pasilla knockdown hansı genlərlə əlaqəlidir?

**Dataset:** Bioconductor pasilla 1.40.0. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, PyDESeq2, pandas, matplotlib.

**Bioinformatics Tools:** PyDESeq2, pandas, matplotlib; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** counts+metadata → design → DE → PCA/heatmap/volcano.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) counts+metadata mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Covariate audit, FDR və effect-size report. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `gene-expression-analysis` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Covariate audit, FDR və effect-size report.

**Potential Research Extension:** Exon usage və pathway sensitivity.

**Status:** Əsas implementasiya mövcuddur; layihə README/STATUS-a baxın.

## 14. Protein Sequence Classifier

**Level:** intermediate

**Goal:** Function annotation üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Function annotation.

**Research Question:** Sequence kompozisiyası ailəni ayıra bilərmi?

**Dataset:** Evidence-supported UniProt families. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, scikit-learn, CD-HIT/MMseqs2.

**Bioinformatics Tools:** scikit-learn, CD-HIT/MMseqs2; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** cluster split → features → baseline → holdout.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) cluster split mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Macro-F1, PR-AUC və homology leakage audit. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `protein-sequence-classifier` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Macro-F1, PR-AUC və homology leakage audit.

**Potential Research Extension:** Protein embeddings.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 15. Phylogenetic Analysis

**Level:** intermediate

**Goal:** Evolutionary relationships üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Evolutionary relationships.

**Research Question:** Alignment trimming ağac topologiyasını dəyişirmi?

**Dataset:** ENA ortholog sequences. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, MAFFT, IQ-TREE, Biopython.

**Bioinformatics Tools:** MAFFT, IQ-TREE, Biopython; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** ortholog selection → MSA → trim → tree → bootstrap.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) ortholog selection mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Bootstrap support və orthology audit. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `phylogenetic-analysis` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Bootstrap support və orthology audit.

**Potential Research Extension:** Gene-tree/species-tree discordance.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 16. Microbial Genome Analysis

**Level:** intermediate

**Goal:** Genome gene content üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Genome gene content.

**Research Question:** Ştamlar arasında hansı genlər dəyişir?

**Dataset:** NCBI bacterial assemblies. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, QUAST, annotation tools, pandas.

**Bioinformatics Tools:** QUAST, annotation tools, pandas; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** assembly QC → annotation → ortholog clustering → matrix.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) assembly QC mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Completeness/contamination, annotation parity. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `microbial-genome-analysis` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Completeness/contamination, annotation parity.

**Potential Research Extension:** Pangenome-open/closed hypothesis.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 17. Disease Classification Baseline

**Level:** intermediate

**Goal:** Diagnostic label prediction üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Diagnostic label prediction.

**Research Question:** Nüvə xüsusiyyətləri malignancy label-ini ayırırmı?

**Dataset:** UCI WDBC 569 samples, 30 features. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, scikit-learn.

**Bioinformatics Tools:** scikit-learn; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** holdout → training CV → model selection → test.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) holdout mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) AUROC, PR-AUC, sensitivity, specificity, bootstrap CI. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `disease-classification-baseline` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** AUROC, PR-AUC, sensitivity, specificity, bootstrap CI.

**Potential Research Extension:** Independent cohort və calibration.

**Status:** Əsas implementasiya mövcuddur; layihə README/STATUS-a baxın.

## 18. Protein Contact Map

**Level:** intermediate

**Goal:** Spatial structure üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Spatial structure.

**Research Question:** Sequence-distant residue-lər strukturda yaxındırmı?

**Dataset:** RCSB PDB 1CRN. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Bio.PDB, NumPy.

**Bioinformatics Tools:** Bio.PDB, NumPy; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** chain/residue selection → Cα distances → contacts.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) chain/residue selection mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Distance symmetry, zero diagonal, missing residues. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `protein-contact-map` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Distance symmetry, zero diagonal, missing residues.

**Potential Research Extension:** Predicted vs experimental comparison.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 19. Pathway Enrichment Audit

**Level:** intermediate

**Goal:** Gene-set interpretation üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Gene-set interpretation.

**Research Question:** Fon genlərinin seçimi discovery-ni dəyişirmi?

**Dataset:** Pasilla DE + Reactome gene sets. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, SciPy, Reactome API.

**Bioinformatics Tools:** SciPy, Reactome API; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** ID mapping → measured background → ORA → BH.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) ID mapping mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Matched null/permutation və gene coverage. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `pathway-enrichment-audit` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Matched null/permutation və gene coverage.

**Potential Research Extension:** Ranked enrichment comparison.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 20. Interaction Network Analysis

**Level:** intermediate

**Goal:** Functional associations üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Functional associations.

**Research Question:** Hub sırası evidence threshold-a sabitdirmi?

**Dataset:** STRING species-specific network. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, NetworkX, STRING API.

**Bioinformatics Tools:** NetworkX, STRING API; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** download → evidence filter → centrality → stability.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) download mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Rank correlation və degree-preserving null. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `interaction-network-analysis` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Rank correlation və degree-preserving null.

**Potential Research Extension:** Tissue-specific network.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 21. Cancer Genomics Pipeline

**Level:** advanced

**Goal:** Tumor molecular heterogeneity üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Tumor molecular heterogeneity.

**Research Question:** Purity-adjustment candidate drivers-i dəyişirmi?

**Dataset:** GDC/TCGA open masked somatic calls. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, GDC API, pandas, statistics.

**Bioinformatics Tools:** GDC API, pandas, statistics; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** manifest → sample QC → variants+clinical → stratified analysis.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) manifest mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Donor independence, purity/confounding və multiple tests. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `cancer-genomics-pipeline` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Donor independence, purity/confounding və multiple tests.

**Potential Research Extension:** Multi-omics driver hypothesis.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 22. Disease Gene Discovery

**Level:** advanced

**Goal:** Gene-disease associations üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Gene-disease associations.

**Research Question:** Cross-cohort expression signal təkrarlanırmı?

**Dataset:** GEO studies + GTEx tissue context. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, PyDESeq2, meta-analysis.

**Bioinformatics Tools:** PyDESeq2, meta-analysis; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** cohort QC → within-study effects → meta-analysis → validation.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) cohort QC mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Direction consistency, heterogeneity və external replication. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `disease-gene-discovery` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Direction consistency, heterogeneity və external replication.

**Potential Research Extension:** Perturbation prioritization.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 23. Variant Pathogenicity Prediction

**Level:** advanced

**Goal:** Evidence-based variant ranking üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Evidence-based variant ranking.

**Research Question:** Performance temporal holdout-da saxlanırmı?

**Dataset:** ClinVar dated releases + annotation. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, scikit-learn, VEP.

**Bioinformatics Tools:** scikit-learn, VEP; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** label curation → gene/time split → features → model.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) label curation mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) PR-AUC, calibration, review-status stratification. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `variant-pathogenicity-prediction` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** PR-AUC, calibration, review-status stratification.

**Potential Research Extension:** Functional assay validation.

**Status:** Birinci mərhələ işləkdir: [regional ClinVar evidence triage](advanced/regional-variant-interpretation/README.md) iki versiyalanmış record-u offline yoxlayır. Temporal holdout ML, VEP annotation və PR-AUC mərhələləri hələ protokoldur.

## 24. Drug Response Prediction

**Level:** advanced

**Goal:** Treatment sensitivity üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Treatment sensitivity.

**Research Question:** Model unseen cell-line və drug-larda işləyirmi?

**Dataset:** GDSC public release; licensing yoxlanmalıdır. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, scikit-learn, molecular features.

**Bioinformatics Tools:** scikit-learn, molecular features; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** response QC → drug/cell split → regression → evaluation.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) response QC mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) MAE/RMSE, per-drug correlation və double-cold split. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `drug-response-prediction` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** MAE/RMSE, per-drug correlation və double-cold split.

**Potential Research Extension:** Transcriptome+structure embeddings.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 25. Protein Function Prediction

**Level:** advanced

**Goal:** Unknown protein annotation üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Unknown protein annotation.

**Research Question:** Embeddings homology baseline-ı keçirmi?

**Dataset:** UniProt experimentally supported GO labels. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, ESM embeddings, scikit-learn.

**Bioinformatics Tools:** ESM embeddings, scikit-learn; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** time/cluster split → features → multi-label prediction.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) time/cluster split mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Macro/micro PR-AUC, hierarchy consistency. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `protein-function-prediction` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Macro/micro PR-AUC, hierarchy consistency.

**Potential Research Extension:** Wet-lab test edilə bilən domain hipotezi.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 26. Single-cell RNA-seq Analysis

**Level:** advanced

**Goal:** Cell-state heterogeneity üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Cell-state heterogeneity.

**Research Question:** Treatment effect donor səviyyəsində təkrarlanırmı?

**Dataset:** GEO/10x donor-annotated counts. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Scanpy, Seurat, PyDESeq2.

**Bioinformatics Tools:** Scanpy, Seurat, PyDESeq2; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** cell QC → doublets → annotation → donor pseudobulk → DE.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) cell QC mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Donor-level FDR, cell-type preservation. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `single-cell-rna-seq-analysis` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Donor-level FDR, cell-type preservation.

**Potential Research Extension:** Spatial transcriptomics.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 27. Multi-omics Integration

**Level:** advanced

**Goal:** Complementary molecular views üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Complementary molecular views.

**Research Question:** İki omics modality proqnozu yaxşılaşdırırmı?

**Dataset:** TCGA matched donor expression/methylation. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, MOFA-style models, scikit-learn.

**Bioinformatics Tools:** MOFA-style models, scikit-learn; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** donor intersection → fold-local transform → fusion → test.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) donor intersection mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Modality ablation, external validation, missingness. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `multi-omics-integration` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Modality ablation, external validation, missingness.

**Potential Research Extension:** Mechanistic network integration.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 28. Rare Disease Prioritization

**Level:** advanced

**Goal:** Mendelian disease candidates üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Mendelian disease candidates.

**Research Question:** Phenotype məlumatı variant sırasını yaxşılaşdırırmı?

**Dataset:** ClinVar public examples + HPO; controlled patient data yox. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, VEP, HPO ontology.

**Bioinformatics Tools:** VEP, HPO ontology; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** quality → inheritance → phenotype match → evidence ranking.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) quality mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Recall@k, gene holdout, evidence provenance. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `rare-disease-prioritization` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Recall@k, gene holdout, evidence provenance.

**Potential Research Extension:** Trio analysis və long-read SV.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 29. Metagenomic Novel Taxa

**Level:** advanced

**Goal:** Unknown community members üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Unknown community members.

**Research Question:** Database-də olmayan taxa necə aşkar edilir?

**Dataset:** ENA mock communities, dated reference DB. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, Kraken2, Bracken.

**Bioinformatics Tools:** Kraken2, Bracken; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** read QC → classify → confidence sweep → unknown detection.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) read QC mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Species precision/recall, abundance error, contamination controls. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `metagenomic-novel-taxa` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Species precision/recall, abundance error, contamination controls.

**Potential Research Extension:** Strain-resolved assembly.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.

## 30. Microbiome Association Study

**Level:** advanced

**Goal:** Community/disease association üçün təkrar işlədilə bilən analiz qurmaq.

**Biological Problem:** Community/disease association.

**Research Question:** Cohort və antibiotic kovariatından sonra signal qalırmı?

**Dataset:** Public curated microbiome study + metadata. Dəqiq accession/versiya, ölçü və şərtlər icradan əvvəl dataset kartında saxlanır.

**Tech Stack:** Python, QIIME2, compositional statistics.

**Bioinformatics Tools:** QIIME2, compositional statistics; alətlərin rolu və versiyası run manifest-də yazılır.

**Pipeline:** QC → taxa table → prevalence → compositional model → validation.

**Implementation Steps:** (1) Dataset və biological unit-i doğrula. (2) QC mərhələsini hazırla. (3) Aralıq cədvəlləri və QC-ni saxlayaraq pipeline-nı tamamla. (4) Effect CI, FDR, leave-study-out performance. (5) Nəticə, uncertainty və məhdudiyyətləri yaz.

**Expected Output:** `microbiome-association-study` üçün versioned run manifest, analiz cədvəli, qrafik və Markdown interpretasiya; əvvəlcədən gözlənən “müsbət” nəticə yoxdur.

**Evaluation:** Effect CI, FDR, leave-study-out performance.

**Potential Research Extension:** Longitudinal perturbation study.

**Status:** Layihə ideyası/protokol; tamamlanmış implementasiya kimi sayılmır.
