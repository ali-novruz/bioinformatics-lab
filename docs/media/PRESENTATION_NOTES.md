# Təqdimatın mətn və danışıq qeydləri

26 slayd. Təxmini təqdimetmə müddəti: 20–25 dəqiqə. Son 6 slayd ayrıca praktiki bələdçidir.
Mənbə vəziyyəti: `43ebcd8`. Hazırlanma: 19 sentyabr 2026.
Aşağıda yekun PPTX-dəki mətn, əlavə izahlar və mənbələr verilir. Qrafiklərin izahı danışıq qeydlərindədir.

## 01. Bioloji sualdan nəticəyə

### Slaydın mətni

- Layihənin imkanları və praktiki istifadə bələdçisi

**Danışıq qeydi:** Bu təqdimat Bioinformatics Research Lab repository-sinin mövcud imkanlarını və istifadə yolunu izah edir. Material tələbələr, müəllimlər və kiçik reproduksiya layihələri qurmaq istəyənlər üçündür. Üz qabığı dekorativ AI illüstrasiyasıdır. Sonrakı elmi qrafiklər saxlanmış analizlərdən götürülüb. Təqdimat təxminən 20–25 dəqiqə, son altı praktiki addım isə ayrıca nümayiş üçün nəzərdə tutulub.

**Mənbələr:**

- [README.md](../../README.md)
- [assets/readme/README.md](../../assets/readme/README.md)

## 02. Bir sualın laboratoriyada keçdiyi yol

### Slaydın mətni

- 1
- Sual
- Nəyi öyrənmək
- istəyirik?
- 2
- Məlumat
- Dataset və onun
- istifadə sərhədi
- 3
- Analiz
- Metod, parametr
- və çıxışlar
- 4
- Nəzarət
- Nəticə nə qədər
- etibarlıdır?
- Yekun şərh növbəti tədqiqat sualının başlanğıcı olur.

**Danışıq qeydi:** Repository yalnız oxu siyahısı deyil. Mövzu qeydləri işlək layihələrə, layihələr saxlanmış nəticələrə, nəticələr isə nəzarət təcrübələrinə bağlanır. Başlanğıc üçün Python və biologiyanın əsasları kifayətdir. Daha mürəkkəb RNA-seq və xam oxunuş workflow-ları əlavə statistik hazırlıq və alətlər tələb edir. Məqsəd nəticənin necə yarandığını başa düşməkdir.

**Mənbələr:**

- [docs/START_HERE.md](../../docs/START_HERE.md)
- [roadmap/README.md](../../roadmap/README.md)
- [research/graph.json](../../research/graph.json)

## 03. Mövcud laboratoriyanın ölçüsü

### Slaydın mətni

- 12
- işlək layihə
- 8
- notebook
- 4 PDF kitab, praktikum və 57 test. Saylar 16 sentyabr 2026 auditinə aiddir.

**Dairəvi qrafik:** 8 offline layihə; 4 endirmə tələb edən layihə.

**Danışıq qeydi:** Offline burada paketlər quraşdırıldıqdan sonra dataset endirmədən işləməyi bildirir. Paket quraşdırılması internet tələb edə bilər. DNA layihəsi raw cache olmadıqda açıq işarələnmiş toy nümunəyə keçir. Səkkiz notebook-un hamısı eyni tip deyil: ilk beşi analiz və modelləri işlədir, son üçü nəticələrin oxunması və qismən yenidən hesablanmasını göstərir. Test sayı sonsuz düzgünlük zəmanəti deyil, mövcud yoxlama əhatəsidir.

**Mənbələr:**

- [STATUS.md](../../STATUS.md)
- [projects/registry.json](../../projects/registry.json)
- [notebooks/README.md](../../notebooks/README.md)
- [resources/books/README.md](../../resources/books/README.md)

## 04. Ardıcıllıq və genom layihələri

### Slaydın mətni

- Layihə ID-si
- Giriş və metod
- Çıxış
- dna
- PhiX174 və ya işarələnmiş toy
- Sequence kompozisiyası
- alignment
- Sintetik sequence, NW və SW
- Hizalama və score müqayisəsi
- variants
- GIAB HG001 VCF prefix-i
- SNV, indel, Ti/Tv xülasəsi
- phylogeny
- 7 Opuntia fraqmenti, NJ
- Bootstrap dəstəkli ağac
- orfs
- Dairəvi PhiX174 genomu
- ORF namizədləri və koordinatlar
- proteins
- UniProt sequence və PDB
- Sequence xülasəsi, contact map
- ID-lər vahid başladıcıda işlənir: python scripts/lab.py run <id>

