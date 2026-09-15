# RNA-Seq Analysis Methods

**Scope:** məqsədli mini-review, systematic review deyil. 2026-09-15-də hazırlanıb; seçilmiş seminal mənbələrlə məhduddur.

## Ümumi yanaşma
Quantification və differential testing bir-birini izləyən fərqli metodlardır.
## Metod fərqləri
Salmon abundance və bias modelini, DESeq2 count dispersion və condition effect-ni hədəfləyir. STAR+counts və Salmon+aggregation yolları da assay-a uyğun qurulur.
## Nəticələr və görünən ziddiyyətlər
Salmon biased və ideal simulyasiyalarda metod fərqinin dəyişdiyini göstərir; DESeq2 effect estimates-in qeyri-sabitliyinə shrinkage tətbiq edir. “Ən çox DE gen” ən yaxşı metod meyarı deyil.
## Problemlər
Annotation release, library type, low counts, batch və small n.
## Research gap və növbəti eksperiment
Quantifier dəyişəndə effect direction və FDR sabitliyini, null control false calls ilə birlikdə yoxlamaq.
## Sübut sərhədi
Bu gap-lər həmin mənbələrdən çıxarılan laboratoriya təklifləridir; ədəbiyyatda heç kimin araşdırmadığı yeni mövzu kimi iddia edilmir. Yeni layihədən əvvəl daha geniş və tarixlə məhdudlaşdırılmış axtarış tələb olunur.
## Mənbələr
- [deseq2](../papers/deseq2.md)
- [salmon](../papers/salmon.md)
