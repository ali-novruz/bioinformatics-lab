# Metagenomics

**Scope:** məqsədli mini-review, systematic review deyil. 2026-09-15-də hazırlanıb; seçilmiş seminal mənbələrlə məhduddur.

## Ümumi yanaşma
Taxonomic read classification, assembly/binning və functional annotation complementary yanaşmalardır.
## Metod fərqləri
Kraken2 nucleotide minimizers sürət/yaddaş üçün; translated search uzaq viral homologlarda əlavə sensitivity verə bilər. Assembly daha uzun kontekst verir, coverage tələbi artır.
## Nəticələr və görünən ziddiyyətlər
Kraken2 benchmark-ları clade exclusion və müxtəlif reference əhatəsini nəzərə alır. Database-dəki taxa-ya yaxınlığın fərqi method ranking-i dəyişə bilər.
## Problemlər
Reference contamination, unknown species, host contamination və database version.
## Research gap və növbəti eksperiment
Mock community-də species exclusion; precision/recall ilə yanaşı unknown rejection və RAM/runtime.
## Sübut sərhədi
Bu gap-lər həmin mənbələrdən çıxarılan laboratoriya təklifləridir; ədəbiyyatda heç kimin araşdırmadığı yeni mövzu kimi iddia edilmir. Yeni layihədən əvvəl daha geniş və tarixlə məhdudlaşdırılmış axtarış tələb olunur.
## Mənbələr
- [kraken2](../papers/kraken2.md)