**Danışıq qeydi:** NW Needleman–Wunsch qlobal, SW Smith–Waterman lokal alignment-dir. Filogeniya Neighbor Joining ilə qurulur. Variant layihəsi variant çağırma dəqiqliyini ölçmür, hazır VCF-in kiçik hissəsini xülasə edir. Protein layihəsində insulin prekursorunun sequence-i ilə crambin strukturu ayrı nümunələrdir. Layihə adları ilə yanaşı dəqiq işlək ID-ləri göstərmək istifadəçinin ilk əmri rahat seçməsinə kömək edir.

**Mənbələr:**

- [projects/registry.json](../../projects/registry.json)
- [projects/README.md](../../projects/README.md)

## 05. İfadə və model layihələri

### Slaydın mətni

- Layihə ID-si
- Giriş və metod
- Çıxış
- rnaseq
- Pasilla, PyDESeq2
- Diferensial ifadə və PCA
- ml
- WDBC morfoloji əlamətləri
- Təsnifat və test metrikləri
- expression-ml
- Khan microarray, LinearSVC
- 4 sinif üzrə proqnoz
- database
- Yeast sayımları, SQLite
- Sorğulana bilən kataloq
- statistics
- Sintetik null simulyasiyası
- Çoxsaylı test və BH düzəlişi
- enrichment
- Yeast və SGD GO-slim
- Term üzrə zənginləşmə analizi
- Model seçimi training daxilində aparılır. WDBC girişləri gen ifadəsi deyil.

**Danışıq qeydi:** Bu altı layihə müxtəlif statistik sualları öyrədir. Pasilla xətti dizaynı ilə qrupları müqayisə edir. Khan çoxsaylı probe ölçmələrindən sinif təxmin edir. SQLite eyni məlumatı sorğulana bilən formaya gətirir. Null simulyasiyası p-value həddinin çoxsaylı testdə niyə kifayət etmədiyini göstərir. GO nəticələri isə seçilmiş gen siyahısının ölçüsündən və universe seçimindən asılıdır.

**Mənbələr:**

- [projects/registry.json](../../projects/registry.json)
- [projects/intermediate/gene-expression-ml/README.md](../../projects/intermediate/gene-expression-ml/README.md)

## 06. RNA-seq: nümunələr və gen ifadəsi

### Slaydın mətni

- 7
- Pasilla nümunəsi
- 1 113
- FDR < 0.05 olan gen
- 9 921 gen test edilir
- Dizayn: type + condition. PCA ayrı, diferensial ifadə modeli ayrı addımdır.

**Danışıq qeydi:** PCA log1p normallaşdırılmış sayımlar əsasında nümunələrin əsas dəyişmə istiqamətlərini göstərir. PCA nöqtələrinin ayrılması təkbaşına diferensial ifadə testi deyil. Dizayn texniki type amilini və condition qrupunu daxil edir. 1113 gen FDR həddini keçir, onlardan 232-si həm də mütləq log2 fold change 1-dən böyük şərtinə uyğundur. Fold change qiymətləri shrinkage tətbiq edilməmiş qiymətlərdir.

**Mənbələr:**

- [projects/intermediate/rnaseq/README.md](../../projects/intermediate/rnaseq/README.md)
- [results/research-audit/projects/rnaseq/summary.json](../../results/research-audit/projects/rnaseq/summary.json)

## 07. WDBC təsnifatının qiymətləndirilməsi

### Slaydın mətni

- 0.996
- test AUROC
- 426 training
- 143 test nümunəsi
- 30 morfoloji əlamət
- Nüvə morfologiyası benchmark-ı. Klinik tətbiq üçün ayrıca yoxlama tələb olunur.

**Danışıq qeydi:** AUROC modelin iki sinfi sıralama qabiliyyətini göstərir. Bu rəqəm 143 nümunəlik ayrılmış testdən alınır və başqa xəstəxanaya, populyasiyaya və ya skrininq şəraitinə avtomatik köçürülmür. Bootstrap nəticələri seçilmiş model və test nümunələrinə şərtlidir. Bu layihənin dərsi böyük score təqdim etməkdən çox, training və test ayrılmasını düzgün saxlamaqdır.

**Mənbələr:**

