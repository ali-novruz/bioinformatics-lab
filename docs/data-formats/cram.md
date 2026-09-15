# CRAM

## Struktur
Reference-based və digər encoding-lərlə sıxılan alignment konteyneri.

## Nümunə
```text
samtools view -C -T reference.fa -o reads.cram reads.bam
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
Böyük sequencing arxivləri.

## Üstünlük və məhdudiyyət
Bir çox ssenaridə BAM-dan az yer tutur. Decode üçün uyğun referens çox vaxt lazımdır; checksum/reference versiyası saxlanmalıdır. Embedded reference rejimləri də var.

## Python ilə oxuma
```python
import pysam
with pysam.AlignmentFile("reads.cram", "rc", reference_filename="reference.fa") as f:
    print(next(f).query_name)
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://samtools.github.io/hts-specs/).
