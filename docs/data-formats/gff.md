# GFF

## Struktur
Burada GFF3: 9 sütun, son sahə ID=...;Parent=... attributlarıdır. Start/end 1-based inclusive.

## Nümunə
```text
##gff-version 3
toy	demo	gene	1	90	.	+	.	ID=g1
toy	demo	mRNA	1	90	.	+	.	ID=t1;Parent=g1
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
Gene, exon, CDS və feature iyerarxiyası.

## Üstünlük və məhdudiyyət
Çox feature tipi və parent əlaqələri. GFF2 və GFF3 qarışdırılmamalıdır; URL-escaped attributes və ##FASTA bölməsi sadə split parserini poza bilər.

## Python ilə oxuma
```python
import pandas as pd
# Yalnız annotation bölməsi olan sadə GFF3 üçün:
df = pd.read_csv("annotation.gff3", sep="\t", comment="#", header=None)
print(df.iloc[:, [0,2,3,4]])
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md).