- [projects/intermediate/disease-classification/README.md](../../projects/intermediate/disease-classification/README.md)
- [results/research-audit/projects/ml/summary.json](../../results/research-audit/projects/ml/summary.json)

## 08. Khan: 4 sinif və ayrılmış test

### Slaydın mətni

- 63
- training
- nümunəsi
- 19/20
- testdə düzgün
- təsnifat
- 2 308 işlənmiş probe sütunu. Bu nəticə təsdiqlənmiş biomarker siyahısı deyil.

**Danışıq qeydi:** Pipeline variance filter, ANOVA seçimi, miqyaslandırma və LinearSVC-dən ibarətdir. Addımlar training cross-validation daxilində tətbiq edilir. Tarixi benchmark testində accuracy 0.95, balanced accuracy təxminən 0.9583-dür. Bu nəticə müstəqil müasir cohort və ya prospektiv skrininq yoxlaması deyil. Upstream emalın və donor asılılığının bəzi detalları məlum deyil.

**Mənbələr:**

- [projects/intermediate/gene-expression-ml/README.md](../../projects/intermediate/gene-expression-ml/README.md)
- [results/expanded-projects/gene-expression-ml/summary.json](../../results/expanded-projects/gene-expression-ml/summary.json)

## 09. Model siqnalı təsadüfdən fərqlənirmi?

### Slaydın mətni

- 0.99
- nested balanced
- accuracy
- 99
- etiket qarışdırılması
- p = 0.01
- Yalnız 63 training nümunəsi. Test faylları açılmayıb. Klinik validasiya deyil.

**Danışıq qeydi:** Xarici 5 fold və daxili 3 fold quruluşu model seçimini qiymətləndirmədən ayırır. Hər etiket qarışdırılmasında bütün pipeline yenidən işləyir. Bu training-only, post-hoc robustness auditidir. Null interval klinik performans üçün confidence interval deyil. Seçilmiş probe-ların orta Jaccard uyğunluğu 0.257 olub, lakin müxtəlif k ölçüləri bu müqayisəyə təsir edir. Yüksək proqnoz sabit biomarker siyahısı demək deyil.

**Mənbələr:**

- [experiments/controls/README.md](../../experiments/controls/README.md)
- [results/research-audit/expression-control/summary.json](../../results/research-audit/expression-control/summary.json)

## 10. GO nəticəsində dizaynın sərhədi

### Slaydın mətni

- 0 / 84
- singleton seçim
- BH < 0.05 verir
- Sabit 62 term ailəsində
- minimum padj: 0.277
- Riyazi əlçatanlıq yoxlaması. Sıfır əhəmiyyətli term bioloji fəaliyyətsizlik demək deyil.

**Danışıq qeydi:** Yeast analizində yalnız bir gen seçildiyindən hər mümkün singleton ayrıca sınanıb. Universe 84 gen və term ailəsi 62 term olaraq sabit saxlanıb. Heç bir seçim əhəmiyyət həddinə çatmır. Deməli, bu konkret dizaynda sıfır əhəmiyyətli term müşahidəsi təəccüblü deyil. Nəticə ümumi power curve və ya bütün GO analizlərinə aid hökm kimi istifadə edilməməlidir.

**Mənbələr:**

- [projects/intermediate/go-enrichment/README.md](../../projects/intermediate/go-enrichment/README.md)
- [results/research-audit/enrichment-control/summary.json](../../results/research-audit/enrichment-control/summary.json)

## 11. Opuntia fraqmentlərinin filogeniyası

### Slaydın mətni

- 7
- fraqment
- 200
- bootstrap
- 146 tam ACGT sütunu və 8 dəyişən mövqe. Ağac qısa fraqmentlərə aiddir.

**Danışıq qeydi:** Başlanğıc alignment 156 sütundur, complete ACGT filtrasiyasından sonra 146 qalır. P-distance məsafəsi əsasında köksüz ağac qurulur. Bootstrap sütunların təkrar nümunələnməsidir və eyni məhdud məlumat daxilində dəstəyi ölçür. Az sayda dəyişən mövqe olduğuna görə nəticəni genom miqyasında təkamül tarixi kimi şərh etmək olmaz.

**Mənbələr:**

- [projects/intermediate/phylogeny/README.md](../../projects/intermediate/phylogeny/README.md)
- [results/expanded-projects/phylogeny/summary.json](../../results/expanded-projects/phylogeny/summary.json)

