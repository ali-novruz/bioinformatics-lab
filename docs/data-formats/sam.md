# SAM

## Struktur
Header @HD/@SQ; tab-separated 11 məcburi sahə: QNAME FLAG RNAME POS MAPQ CIGAR RNEXT PNEXT TLEN SEQ QUAL.

## Nümunə
```text
@HD	VN:1.6	SO:unsorted
@SQ	SN:toy	LN:100
r1	0	toy	1	60	4M	*	0	0	ACGT	IIII
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
Read alignment, splice junction, coverage.

## Üstünlük və məhdudiyyət
İnsan tərəfindən oxunur; tag-lar genişlənir. Böyükdür; FLAG bitmask-dır. POS 1-based, pysam reference_start 0-based-dir. M match və mismatch ola bilər.

## Python ilə oxuma
```python
import pysam
with pysam.AlignmentFile("reads.sam", "r") as f:
    for r in f:
        print(r.query_name, r.reference_start, r.cigarstring)
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://samtools.github.io/hts-specs/).
