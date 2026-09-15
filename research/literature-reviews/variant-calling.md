# Variant Calling Methods

**Scope:** məqsədli mini-review, systematic review deyil. 2026-09-15-də hazırlanıb; seçilmiş seminal mənbələrlə məhduddur.

## Ümumi yanaşma
Reads align edilir, variant candidates və genotypes infer edilir, sonra normalized truth-set comparison aparılır.
## Metod fərqləri
BWA mapping, GATK framework, DeepVariant learning-based genotyping fərqli pipeline qatlarıdır; onları tək alternativlər kimi sıralamaq yanlışdır.
## Nəticələr və görünən ziddiyyətlər
BWA nəticəsi mapping; GATK2010 arxitektura; DeepVariant abstract variant-call üstünlüyü bildirir. Müxtəlif data və qiymətləndirməyə görə bu məqalələrdən vahid leaderboard qurulmur.
## Problemlər
Reference bias, repeats, indel representation, difficult regions, model/platform transfer.
## Research gap və növbəti eksperiment
Eyni reads, referens və confident region daxilində mapper×caller factorial experiment; F1 ilə yanaşı stratified error.
## Sübut sərhədi
Bu gap-lər həmin mənbələrdən çıxarılan laboratoriya təklifləridir; ədəbiyyatda heç kimin araşdırmadığı yeni mövzu kimi iddia edilmir. Yeni layihədən əvvəl daha geniş və tarixlə məhdudlaşdırılmış axtarış tələb olunur.
## Mənbələr
- [bwa](../papers/bwa.md)
- [gatk](../papers/gatk.md)
- [deepvariant](../papers/deepvariant.md)
