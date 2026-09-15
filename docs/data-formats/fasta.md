# FASTA

## Struktur
`>` ilə başlayan başlıq, sonra bir və ya çox sətir sequence. Başlığın ilk sözü çox alətdə ID-dir.

## Nümunə
```text
>toy_dna
ATGCGTNN
ACGT
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
Referens, protein və transkript ardıcıllığı.

## Üstünlük və məhdudiyyət
Sadə, oxunaqlı, streaming üçün uyğundur. Read keyfiyyəti saxlamır; əlifba və unikal ID ayrıca yoxlanır.

## Python ilə oxuma
```python
from Bio import SeqIO
for record in SeqIO.parse("input.fa", "fasta"):
    print(record.id, len(record.seq))
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://www.ncbi.nlm.nih.gov/genbank/fastaformat/).
