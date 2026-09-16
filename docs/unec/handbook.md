# Bioinformatika praktikumu

## 1. Məlumat, dəyişən və mənşə

**Məqsəd:** cədvəldəki rəqəmin hansı bioloji obyektə aid olduğunu izah etmək. Məlumatın formatı onun mənası ilə eyni deyil. `sample_id` rəqəmlə yazılsa belə, hesablama üçün miqdar deyil; nümunənin adıdır. `condition` kateqoriya, `count` qeyri-mənfi tam ölçmə, normalizasiya edilmiş ifadə isə davamlı dəyişən ola bilər. Çatışmayan ölçmə sıfır ifadə demək deyil.

UNEC məlumat və informasiya dərsindəki kəmiyyət/keyfiyyət ayrımını RNA-seq cədvəlinə tətbiq edək. Bir sətir gen, sütunlar nümunələrdir. Metadata cədvəli hər nümunənin müalicə qrupunu və bioloji təkrarını saxlayır. İki cədvəlin əlaqəsi sütun sırası ilə deyil, `sample_id` ilə qurulmalıdır. Sütunların yeri dəyişdikdə düzgün uyğunlaşdırma nəticəni dəyişdirməz; mövqeyə görə birləşdirmə isə qrupları səhv verə bilər.

Mənşə qeydi faylın haradan gəldiyini, nə vaxt alındığını, hansı versiyaya aid olduğunu və dəyişdirilib-dəyişdirilmədiyini saxlayır. SHA-256 eyni baytların istifadə edildiyini yoxlayır. O, elmi doğruluğu, müəllifliyi və istifadə hüququnu sübut etmir. Buna görə hash ilə yanaşı accession, mənbə URL-i, müəllif və lisenziya statusu da yazılır.

**Praktika:** `results/raw-examples/rna-model/counts.tsv` və `metadata.csv` fayllarında nümunə adlarını müqayisə edin. 6 nümunə və 124 gen gözlənilir. Bunlar chrI üzrə kiçik subsample nəticələridir; bütün yeast genomunu təmsil edən tam eksperiment kimi şərh edilməməlidir.

**Keçid meyarı:** bir nümunənin mənbədən yekun hesabata yolunu izah edin; missing, zero və duplicate arasındakı fərqi nümunə ilə göstərin.

**Mənbə:** U4072, abzas 19-26; U4084, abzas 16-48. Fayl kimlikləri [kataloqda](../../resources/unec/catalog.csv) saxlanılıb.

## 2. Bioloji verilənlər bazası

**Məqsəd:** məlumat bütövlüyünü proqramın yaddaşından asılı olmayan qaydalarla qorumaq. Verilənlər bazası sadəcə böyük Excel cədvəli deyil: cədvəllər arasındakı əlaqələr və qəbul edilən qiymətlər də modelin hissəsidir.

Bu laboratoriyada `sample` nümunələri, `gene` genləri, `gene_count` isə nümunə-gen ölçmələrini saxlayır. `gene_count` cədvəlinin əsas açarı iki sütundan ibarətdir: `(sample_id, gene_id)`. Eyni gen müxtəlif nümunələrdə ölçülə bilər, eyni nümunədə müxtəlif genlər ola bilər; eyni cüt ikinci dəfə əlavə edilə bilməz. Xarici açar mövcud olmayan nümunəyə ölçmə yazılmasını rədd edir. SQLite-da bunun üçün bağlantıda `PRAGMA foreign_keys=ON` aktiv edilməlidir.

Sayım mənfi və ya kəsr ola bilməz. Kod həm qeyri-mənfilik, həm də SQLite daxilində tam ədəd tipini yoxlayır. Bu qayda TPM kimi davamlı qiymətlər üçün uyğun deyil; TPM ayrıca ölçmə tipi və ayrıca sxem tələb edər. Cədvəldə ölçmə vahidini dəyişib əvvəlki sütun adını saxlamaq təhlükəli qarışıqlıq yaradır.

```sql
SELECT s.sample_id, s.condition, SUM(c.count) AS assigned_fragments
FROM sample s JOIN gene_count c USING(sample_id)
GROUP BY s.sample_id, s.condition
ORDER BY s.sample_id;
```

