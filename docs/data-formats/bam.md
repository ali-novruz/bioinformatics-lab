# BAM

## Struktur
SAM-ın BGZF-sıxılmış binary təqdimatı. Hex və ya adi text faylı deyil.

## Nümunə
```text
SAM nümunəsini çevirmək: samtools view -b -o reads.bam reads.sam
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
Coverage, variant calling, IGV.

## Üstünlük və məhdudiyyət
Kompakt və indeksli region sorğuları. Region fetch üçün coordinate-sort və BAI/CSI lazımdır; böyük contig-lərdə CSI seçin.

## Python ilə oxuma
```python
import pysam
with pysam.AlignmentFile("reads.bam", "rb") as f:
    for r in f.fetch(until_eof=True):
        print(r.query_name)
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://samtools.github.io/hts-specs/).