## 12. Dairəvi PhiX174 genomunda ORF-lər

### Slaydın mətni

- 114 namizəd
- 93 müsbət strand
- 21 mənfi strand
- 24 başlanğıcı
- keçən namizəd
- 5 386 nt. ATG, ilk stop, minimum 30 aa. Namizədlər təsdiqlənmiş gen annotasiyası deyil.

**Danışıq qeydi:** PhiX174 genomu dairəvi olduğu üçün koordinat başlanğıcını keçən namizədlər də saxlanır. Nested ORF-lər çıxarılmır. Ən uzun namizəd 522 amin turşusudur. Bu sadə qayda əsasında namizəd tapma məşqidir, eksperimental təsdiq və ya tam gen annotasiyası deyil. Parametr dəyişdikdə namizəd sayı dəyişə bilər.

**Mənbələr:**

- [projects/beginner/orf-discovery/README.md](../../projects/beginner/orf-discovery/README.md)
- [results/expanded-projects/orf-discovery/summary.json](../../results/expanded-projects/orf-discovery/summary.json)

## 13. İki ayrı protein nümunəsi

### Slaydın mətni

- P01308
- Insulin prekursoru
- 110 amin turşusu
- Sequence analizi
- 1CRN
- Crambin strukturu, 46 Cα
- Sequence və struktur nümunələri ayrı proteinlərə aiddir.

**Danışıq qeydi:** Bu layihə iki ayrı data formatını öyrədir. UniProt P01308 sequence üzərində uzunluq və kompozisiya analizi üçündür. PDB 1CRN məkan koordinatları və contact map üçündür. Onların yanaşı göstərilməsi sequence-structure uyğunluğu iddiası yaratmamalıdır. Qrafik crambin C-alpha izini göstərir, yeni proqnozlaşdırılmış struktur deyil.

**Mənbələr:**

- [projects/intermediate/protein-analysis/README.md](../../projects/intermediate/protein-analysis/README.md)
- [results/research-audit/projects/proteins/summary.json](../../results/research-audit/projects/proteins/summary.json)

## 14. Xam oxunuşdan analizə

### Slaydın mətni

- FASTQ
- Keyfiyyət
- Alignment
- Sayım
- Model
- 6
- real yeast nümunəsi
- 300k
- oxunuş cütü
- 84
- test edilmiş gen
- Əlavə DNA fixture: 32 variant, 27 PASS. Kiçik integration sınağı, tam genom benchmark-ı deyil.

**Danışıq qeydi:** RNA yolu FASTQ, FastQC, STAR, featureCounts və PyDESeq2 addımlarından keçir. FDR geni YAL005C-dir, log2 fold change 0.224 olduğundan böyük effekt həddini keçmir. DNA workflow-u BWA və variant calling mərhələlərini yoxlayır. Xarici fixture üçün donor truth məlum deyil, ona görə precision və recall iddiası yoxdur. Sintetik məlum müsbət nəzarət ayrıca işlədilib.

**Mənbələr:**

- [results/raw-examples/README.md](../../results/raw-examples/README.md)
- [workflows/README.md](../../workflows/README.md)

## 15. Hər nəticənin izlənən mənşəyi

### Slaydın mətni

- 1
- Input
- Accession, versiya
- və hash
- 2
- İcra
- Parametr, mühit
- və log
- 3
- Çıxış
- Status, cədvəl
- və hash
- Windows və Linux: 99 permutation score-u 1e-12 həddində uyğun gəlib
- Uyğunluq yoxlanmış dataset, seed və mühitlər daxilindədir.

**Danışıq qeydi:** Hash faylın konkret baytlarını tanıdır, bioloji doğruluğunu təsdiq etmir. Ayrı nəticə qovluqları keçmiş icraların təsadüfən əvəz edilməsinin qarşısını alır. Tarixi source arxivləri köhnə nəticələrin hansı koddan yarandığını izləməyə imkan verir. Platforma uyğunluğu yalnız yoxlanmış dataset, seed və mühitlər daxilində göstərilib. Yeni mühit üçün eyni uyğunluğu əvvəlcədən zəmanət vermək olmaz.

**Mənbələr:**

- [DATA_POLICY.md](../../DATA_POLICY.md)
- [results/README.md](../../results/README.md)
- [results/research-audit/README.md](../../results/research-audit/README.md)

## 16. UNEC mənbələrindən praktik dərslərə

