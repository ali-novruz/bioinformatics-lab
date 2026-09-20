# 24 tapşırıq

Əvvəl [praktikumu](../handbook.md) oxuyun. Hər mərhələdə cavaba baxmadan üç sualı həll edin. Kodlu tapşırıqda əmr, nəticə və şərhi birlikdə saxlayın.

## 1. Məlumat

1. `sample_id=17`, `condition=treated`, `count=0` dəyişənlərini təsnif edin.
2. Metadata sırası tərsinə çevrilsə, cədvəllər necə birləşdirilməlidir?
3. Eyni SHA-256 elmi doğruluğu sübut edirmi?

**Özünü yoxla:** [ ] identifikatoru ölçüdən ayırdım · [ ] açarla join etdim · [ ] checksum-un sərhədini yazdım

## 2. SQL

4. 124 gen və 6 nümunənin tam ölçmə cədvəlində neçə qeyd olar?
5. Eyni `(sample_id, gene_id)` cütünü yenidən yazmaq hansı qaydanı pozur?
6. `count=-1` və `count=1.5` raw count kimi qəbul edilməlidirmi?

**Özünü yoxla:** [ ] gözlənən sətir sayını hesabladım · [ ] primary key-i göstərdim · [ ] data tipini əsaslandırdım

## 3. Maşın öyrənməsi

7. Feature selection bütün data-da CV-dən əvvəl edilsə nə baş verir?
8. Recall-lar 1, 5/6, 1, 1 olduqda balanced accuracy-ni hesablayın.
9. Test nəticəsinə baxıb hiperparametrləri dəyişdikdə nə itirilir?

**Özünü yoxla:** [ ] leakage mənbəyini tapdım · [ ] hesabı göstərdim · [ ] untouched test rolunu izah etdim

## 4. Genetika

10. VCF `0/1` ilə `0|1` arasındakı fərq nədir?
11. REF alleli həmişə sağlam alleldirmi?
12. Poligenlik və pleiotropiyanı ayırın.

**Özünü yoxla:** [ ] fazanı izah etdim · [ ] referenslə klinik şərhi ayırdım · [ ] iki anlayışa nümunə verdim

## 5. Ardıcıllıq axtarışı

13. Nukleotid sorğunu tərcümə edib protein bazasında hansı proqram axtarır?
14. 100% identity, 12 nt alignment gen funksiyasını sübut edirmi?
15. BLAST score 200 olduqda alignment 200 bp olmalıdırmı?

**Özünü yoxla:** [ ] proqramı düzgün seçdim · [ ] coverage-i yoxladım · [ ] score və uzunluğu ayırdım

## 6. Statistika

16. 1000 kalibrə edilmiş həqiqi null testdə `alpha=0.05` üçün gözlənilən yanlış müsbət sayı nədir?
17. `p=0.03` H0-ın doğru olma ehtimalının 3% olduğunu bildirirmi?
18. Bir simulyasiyada BH-dən sonra sıfır nəticə qalması ümumi zəmanətdirmi?

**Özünü yoxla:** [ ] gözlənilən sayı hesabladım · [ ] p-value-ni şərti ehtimal kimi yazdım · [ ] FDR zəmanətini düzgün məhdudlaşdırdım

## 7. Təkrar icra

19. NumPy `a*b` və `a@b` nə ilə fərqlənir?
20. Seed eyni olsa da paket versiyası dəyişsə nəticə dəyişə bilərmi?
21. İki run qovluğunun adı fərqli, xülasələri eynidir. Bu uyğunsuzluqdurmu?

**Özünü yoxla:** [ ] operatorları test etdim · [ ] mühit versiyasını qeyd etdim · [ ] run kimliyi ilə elmi nəticəni ayırdım

## 8. Elmi iddia

22. 20 şiş toxumasında 95% accuracy erkən xərçəng skrininqini təsdiqləyirmi?
23. `V17` ən yaxşı xüsusiyyətdirsə onu gen biomarkeri adlandırmaq olarmı?
24. U4247-dəki miRNA xülasəsini ilkin məqalə reproduksiyası saymaq olarmı?

**Özünü yoxla:** [ ] populyasiya sərhədini yazdım · [ ] feature annotasiyasını yoxladım · [ ] xülasə ilə reproduksiyanı ayırdım

Bitirdikdən sonra [cavab və izahlara](../solutions/README.md) keçin.