Bu sorğu hər nümunəyə genlər üzrə təyin edilmiş fragmentləri cəmləyir. Cəm FASTQ-dakı bütün read-lərin sayı deyil: mapping və assignment zamanı fərqli filtrlər tətbiq edilib. `run_study_database.py` SQL cəmlərini ilkin matrisin ümumi cəmi ilə tutuşdurur.

**Keçid meyarı:** 744 qeyd, 6 nümunə, 124 gen alınmalıdır; integrity check `ok`, foreign-key pozuntuları boş olmalıdır. Bir keyfiyyət qaydasının pozulmasını testlə göstərin.

**Mənbə:** U4084, abzas 16-69; U4129 metadata ilə mövzunun yoxlanması nümunəsidir: faylın daxilində genetika deyil, database sualları var.

## 3. Data mining və sızmasız maşın öyrənməsi

**Məqsəd:** çoxsaylı xüsusiyyətlərdən model qurarkən test məlumatının qərarlara qarışmasının qarşısını almaq. Khan mikroarray nümunəsində 2308 xüsusiyyət, cəmi 63 training nümunəsi var. Xüsusiyyətlərin çoxluğu güclü proqnoza zəmanət vermir; təsadüfi əlaqələri tapmağı asanlaşdırır.

Ardıcıllıq belədir: sıfır dispersiyalı sütunları çıxar, ANOVA ilə xüsusiyyət seç, standartlaşdır, linear SVM öyrət. Bu addımların hamısı bir pipeline daxilindədir. Beşqat cross-validation zamanı hər training fold öz xüsusiyyətlərini və orta/standart sapmalarını öyrənir. Bütün 83 nümunədə əvvəlcədən gen seçib sonra cross-validation etmək test məlumatını təlimə sızdırardı.

Grid search yalnız 63 training nümunəsində `k = 25, 100, 500` və `C = 0.01, 0.1, 1` seçimlərini müqayisə edir. Balanced accuracy hər sinif üzrə recall-un ortasıdır; çoxluq sinfi nəticəni təkbaşına idarə etmir. Ən çox rast gəlinən sinfi deyən dummy model nə qədər irəliləyiş olduğunu görmək üçün başlanğıc müqayisədir.

Saxlanmış icrada 25 xüsusiyyət və C=0.01 seçildi. Seçim üçün istifadə olunan CV balı 1.0-dır, lakin bu, qərəzsiz son generalizasiya qiyməti deyil. Bir dəfə qiymətləndirilən 20 test nümunəsindən 19-u düzgün təsnif edildi. Test nəticəsinə baxıb grid-i yenidən uyğunlaşdırmaq həmin dəsti inkişaf dəstinə çevirər; yeni qiymətləndirmə üçün yeni məlumat lazım olar.

`V1` kimi sütun adları təsdiqlənmiş gen simvolları deyil. Ən yüksək bal alan sütunu biomarker adlandırmaq üçün probe annotasiyası, müstəqil cohort və bioloji yoxlama lazımdır. Mənbənin əvvəlcədən etdiyi preprocessing-in müstəqilliyi burada müəyyən edilməyib.

**Keçid meyarı:** preprocessing-in niyə fold daxilində olması lazım olduğunu izah edin; accuracy və balanced accuracy-ni confusion matrix-dən hesablayın.

**Mənbə:** U4096, abzas 17-38 və 85-93; U4114, abzas 75-84; U4117, PDF səhifə 41, 55-56; U4252, slayd 4-7.

## 4. Genotipdən fenotipə

**Məqsəd:** variant, allel, genotip və fenotipi ayrı anlayışlar kimi istifadə etmək. Allel müəyyən genomik mövqedəki alternativ ardıcıllıq variantıdır. Diploid autosomal lokusda fərd adətən valideynlərdən bir nüsxə alır; eyni və fərqli allellər homozigot və heterozigot vəziyyət yarada bilər. Haploid genom və cinsiyyət xromosomları üçün ploidiyanı ayrıca nəzərə almaq lazımdır.

