# FASTQ

## Struktur
Hər read üçün 4 sətir: @ID, sequence, +, ASCII keyfiyyət. Burada Phred+33 qəbul edilir.

## Nümunə
```text
@r1
ACGT
+
IIII
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
Sequencing QC, adapter trimming, mapping.

## Üstünlük və məhdudiyyət
Hər baza üçün keyfiyyət verir. Tarixi encoding-lər fərqlənir; sequence və quality uzunluğu eyni olmalıdır. Q=-10log10(Perror); Q30 üçün Perror=0.001.

## Python ilə oxuma
```python
from Bio import SeqIO
for r in SeqIO.parse("reads.fq", "fastq"):
    print(r.id, r.letter_annotations["phred_quality"])
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://www.ncbi.nlm.nih.gov/sra/docs/submitformats/).
