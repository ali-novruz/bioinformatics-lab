# BED

## Struktur
İlk 3 sahə chrom, chromStart, chromEnd; 0-based, half-open [start,end). 3–12 standart sütun.

## Nümunə
```text
toy	0	10	region1	0	+
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
Region overlap, peaks, browser track.

## Üstünlük və məhdudiyyət
Sadə və interval hesablamaları rahatdır. BED [0,10) uzunluğu 10-dur; GFF 1..10 eyni intervaldır. BED12 block strukturu ayrıca parse tələb edir.

## Python ilə oxuma
```python
import pandas as pd
df = pd.read_csv("regions.bed", sep="\t", header=None)
assert (df[2] > df[1]).all()
print(df[2] - df[1])
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://genome.ucsc.edu/FAQ/FAQformat.html#format1).