VCF-də `0/1` genotipi REF və birinci ALT allelinin mövcudluğunu göstərir. `0|1` phased qeyddir; `0/1` isə bu faza məlumatını vermir. REF alleli sağlam, ALT alleli xəstəlik alleli demək deyil. Referens genom müqayisə çərçivəsidir, klinik normalın universal təsviri deyil.

Fenotip müşahidə olunan xüsusiyyətdir. Genotip, mühit, inkişaf mərhələsi və onların qarşılıqlı təsiri fenotipə töhfə verə bilər. Poligen xüsusiyyətdə bir neçə gen bir əlamətə təsir edir. Pleiotropiyada isə bir gen bir neçə xüsusiyyətlə bağlıdır. Bunlar bir-birini əvəz edən terminlər deyil. Hipomorf allel funksiyası azalmış alleldir; genotip və mühit arasındakı ümumi uyğunsuzluğun adı deyil.

İrsiyyət müzakirəsində ayrıca mexanizmləri ayırın: nüvə genomu, mitoxondrial genom və epigenetik vəziyyət eyni ötürülmə qaydasına malik deyil. Sperm hüceyrələrində mitoxondri var; insanlarda mitoxondrial irsiyyətin əsasən maternal olması onların spermada olmaması ilə izah edilmir.

**Praktika:** mövcud variant layihəsində bir VCF sətrinin CHROM, POS, REF, ALT, FILTER və GT sahələrini izah edin. `PASS` yalnız tətbiq edilmiş texniki filtrlərin keçildiyini bildirir. Patogenlik, penetrantlıq və səbəb-nəticə üçün başqa sübutlar tələb edilir.

**Keçid meyarı:** eyni variantın iki fərqli genom build-də koordinatlarının niyə eyni olmaya biləcəyini və ploidiyanın genotipə təsirini izah edin.

**Mənbə:** U4126, abzas 17-31 və 50-54; U4139, abzas 17-22. Dəqiqləşdirmələr üçün [errata](errata.md).

## 5. Sequence bazaları və BLAST

**Məqsəd:** axtarış aləti, axtarılan kolleksiya və nəticə qeydini ayırmaq. GenBank ardıcıllıq qeydləri saxlayan resursdur; BLAST oxşarlıq axtarışı üçün proqramlar ailəsidir. BLASTN və BLASTX ayrıca verilənlər bazası deyil. Eyni proqram müxtəlif database-lərə qarşı işlədilə bilər.

BLASTN nukleotid sorğunu nukleotid kolleksiyası ilə müqayisə edir. BLASTP protein-protein axtarışıdır. BLASTX nukleotid sorğunu altı oxuma çərçivəsində tərcümə edib protein kolleksiyası ilə müqayisə edir. TBLASTN isə protein sorğunu tərcümə olunan nukleotid kolleksiyasında axtarır. Yanlış proqram seçimi bioloji sualı dəyişdirə və uyğun nəticələri qaçıra bilər.

Nəticədə percent identity, alignment length, query coverage, score və E-value birlikdə qiymətləndirilir. Yüksək identity çox qısa uyğunlaşmadan gələ bilər. E-value müəyyən axtarış şərtlərində təsadüfən gözlənilən ən azı bu qədər güclü uyğunlaşmaların sayını ifadə edir; database ölçüsündən də asılıdır. Rəngli score zolağı nukleotid uzunluğu ölçüsü deyil. Oxşarlıq təkbaşına eyni funksiya və ya birbaşa ortologiya sübut etmir.

**Praktika:** lokal alignment layihəsində iki qısa sequence üçün score və alignment length-i ayrı yazın. Sonra gələcək BLAST icrası üçün proqram versiyası, database adı/tarixi, sorğu accession-u və parametrlərdən ibarət qeyd hazırlayın. Bu dərsin əlavə olunması ayrıca BLAST axtarışının icra edildiyi mənasına gəlmir.

PubMed biblioqrafik axtarış resursudur. Qeydin pulsuz görünməsi bütün məqalələrin tam mətninin pulsuz olduğu mənasına gəlmir. Tam mətn linki və istifadə şərti ayrıca yoxlanmalıdır.

**Keçid meyarı:** nukleotid sorğusu ilə uzaq protein homologiyası araşdırması üçün BLASTX seçiminin səbəbini izah edin; qısa uyğunlaşmanın yüksək identity-sini tənqidi şərh edin.