### Slaydın mətni

- 68
- kataloqlaşdırılmış fayl
- 8
- praktiki dərs
- 24
- cavablı tapşırıq
- 15 həftəlik proqram
- 14 səhifəlik PDF praktikum
- 61 unikal mənbə, 7 bayt səviyyəli dublikat. Mənbələr kataloqda izlənir.

**Danışıq qeydi:** Göndərilmiş UNEC PDF, DOCX və PPTX faylları kataloqlaşdırılıb. Məqsəd bütün faylları kor şəkildə yığmaq əvəzinə, tədris mövzularını işə yarayan praktiki məşqlərlə əlaqələndirməkdir. Materialların mənşəyi kataloqda saxlanır. Dərslər və cavablar müstəqil öyrənməni asanlaşdırır, amma müəllimin qiymətləndirməsini avtomatik əvəz etmir.

**Mənbələr:**

- [docs/unec/README.md](../../docs/unec/README.md)
- [resources/unec/README.md](../../resources/unec/README.md)
- [resources/unec/bioinformatika-praktikum.pdf](../../resources/unec/bioinformatika-praktikum.pdf)

## 17. Öyrənmə yolunun əsas dayanacaqları

### Slaydın mətni

- 1
- Biologiya
- 16 anlayış
- 11 format
- 2
- Python
- İşlək layihələr
- 8 notebook
- 3
- Real data
- 18 database kartı
- PDF kitablar
- 4
- Tədqiqat
- 11 məqalə qeydi
- 9 mini-review
- Tam yol 10 mərhələdən ibarətdir. Məqalə qeydləri systematic review deyil.

**Danışıq qeydi:** Öyrənmə yolu biologiya və Python əsaslarından real analiz və tədqiqat sualına doğru gedir. Məqalə qeydləri systematic review deyil və orijinal məqalələrin bütün benchmark-larını təkrar etmir. Oxucu hər qeydin əhatəsini yoxlamalıdır. Kitab manifesti PDF mənbə ünvanlarını və istifadə qeydlərini göstərir. Yeni kitab əlavə edilərkən açıq və icazəli PDF mənbə üstün tutulur.

**Mənbələr:**

- [roadmap/README.md](../../roadmap/README.md)
- [resources/books/README.md](../../resources/books/README.md)
- [research/papers/README.md](../../research/papers/README.md)
- [research/literature-reviews/README.md](../../research/literature-reviews/README.md)

## 18. Real data, sintetik nümunə və protokol

### Slaydın mətni

- Material
- İstifadə məqsədi
- Nə yoxlanır?
- Real dataset
- Məhdud bioloji sual
- Mənşə, dizayn, ölçü
- Sintetik nümunə
- Metod və məlum nəzarət
- Gözlənilən davranış
- Gələcək protokol
- Yeni tədqiqat planı
- Sual və qəbul meyarı
- Böyük raw fayllar Git-ə daxil edilmir. Mənbə və istifadə şərti dataset kartında saxlanır.

**Danışıq qeydi:** Şəxsi və ya həssas məlumat bu tədris nümunələrinin bir hissəsi deyil. Yeni dataset əlavə edən iştirakçı onun istifadə şərtini və mənbəyini yoxlamalıdır. PDF kitab istəyi icazəsiz nüsxə paylaşmaq kimi şərh edilmir. Manifestlər təkrar endirməni və dəyişikliyi izləməyi asanlaşdırır. Repo hazırda private-dır, GitHub linkləri səlahiyyətli hesabla açılır.

**Mənbələr:**

- [DATA_POLICY.md](../../DATA_POLICY.md)
- [resources/books/README.md](../../resources/books/README.md)
- [datasets/README.md](../../datasets/README.md)

## 19. Model nəticəsindən elmi iddiaya

### Slaydın mətni

- Yüksək
- score
- Ayrıca sübut tələb edənlər
- Yeni cohort-da doğrulama
- Probe seçiminin sabitliyi
- Klinik fayda
- Kiçik dataset və texniki dizayn nəticənin tətbiq sərhədini müəyyən edir.

**Danışıq qeydi:** WDBC və Khan nəticələri tədris benchmark-larıdır. Gene-level biomarker iddiası üçün probe identifikasiyası, sabitlik və müstəqil doğrulama lazımdır. GO-da sıfır əhəmiyyətli term pathway fəaliyyətsizliyi demək deyil. ORF namizədi gen annotasiyası deyil. Variant sayları calling accuracy deyil. Bu fərqlər təqdimat və videoda da qorunmalıdır.

