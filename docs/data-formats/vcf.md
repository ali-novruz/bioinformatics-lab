# VCF: variant qeydini düzgün oxumaq

VCF referens koordinatı, allellər, filter, annotasiya və sample genotiplərini saxlayır. Parser-in faylı qəbul etməsi variantın bioloji və ya klinik baxımdan doğru olması demək deyil. Rəsmi tərif [GA4GH VCF spesifikasiyasıdır](https://github.com/samtools/hts-specs/blob/master/VCFv4.5.pdf).

```vcf
##fileformat=VCFv4.3
##contig=<ID=chr1,length=1000>
##FILTER=<ID=LowQual,Description="QUAL below threshold">
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total depth">
##INFO=<ID=AF,Number=A,Type=Float,Description="ALT allele frequency">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=AD,Number=R,Type=Integer,Description="Allele depths">
#CHROM POS ID REF ALT QUAL FILTER INFO FORMAT sample_A sample_B
chr1 101 rsToy1 A G 60 PASS DP=31;AF=0.42 GT:AD 0/1:9,8 0/0:14,0
chr1 205 . T TA 45 PASS DP=22;AF=0.23 GT:AD 0/1:8,4 0/0:10,0
chr1 310 . C A,G 70 PASS DP=40;AF=0.20,0.10 GT:AD 1/2:12,8,4 0/1:9,7,0
chr1 420 . AT A . LowQual DP=9;AF=0.11 GT:AD 0/1:5,1 ./.:.
```

Real VCF sütunları tab ilə ayrılır. `POS` 1-based-dir; `FILTER=.` test edilməmiş qeyd ola bilər və `PASS` deyil. `Number=A` hər ALT, `R` REF+ALT, `G` mümkün genotiplər üçün dəyər deməkdir. İki ALT-li sətirdə AF iki, AD üç elementlidir.

| Sahə | Yoxlama |
|---|---|
| CHROM/POS | assembly, contig lüğəti, 1-based koordinat |
| REF/ALT | FASTA ilə REF uyğunluğu, strand, normalization |
| QUAL/FILTER | caller-ə məxsus məna; missing ilə PASS ayrılır |
| INFO/FORMAT | header-də Type və Number; trailing missing sahələr |
| GT | phased `|`, unphased `/`, missing `.` və allele index |

Multi-allelic `C→A,G` qeydini parçalayanda `Number=A/R/G` sahələri və genotiplər yenidən yazılmalıdır. Indel-lər parsimonious və left-aligned olmalıdır.

```bash
bcftools norm --check-ref w --fasta-ref reference.fa --multiallelics -both input.vcf.gz -Oz -o normalized.vcf.gz
bcftools index --tbi normalized.vcf.gz
bcftools stats normalized.vcf.gz > normalized.stats.txt
```

Repo parser-i dərs subset-i üçün başlıq, sahə sayı, QUAL, FORMAT və allele index-i yoxlayır:

```python
from biolab.io import read_vcf
for record in read_vcf("datasets/fixtures/toy.vcf"):
    print(record["chrom"], record["pos"], record["ref"], record["alts"])
```

Tez səhvlər: assembly-ni yazmamaq; `./.`-ni `0/0` saymaq; çoxallelli qeydi kor-koranə bölmək; REF mismatch-i səssiz düzəltmək; ClinVar significance-i condition, review status və tarixsiz ground truth saymaq. Minimum QC-də variant/allele sayı, filter/type bölgüsü, missing genotype, sample unikallığı və normalization-dan əvvəl/sonra fərq saxlanır.