**Mənbə:** U4208, slayd 3-15; [NCBI BLAST sənədləri](https://blast.ncbi.nlm.nih.gov/doc/blast-help/).

## 6. Hipotez, qeyri-müəyyənlik və FDR

**Məqsəd:** müşahidə olunan fərqi statistik və bioloji mənada ayrı qiymətləndirmək. H0 əvvəlcədən sübut edilmiş fikir deyil; model altında sınaqdan keçirilən null hipotezdir. Onu rədd edə bilməmək doğruluğunu sübut etmir. İki orta qiymətin 20 və 50 olması nümunə sayı, variasiya və dizayn bilinmədən test qərarı verməyə kifayət etmir.

P-value H0 və testin digər fərziyyələri doğru olduqda müşahidə edilən qədər və ya daha ekstremal test statistikasının ehtimalıdır. Bu, H0-ın doğru olması ehtimalı və ya nəticənin səhv olma ehtimalı deyil. `p < 0.05` bioloji əhəmiyyət və ya klinik fayda sübut etmir. Effektin ölçüsü, interval, data keyfiyyəti və əvvəlcədən seçilmiş analiz planı birlikdə təqdim edilir.

Min həqiqi null hipotezi ayrı-ayrı 0.05 həddində yoxladıqda, kalibrə edilmiş testlər üçün gözlənilən yanlış müsbətlərin sayı 50-dir. Bu, hər icrada dəqiq 50 alınacaq demək deyil. Bizim seed-i sabit Welch t-test simulyasiyamızda 47 nəticə həddi keçdi. Benjamini-Hochberg düzəlişindən sonra bu realizasiyada sıfır nəticə qaldı. Bu bir sınaq BH-nin bütün mümkün datada sıfır səhv verəcəyini göstərmir.

BH uyğun fərziyyələr altında rədd edilən hipotezlər arasında yanlış kəşflərin payının gözlənilən qiymətini idarə edir. FDR və ailə üzrə ən azı bir yanlış müsbət ehtimalı eyni ölçü deyil. Hipotezlər arasındakı asılılıq strukturu metodun şərtlərinə təsir edə bilər.

Real RNA nümunələrinin library totals xülasəsi ayrıca hesablanır. Library ölçülərinin yaxınlığı batch təsirinin yoxluğunu və ya bütün genlərin ifadəsinin eyniliyini sübut etmir. Bu xülasə QC məlumatıdır, differential expression testini əvəz etmir.

**Keçid meyarı:** simulyasiya və bioloji müşahidəni ayırın; H0-ı rədd etməmək üçün düzgün cümlə qurun; p-value, FDR və effekt ölçüsünün üç fərqli sualını yazın.

**Mənbə:** U4226, abzas 37-55; U4236, abzas 12 və 23-28; U4230, ehtimal, etibar intervalları və hipotez yoxlaması bölmələri; Think Stats, fəsil 9.

## 7. Proqram təminatı və təkrarlana bilən icra

**Məqsəd:** nəticəni yalnız bir şəxsin kompüterində işləyən əməliyyatlardan ayırmaq. U4178-də MATLAB matrisləri və proqram faylları təqdim olunur. Repo Python istifadə edir, lakin əsas dərs dəyişmir: giriş, əməliyyat və çıxış aydın olmalıdır. Köhnə MATLAB slaydları cari toolbox imkanlarının yoxlanmış siyahısı kimi təqdim edilmir.

MATLAB-da indekslər adətən 1-dən, Python-da 0-dan başlayır. NumPy-da `a * b` elementlər üzrə vurmadır, `a @ b` matris vurmasıdır. Ölçülər uyğun olsa belə, yanlış operator bioloji mənanı dəyişə bilər. Gen-nümunə matrisini nümunə-gen matrisinə çevirmək sadəcə texniki detal deyil: modelin hansı oxu müşahidə saydığı aydın yazılmalıdır.

Hər yeni icra ayrıca qovluğa yazılır. `run.json` girişlərin SHA-256 izlərini, parametrləri, mühit məlumatlarını və mənbə kodunun izlərini saxlayır. Seed təsadüfi seçimləri sabitləşdirir; paket versiyaları, hesablama arxitekturası və paralel əməliyyatlar da nəticəyə təsir edə bilər. Buna görə seed təkbaşına tam reproduksiya təmin etmir.

Saxlanmış nəticəni yoxlamaq iki səviyyəlidir: faylların hash uyğunluğu nəticənin dəyişmədiyini göstərir; kodu təkrar işlətmək isə hazırkı mühitin nəticəni yenidən yarada bildiyini yoxlayır. Bunlar ayrı sübutlardır. Tarixi nəticənin commit-i əvvəlki ola bilər; dirty flag və həmin anda saxlanmış kod hash-ləri gizlədilmir.

**Praktika:** yeni laboratoriyalardan birini iki dəfə işlədin. Yeni run qovluqları yaranmalıdır. Elmi xülasələri müqayisə edin; vaxt nişanlarının fərqli olması gözləniləndir. Mövcud snapshot-u səssizcə əvəz etmək əvəzinə yeni nəticənin mənşəyini saxlayın.

**Keçid meyarı:** “fayl eynidir”, “kod eynidir” və “nəticə təkrar alındı” ifadələrinin fərqli sübutlarını göstərin.

**Mənbə:** U4178, abzas 12-35; U4158, abzas 16-22; repo icra qeydləri.

## 8. Elmi sualdan yoxlanılan iddiaya

**Məqsəd:** geniş ideyanı konkret giriş, ölçü və qərar meyarına çevirmək. U4252-də gen ifadəsi və ML ilə xəstəlik araşdırması mövzusu təqdim olunur. Bizim konkret sualımız: “Khan benchmark-ının verilmiş training hissəsində seçilmiş model, saxlanmış test hissəsində dörd şiş sinfini hansı səhvlərlə ayırır?” Bu sual mövcud data ilə cavablandırıla bilir.

“Xərçəngi erkən aşkarlayırıq” fərqli sualdır. Bunun üçün xəstəliyin erkən mərhələləri, uyğun sağlam/nəzarət qrupu, nümunə toplama protokolu, populyasiya prevalansı və prospektiv qiymətləndirmə lazımdır. Tarixi şiş toxuması benchmark-ında yüksək accuracy həmin sübutları yaratmır. Diaqnostik tətbiq üçün xarici cohort, batch uyğunluğu, həssaslıq/spesifiklik, kalibrasiya və klinik istifadə konteksti ayrıca araşdırılmalıdır.

U4247-də miRNA və siqnal yolları barədə ədəbiyyat xülasəsi var. Xülasədən “bu miRNA səbəb olur” nəticəsi çıxarmaq olmaz. Əvvəl ilkin məqalə, eksperiment modeli, ölçmə metodu, müdaxilə və nəzarət qrupları tapılmalıdır. Pathway təsviri ilə real enrichment nəticəsi, müşahidə ilə müdaxilə sübutu ayrılır.

Hesabatın minimal forması: sual; dataset və seçim qaydası; analizdən əvvəl parametrlər; nəticə və qeyri-müəyyənlik; alternativ izah; məhdudiyyət; növbəti sınaq. Bir nəticə gözləntiyə uyğun gəlmədikdə onu gizlətmək əvəzinə məlumat keyfiyyəti, model fərziyyələri və statistik güc yoxlanır. Yeni hipotez əvvəlki testin təsdiqi kimi təqdim edilmir.

**Praktika:** expression modelinin bir səhvini confusion matrix-də tapın. Yeni model seçmədən bu səhvin hansı siniflər arasında olduğunu yazın. Sonra gələcək müstəqil cohort üçün əvvəlcədən qiymətləndirmə planı qurun: hansı metrik, hansı interval, hansı qruplar və hansı istisna meyarları istifadə ediləcək?

**Keçid meyarı:** müşahidə, metod seçimi və gələcək hipotezi üç ayrı abzasda təqdim edin. Sizin nəticənizdən çıxarıla bilməyən bir iddianı da konkret yazın.

**Mənbə:** U4252, slayd 1-9; U4247, abzas 11-15; [ISLP Khan mənbə kartı](../../datasets/public-datasets/khan.md).
