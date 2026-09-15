# VCF

## Struktur
## metadata, #CHROM header; CHROM POS ID REF ALT QUAL FILTER INFO; varsa FORMAT və sample sütunları. POS 1-based-dir.

## Nümunə
```text
##fileformat=VCFv4.2
##contig=<ID=toy,length=100>
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO
toy	5	.	A	G	50	PASS	.
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
SNV/indel/SV annotasiyası və genotip analizi.

## Üstünlük və məhdudiyyət
Referens və alternativ allel, keyfiyyət və sample genotipi eyni yerdədir. Multi-allelic normalization, left alignment və reference build vacibdir. QUAL=. itkindir; FILTER=. test edilməyib, PASS deyil.

## Python ilə oxuma
```python
import pysam
with pysam.VariantFile("variants.vcf") as f:
    for v in f:
        print(v.contig, v.pos, v.ref, v.alts)
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://samtools.github.io/hts-specs/).
