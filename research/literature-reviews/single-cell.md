# Single-cell RNA Sequencing

**Scope:** məqsədli mini-review, systematic review deyil. 2026-09-15-də hazırlanıb; seçilmiş seminal mənbələrlə məhduddur.

## Ümumi yanaşma
Cell QC, doublets, normalization, dimension reduction, annotation və donor-aware differential testing.
## Metod fərqləri
Seurat anchors data inteqrasiyası/transfer üçündür; donor pseudobulk population-level inference üçün fərqli qatdır.
## Nəticələr və görünən ziddiyyətlər
Seurat3 integration nümunələri mixing və biological structure arasında kompromisi göstərir. UMAP-da daha çox mixing avtomatik daha doğru biological result deyil.
## Problemlər
Rare states, doublets, dissociation effects, pseudoreplication və overcorrection.
## Research gap və növbəti eksperiment
Leave-donor-out annotation və raw-count pseudobulk nəticəsinin anchor threshold-a həssaslığı.
## Sübut sərhədi
Bu gap-lər həmin mənbələrdən çıxarılan laboratoriya təklifləridir; ədəbiyyatda heç kimin araşdırmadığı yeni mövzu kimi iddia edilmir. Yeni layihədən əvvəl daha geniş və tarixlə məhdudlaşdırılmış axtarış tələb olunur.
## Mənbələr
- [seurat](../papers/seurat.md)
- [deseq2](../papers/deseq2.md)