**Mənbələr:**

- [docs/RESEARCH_AUDIT.md](../../docs/RESEARCH_AUDIT.md)
- [experiments/controls/README.md](../../experiments/controls/README.md)

## 20. Növbəti tədqiqatların planı

### Slaydın mətni

- 01
- Khan
- Müstəqil cohort
- Sabit k ilə sabitlik
- 02
- GO
- Foreground ölçüsü
- Universe həssaslığı
- 03
- Xam workflow
- Truth dataset
- Daha böyük miqyas
- Bunlar gələcək işlərdir. 30 ideyanın hamısı icra edilməyib.

**Danışıq qeydi:** İnkişaf prioriteti yeni nəticə sayını artırmaqdan əvvəl mövcud iddiaları daha sərt yoxlamaqdır. Sabit k Jaccard şərhində seçilmiş siyahı ölçüsü qarışıqlığını azaldar. GO həssaslıq analizi cari singleton attainability təcrübəsindən fərqli sualdır. Variant workflow-u üçün məlum truth olmadan dəqiqlik benchmark-ı qurmaq olmaz. Hər yeni layihə əvvəlcə sual, giriş, metod və qəbul meyarı ilə yazılmalıdır.

**Mənbələr:**

- [docs/RESEARCH_AUDIT.md](../../docs/RESEARCH_AUDIT.md)
- [projects/IDEAS.md](../../projects/IDEAS.md)

## 21. Başlanğıc 1. Repo xəritəsi

### Slaydın mətni

- bioinformatics-lab
- START_HERE
- Başlanğıc yolu
- SETUP
- Mühit qurulması
- PROJECTS
- Analizin seçilməsi
- STATUS
- İcra əhatəsi
- Dəqiq yollar: docs/START_HERE.md, SETUP.md, projects/README.md, STATUS.md.

### Tam əmr nümunəsi

```text
docs/START_HERE.md
SETUP.md
projects/README.md
STATUS.md
```

**Danışıq qeydi:** README üz qabığından sonra başlanğıc keçidini açın. START_HERE oxucu məqsədinə uyğun yolu göstərir. SETUP mühit qurulmasını izah edir. STATUS mövcud icra əhatəsini bildirir. Layihəni seçərkən offline və download fərqini yoxlayın. Şəkilli bələdçinin bu səhifəsi GitHub interfeysinin saxta screenshot-u deyil, fayl xəritəsidir.

**Mənbələr:**

- [docs/START_HERE.md](../../docs/START_HERE.md)
- [SETUP.md](../../SETUP.md)
- [STATUS.md](../../STATUS.md)

## 22. Başlanğıc 2. Python mühiti

### Slaydın mətni

- 01
- Mühit yarat
- python -m venv .venv
- 02
- Aktivləşdir
- .venv\Scripts\Activate.ps1
- 03
- Paketləri qur
- python -m pip install -e ".[dev]"
- Repo kökündə Python 3.12. Linux/macOS: source .venv/bin/activate.

### Tam əmr nümunəsi

```text
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

**Danışıq qeydi:** Repository əvvəlcə lokal kompüterə clone və ya ZIP vasitəsilə alınmalıdır. Bu əmrlər repo kökündə yerinə yetirilir. PowerShell activation məhdud olarsa siyasəti dəyişmədən .venv/Scripts/python.exe yolunu birbaşa işlətmək olar. RNA-seq daxil tam suite üçün dev ilə yanaşı research extra-sı da lazımdır. Python 3.11 də əsas paket və CI-də dəstəklənir.

**Mənbələr:**

- [SETUP.md](../../SETUP.md)
- [README.md](../../README.md)

## 23. Başlanğıc 3. İlk offline analiz

### Slaydın mətni

- ALIGNMENT
- python scripts/lab.py list
- python scripts/lab.py run alignment --offline
- passed
- Yeni nəticə qovluğu: results/runs/
- passed uğurlu icrada gözlənən statusdur. Bu slayd terminal screenshot-u deyil.

### Tam əmr nümunəsi

```text
python scripts/lab.py list
python scripts/lab.py run alignment --offline

