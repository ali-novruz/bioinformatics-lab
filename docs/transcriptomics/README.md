# RNA-seq və transcriptomics

### Məlumatın mənası
RNA-seq oxunuşları ekspressiyanın qeyri-bərabər, library size və texniki bias-a bağlı nümunəsidir. Raw integer counts, normalized counts, CPM və TPM fərqli obyektlərdir. TPM transkript uzunluğunu nəzərə alır, DESeq2-yə raw counts əvəzinə verilmir.

### Xam data yolu
FASTQ → QC → STAR/HISAT2 ilə splice-aware alignment + gene counting və ya Salmon ilə transcript quantification → uyğun transcript-to-gene aggregation → count matrix → model. Strandness və genome/annotation release uyğunsuzluğu bütün analizi dəyişə bilər. Salmon estimate-ləri üçün tximport kimi uyğun yol seçin; fractional count-ları təsadüfi yuvarlaqlaşdırmayın.

### Statistika
DESeq2 count-ları negative binomial model ilə təhlil edir; dispersion shrinkage kiçik replikatlarda sabitliyə kömək edir. Pasilla layihəsində design `~ type + condition`, contrast treated/untreated-dir. Filtr qrup nəticələrinə baxmadan ümumi sayımla seçilir. FDR<0.05 və |log2FC|>1 ayrı threshold-lardır; ikincisi effekti vurğulayır, yeni FDR sübutu deyil.

### Vizual yoxlama
PCA və clustering üçün log-normalized counts və ya VST istifadə edilir. Buradakı PCA log1p normalized counts-dur, VST deyil. Heatmap üçün əvvəlcədən müəyyən edilmiş variable genes seçilir. Volcano -log10(adjusted p)-ni göstərir; missing adjusted p sıfıra çevrilmir.

### Pathway
ORA fon dəsti bütün genom deyil, test edilə bilən genlər olmalıdır. Ranked enrichment üçün sign və ID mapping tutarlı saxlanır. Gene set overlap və annotation bias nəticəni gücləndirə bilər.

### Araşdırma
Problem: gene-level bolluq splicing-i gizlədir. Data: pasilla. Eksperiment: `~condition` və `~type+condition` modelinin həssaslıq müqayisəsi; əsas modeli əvvəlcədən seçin. Yeni sual: exon usage dəyişməsi gene-level nəticəsiz regionlarda görünürmü?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://pmc.ncbi.nlm.nih.gov/articles/PMC4302049/). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
