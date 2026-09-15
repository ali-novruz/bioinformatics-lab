# Proteomics

### Sequence-dən funksiyaya
Protein family təkamül əlaqəsi, domain isə struktur/funksional modul anlayışıdır. Qısa motif təsadüfən də yarana bilər; domain HMM-ləri və homology coverage daha geniş sübut verir. Sequence identity yüksək olsa da active-site dəyişməsi funksiyanı dəyişə bilər.

### Mass spectrometry
MS1 precursor ionları, MS2 fragmentləri ölçür. Peptide-spectrum matching axtarış bazasına və scoring-ə bağlıdır. Target-decoy yanaşması PSM/peptide/protein səviyyəsində FDR üçün işlənir; bu səviyyələr eyni deyil. Shared peptides protein inference-ni çətinləşdirir. Missing protein intensity avtomatik sıfır deyil.

### Annotation və interaction
UniProt reviewed/unreviewed status, evidence və version saxlanmalıdır. STRING score funksional association sübutudur; bütün kənarlar birbaşa fiziki binding demək deyil. PDB strukturundakı chain sequence prekursorun hamısı olmaya bilər.

### Praktika
`python scripts/protein_project.py` P01308 insulin FASTA-sını və 1CRN crambin strukturunu ayrı nümunələr kimi analiz edir. Bunlar eyni protein deyil; struktur və sequence pipeline-larını nümayiş etdirir. UniProt-dan uzunluq/kompozisiya, PDB-dən Cα contact map və chain xülasəsi çıxarılır.

### Araşdırma
Problem: funksiya etiketləri natamamdır. Metod: homology+domain+ML. Zəiflik: homologların train/test arasında qalması. Data: UniProt evidence-supported annotations. Eksperiment: sequence-cluster split; metric: macro-F1 və annotation coverage. Yeni sual: uzaq homologlarda hansı domain səhvləri proqnozu pozur?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://www.uniprot.org/help). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
