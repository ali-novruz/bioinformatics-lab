# Khan: dörd sinifli mikroarray benchmark

## Mənbə

Khan J. və b., 2001. *Classification and diagnostic prediction of cancers using gene expression profiling and artificial neural networks*. Nature Medicine 7, 673-679. Bu repo məqalənin neural network nəticələrinin reproduksiyası deyil; fərqli SVM tədris analizidir.

Fayllar dərslik müəlliflərinin [ISLP deposundan](https://github.com/intro-stat-learning/ISLP/tree/a1f4e43ca88d4c9a6f186930181d628b9270015d/ISLP/data) götürülür. [Dataset izahı](https://github.com/intro-stat-learning/ISLP/blob/a1f4e43ca88d4c9a6f186930181d628b9270015d/docs/jupyterbook/datasets/Khan.md). Sabit revision: `a1f4e43ca88d4c9a6f186930181d628b9270015d`. Dörd CSV üçün URL, ölçü və SHA-256 [manifestdə](../khan-manifest.json) saxlanılır.

| Sahə | Dəyər |
|---|---|
| Bioloji mövzu | Kiçik yumru mavi hüceyrəli şişlərin dörd sinfi |
| Training | 63 nümunə; sinif 1/2/3/4 sayları 8/23/12/20 |
| Test | 20 nümunə; sinif sayları 3/6/6/5 |
| Xüsusiyyət | 2308 əvvəlcədən emal edilmiş mikroarray sütunu |
| Qiymətlər | Davamlı ifadə; mənfi qiymətlər mümkündür; raw RNA-seq counts deyil |
| Bölünmə | ISLP tərəfindən verilən train/test saxlanılır |
| Saxlama | CSV-lər ilk icrada endirilir, Git-ə daxil edilmir |

Sinif adları və prob annotasiyası [`scripts/build_khan_annotation.py`](../../scripts/build_khan_annotation.py) ilə CRAN `plsgenomics` 1.5-3 `SRBCT` məlumatına ədədi uyğunlaşdırma yolu ilə təsdiqlənib: 1 = BL, 2 = EWS, 3 = NB, 4 = RMS. `Vj` sütunu SRBCT-nin j-ci geninə uyğundur; IMAGE klon ID-si və təsviri [`datasets/annotations/`](../annotations/) daxilindədir. Təsvirlər 2001-ci il annotasiyasıdır, müasir HGNC simvolu deyil. Mövcud kanonik qrafiklər tarixi səbəbdən 1-4 saxlayır. Bu versiyanın 20 test nümunəsi orijinal məqalənin bütün cohort-u kimi göstərilmir. Mənbədən əvvəlki preprocessing-in split-dən müstəqil olub-olmadığı burada yoxlanmayıb.

## İstifadə və məhdudiyyət

Mənbə açıq endirmə üçün əlçatandır; dataset-ə ayrıca hüquq iddiası edilmir və proqram təminatının lisenziyası avtomatik olaraq bioloji data lisenziyası sayılmır. İlkin müəlliflərə istinad saxlanılır. Əlavə klinik, kommersiya və ya yenidən yayım istifadəsi üçün mənbə şərtləri ayrıca qiymətləndirilməlidir.

Bu tarixi benchmark müasir xəstə populyasiyasında diaqnoz, skrininq və ya erkən aşkarlama validasiyası deyil. [Layihənin nəticə və limitləri](../../projects/intermediate/gene-expression-ml/README.md).
