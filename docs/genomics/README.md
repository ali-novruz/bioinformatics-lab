# Genomics: sequencing-dən interpretasiyaya

### Sequencing, assembly və referens
Short reads baza dəqiqliyi və xərc baxımından faydalıdır; long reads təkrar region və structural variation üçün əlavə əlaqə verir. De novo assembly çox vaxt de Bruijn graph və ya overlap ideyalarını istifadə edir. N50 contiguity ölçüsüdür, düzgünlük sübutu deyil; completeness, contamination və misassembly də yoxlanmalıdır. Linear reference bir kohortu tam təmsil etmir; pangenome alternativ allelləri nəzərə alır.

### Variant pipeline
FASTQ → FastQC/MultiQC → lazım olduqda Cutadapt → BWA/uyğun aligner → sort/index BAM → caller → normalize VCF → annotasiya → biological interpretation. Adapter problemi yoxdursa kor-koranə trimming faydasız ola bilər. Read groups, sample ID, ploidy və duplicate strategiyası assay-a uyğun seçilməlidir.

### Variant sinifləri
SNV/SNP, kiçik indel, structural variant və copy-number eyni caller ilə eyni keyfiyyətdə tutulmur. Repeat və paralog regionlarda mapping ambiguity yüksəkdir. Truth-set precision/recall yalnız qiymətləndirilən confident regionlarda hesablanmalıdır.

### Populyasiya və müqayisəli genomika
PCA ancestry strukturunu aşkar edə bilər; GWAS-da relatedness, ancestry və multiple testing nəzərə alınır. Assosiasiya causal variantı sübut etmir; LD qonşu markerləri əlaqələndirir. Comparative genomics-də ortholog ilə paralog fərqini qoruyun.

### Pharmacogenomics və cancer genomics
Drug response çox allelli haplotiplər, copy-number və populyasiya konteksti tələb edə bilər. Tumor purity, heterogeneity, normal contamination və paired-normal dizayn somatik çağırışlarda vacibdir. Bu repo klinik interpretasiya sistemi deyil.

### Araşdırma
Problem: reference bias; mövcud yanaşma graph reference; zəiflik: resurs və benchmark uyğunluğu. Data: GIAB confident regions. Eksperiment: mapping/caller-i ayrı-ayrı dəyişib precision/recall və runtime ölçün. Yeni sual: indel uzunluğu artdıqca səhv hansı mərhələdən gəlir?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://samtools.github.io/bcftools/howtos/variant-calling.html). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
