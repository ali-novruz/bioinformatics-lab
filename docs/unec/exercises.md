# Tapşırıqlar və cavablar

Materiallar tələbənin əvvəlcə müstəqil işləməsi üçün ayrılıb:

- [24 tapşırıq və mərhələ yoxlamaları](exercises/README.md)
- [Müəllim üçün cavablar və izahlar](solutions/README.md)

Arxivdəki aşağıdakı birləşik versiya geriyə uyğun keçid üçün saxlanılır.

Əvvəl [praktikumu](handbook.md) oxuyun. Hər bölmənin üç sualını cavaba baxmadan həll edin. Kodlu tapşırıqlarda nəticə və izahı birlikdə saxlayın.

## 1. Məlumat

1. `sample_id=17`, `condition=treated`, `count=0` dəyişənlərini təsnif edin.
2. Metadata-nın sırası tərsinə çevrilsə, cədvəllər necə birləşdirilməlidir?
3. Eyni SHA-256 elmi doğruluğu sübut edirmi?

**Cavablar:** 1) ID, kateqoriya, tam sayım. 2) `sample_id` üzrə; sıra üzrə deyil. 3) Xeyr, yalnız bayt uyğunluğunu yoxlamağa kömək edir. Mənbə və metod ayrıca qiymətləndirilir.

## 2. SQL

4. 124 gen və 6 nümunənin tam ölçmə cədvəlində neçə qeyd olar?
5. Eyni `(sample_id, gene_id)` cütünü yenidən yazmaq hansı qaydanı pozur?
6. `count=-1` və `count=1.5` qəbul edilməlidirmi?

**Cavablar:** 4) 744. 5) Birləşmiş əsas açarı. 6) Raw count cədvəlində hər ikisi rədd edilməlidir; TPM üçün başqa sxem qurulur.

## 3. Maşın öyrənməsi

7. Feature selection bütün data-da CV-dən əvvəl edilsə nə baş verir?
8. Recall-lar 1, 5/6, 1, 1 olduqda balanced accuracy-ni hesablayın.
9. Test nəticəsinə baxıb hiperparametrləri dəyişdikdə nə itirilir?

**Cavablar:** 7) Validation məlumatı seçimə sızır; score optimist ola bilər. 8) 23/24 = 0.95833. 9) Testin müstəqil son qiymətləndirmə rolu; yeni untouched data lazımdır.

## 4. Genetika

10. VCF `0/1` ilə `0|1` arasındakı fərq nədir?
11. REF alleli həmişə sağlam alleldirmi?
12. Poligenlik və pleiotropiyanı ayırın.

**Cavablar:** 10) İkincidə faza məlumatı göstərilir. 11) Xeyr, REF referens ardıcıllığın allelidir. 12) Çox gen → bir xüsusiyyət; bir gen → bir neçə xüsusiyyət.

## 5. Sequence axtarışı

13. Nukleotid sorğunu tərcümə edib protein bazasında hansı proqram axtarır?
14. 100% identity, 12 nt alignment gen funksiyasını sübut edirmi?
15. BLAST score 200 olduqda alignment 200 bp olmalıdırmı?

**Cavablar:** 13) BLASTX. 14) Xeyr; coverage, təsadüfi uyğunluq və digər sübutlar lazımdır. 15) Xeyr; score və uzunluq müxtəlif ölçülərdir.

## 6. Statistika

16. 1000 kalibrə edilmiş həqiqi null testdə alfa=0.05 üçün gözlənilən yanlış müsbət sayı?
17. `p=0.03` H0-ın doğru olma ehtimalının 3% olduğunu bildirirmi?
18. Bu simulyasiyada BH-dən sonra sıfır nəticə qalması ümumi zəmanətdirmi?

**Cavablar:** 16) 50; hər realizasiyada eyni say deyil. 17) Xeyr; ehtimal H0/model şərti altında test statistikasına aiddir. 18) Xeyr; FDR uyğun şərtlərdə gözlənilən payı idarə edir.

## 7. Təkrar icra

19. NumPy `a*b` və `a@b` nə ilə fərqlənir?
20. Seed eyni olsa da paket versiyası dəyişsə nəticə dəyişə bilərmi?
21. İki run qovluğunun adı fərqlidir, xülasələri eynidir. Bu uyğunsuzluqdurmu?

**Cavablar:** 19) Elementlər üzrə və matris vurması. 20) Bəli; seed bütün mühit fərqlərini idarə etmir. 21) Xeyr; yeni vaxt/unikal run kimliyi gözlənilir. Elmi nəticəni ayrıca müqayisə edin.

## 8. Elmi iddia

22. 20 şiş toxumasında 95% accuracy erkən xərçəng skrininqini təsdiqləyirmi?
23. `V17` ən yaxşı xüsusiyyətdirsə onu gen biomarkeri adlandırmaq olarmı?
24. U4247-dəki miRNA xülasəsini ilkin məqalə reproduksiyası saymaq olarmı?

**Cavablar:** 22) Xeyr; uyğun populyasiya, nəzarət, mərhələ və xarici validasiya yoxdur. 23) Əvvəl probe-gen xəritəsi və müstəqil sübut lazımdır. 24) Xeyr; ilkin data və metodla ayrıca icra tələb olunur.