Çıxış: results/runs/ daxilində yeni qovluq
```

**Danışıq qeydi:** Alignment layihəsi kiçik sintetik sequence cütləri ilə qlobal və lokal hizalamanı göstərir. İşləyən prosesin yaratdığı qovluq yolunu saxlayın. Uğursuz icrada output-u uğurlu nəticə kimi təqdim etməyin. Bu əmrlər video çəkilişində qısa, real və təkrarlana bilən nümayiş üçün uyğundur. Nəticə qovluqlarının vaxt və ID hissələri hər icrada dəyişir.

**Mənbələr:**

- [scripts/lab.py](../../scripts/lab.py)
- [projects/beginner/sequence-alignment/README.md](../../projects/beginner/sequence-alignment/README.md)

## 24. Başlanğıc 4. Nəticə qovluğunun xəritəsi

### Slaydın mətni

- suite.json
- Status və layihə yolları
- alignment.log
- İcranın gedişi
- run.json
- Parametr və mənşə
- Layihə çıxışları
- Cədvəl və elmi nəticələr
- Faktiki layihə qovluqları suite.json daxilində run_paths sahəsində göstərilir.

### Tam əmr nümunəsi

```text
suite.json  → status və run_paths
alignment.log  → icranın gedişi
run.json  → parametr və mənşə
Layihə qovluğu  → cədvəl və digər çıxışlar
```

**Danışıq qeydi:** Suite qovluğu çoxlu layihənin idarəetmə hesabatını saxlayır, elmi nəticələrin hamısı həmin qovluğun içində olmaya bilər. projects daxilindəki run_paths faktiki layihə qovluqlarına işarə edir. Run metadata-si girişlər və icra haqqında məlumat verir. Saxlanmış nəşr edilmiş nəticələrin bütövlüyü check_all_results.py ilə ayrıca yoxlanır. Status complete olması bioloji şərhin avtomatik düzgün olması deyil.

**Mənbələr:**

- [scripts/lab.py](../../scripts/lab.py)
- [src/biolab/reporting.py](../../src/biolab/reporting.py)
- [results/README.md](../../results/README.md)

## 25. Başlanğıc 5. Offline və tam icra

### Slaydın mətni

- 8 layihə
- Data endirmədən
- run all --offline
- 12 layihə
- Research paketləri
- və internet ilə
- run all
- Tam əmrlər şəkilli bələdçidədir. Xam FASTQ workflow-ları ayrıca Linux/WSL mühiti tələb edir.

### Tam əmr nümunəsi

```text
python scripts/lab.py run all --offline

python -m pip install -e ".[dev,research]"
python scripts/lab.py run all
```

**Danışıq qeydi:** Offline suite download tələb edən dörd layihəni buraxır və skipped siyahısını saxlayır. Tam suite dataset fetch addımlarını icra edir. Endirmə xətası baş verdikdə səbəbi log-dan yoxlamaq lazımdır. Notebook-ların yenidən icrası real girişləri əvvəlcədən tələb edə bilər. Xam sequencing üçün workflows/README və SETUP-da ayrıca quraşdırma yolu verilir.

**Mənbələr:**

- [SETUP.md](../../SETUP.md)
- [scripts/lab.py](../../scripts/lab.py)
- [workflows/README.md](../../workflows/README.md)

## 26. İlk layihədən öz tədqiqat sualınıza

### Slaydın mətni

- İşlədin.
- Şərh edin.
- Yoxlayın.
- Başlanğıc
- docs/START_HERE.md
- Töhfə qaydaları
- CONTRIBUTING.md
- github.com/ali-novruz/bioinformatics-lab

### Tam əmr nümunəsi

```text
python -m pytest
python scripts/check_repository.py
python scripts/check_all_results.py

Töhfə qaydaları: CONTRIBUTING.md
```

**Danışıq qeydi:** Yeni layihə qeydiyyatı, sənədləşmə və testlər birlikdə dəyişməlidir. Tarixi nəticələri yeni kodla səssizcə əvəz etməyin. README və lokal link yoxlamaları yeni sənədlərin tapılmasını təmin edir. Testlərdən keçmək tədqiqatın tam doğrulanması deyil, mühəndislik yoxlamasıdır. Təqdimatı bağlayarkən konkret çağırış verin: alignment nümunəsini işlədib nəticə qovluğundan istifadə olunan metod və input-u tapmaq.

**Mənbələr:**

- [CONTRIBUTING.md](../../CONTRIBUTING.md)
- [scripts/check_repository.py](../../scripts/check_repository.py)
- [scripts/check_all_results.py](../../scripts/check_all_results.py)
