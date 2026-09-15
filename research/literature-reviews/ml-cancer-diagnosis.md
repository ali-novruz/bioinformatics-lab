# Machine Learning for Cancer Diagnosis

**Scope:** məqsədli mini-review, systematic review deyil. 2026-09-15-də hazırlanıb; seçilmiş seminal mənbələrlə məhduddur.

## Ümumi yanaşma
Morphology və molecular feature-lərdən supervised classification; regularized linear baseline və nonlinear ansambllar.
## Metod fərqləri
WDBC morphology ilə gene-expression cohort nəticəsini birbaşa müqayisə etmək olmaz. Train-only CV və prospective external validation fərqli sübut səviyyələridir.
## Nəticələr və görünən ziddiyyətlər
Repo WDBC-də yüksək internal AUROC əldə edir; müstəqil klinik cohort test edilmədiyi üçün clinical usefulness nəticəsi çıxarılmır. TCGA-CDR label tərifinin model qədər vacib olduğunu göstərir.
## Problemlər
Case-mix, hospital leakage, class imbalance, calibration və verification bias.
## Research gap və növbəti eksperiment
Eyni preprocess ilə external test; decision threshold-u validation set-də əvvəlcədən seçmək.
## Sübut sərhədi
Bu gap-lər həmin mənbələrdən çıxarılan laboratoriya təklifləridir; ədəbiyyatda heç kimin araşdırmadığı yeni mövzu kimi iddia edilmir. Yeni layihədən əvvəl daha geniş və tarixlə məhdudlaşdırılmış axtarış tələb olunur.
## Mənbələr
- [tcga-cdr](../papers/tcga-cdr.md)
