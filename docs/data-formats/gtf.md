# GTF

## Struktur
9 sütun; attributes gene_id "..."; transcript_id "..."; şəklindədir. Koordinatlar 1-based inclusive.

## Nümunə
```text
toy	demo	exon	1	30	.	+	.	gene_id "g1"; transcript_id "t1";
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
RNA-seq exon/gene counting və transkript modelləri.

## Üstünlük və məhdudiyyət
STAR/featureCounts kimi alətlərlə geniş uyğunluq. Annotasiya release və referens uyğun gəlməlidir; attribute-ları boşluğa görə kor-koranə bölməyin.

## Python ilə oxuma
```python
import pandas as pd
df = pd.read_csv("genes.gtf", sep="\t", comment="#", header=None)
print(df[df[2] == "exon"][[0,3,4,8]])
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://www.ensembl.org/info/website/upload/gff.html).
