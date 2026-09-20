# Tənqidi tədqiqat auditi — 2026-09-16

> Bu sənəd 2026-09-16 tarixli dondurulmuş auditdir. 2026-09-20 lisenziya, CLI, lock/CI, 13-cü layihə, notebook və geniş məzmun dəyişiklikləri üçün [cari vəziyyətə](../STATUS.md) baxın.

## Qiymətləndirmə və əhatə

Başlanğıc revision: `fda0c35f0930dbc794eec1a8ac9076bafd4b0d8d`.
Repo işlək tədris laboratoriyasıdır; müstəqil bioloji kəşfi və klinik etibarlılığı
təsdiqləyən tədqiqat sistemi səviyyəsinə hələ çatmır. Əsas çatışmazlıq yeni mövzu
sayının azlığı deyil: mövcud nəticələrin sabitliyi və sübut sərhədidir.

[Başlanğıc inventarı](../results/research-audit/baseline-inventory.json) bütün
izlənən faylların ölçü/hash qeydlərini, Python funksiyalarını və notebook
metadatasını saxlayır. 43 Python faylı sintaktik təhlil edildi; mənbə modulları,
CLI, analiz/endirmə/yoxlama skriptləri, testlər, workflow və konfiqurasiya
əlaqələri nəzərdən keçirildi. Layihə, dataset, eksperiment, research, roadmap,
resurs və dərs sənədləri nəticə statusları ilə tutuşduruldu. Yeddi mövcud
notebook-un kod və izahları yoxlandı; əvvəlki şəkillər və nəticə manifestləri
auditin girişidir. Yeni nəticələr ayrıca saxlanır.

İnventarlaşdırma bütün məzmunun eyni dərinlikdə ekspertizasını ifadə etmir:
böyük kitab PDF-lərinin bütün səhifələri yenidən oxunmayıb; onların bütövlüyü,
mənbə/lisenziya qeydi və əvvəlki seçilmiş bölmə təhlilləri yoxlanıb. İlkin
məqalələr yenidən tam sistematik ədəbiyyat axtarışına çevrilməyib. Git-dən kənar
xam girişlər öz sabit manifestləri və faktiki icralarla yoxlanır.

## On iki baxışın ayrı nəticəsi

Bu cədvəl bir audit daxilində tətbiq edilən 12 baxışdır; 12 müstəqil insanın
peer review-u və ya 12 ayrıca agentin rəyi kimi təqdim edilmir.

| Baxış | Əsas müşahidə | Qərar |
|---|---|---|
| Bioinformatika tədqiqatçısı | GO nəticəsi yalnız chrI alt dəstinə və bir seçilmiş genə əsaslanır | Eyni universe və annotasiya ilə statistik çatımlılığı hesabla |
| Skeptik elmi rəyçi | İşlək pipeline nəticəsi məqalə reproduksiyasını göstərmir | Demo, real analiz, protokol və xarici validasiyanı ayrı saxla |
| Statistik | Seçilmiş CV score optimist ola bilər; sıfır discovery məlumat çatışmazlığından gələ bilər | İç-içə CV, tam seçimli permutation və exhaustive GO control |
| ML tədqiqatçısı | Khan n=63, p=2308; əvvəlki 20 test nümunəsi artıq müşahidə olunub | Yeni auditdə test fayllarını açmadan training-only qiymətləndir |
| Proqram arxitektoru | Modullar faydalıdır, lakin registry yoxlanmır və suite nəticəyə bağlanmır | Kiçik registry validator və birbaşa run receipts əlavə et |
| Təkrar icra mühəndisi | Köhnə source hash-ləri qorunur; command/runtime/output hash boşluğu var | Mənbə arxivi, run möhürlənməsi və output yoxlaması |
| Data mühəndisi | Eyni gene ID fərqli koordinat/strand/length ilə birləşə bilər | Tam annotasiya müqayisəsi, string ID və sərt integer sayımlar |
| DevOps mühəndisi | Hər dəyişiklikdə xarici data/alətlər tələb edən yoxlama var | Offline Python matrix; main/manual integration və Linux smoke ayrı jobs |
| Test mühəndisi | Məlum-cavab testləri yaxşı başlanğıcdır; CLI/provenance xətaları əskikdir | Boş nəticə, duplicate ID, annotation mismatch, hash corruption regressiyaları |
| Tədris dizayneri | İdeya/protokol çoxdur; notebook-ların bəzisi saxlanmış nəticəni oxuyur | İcra və readback fərqini göstər; yeni control notebook-da hesabı yoxla |
| Adversarial rəyçi | Custom RNA qrafiki yanlış dataset/dizayn adı yaza bilir | Başlığı actual input-a bağla, məqsədli regression testi əlavə et |
| Yaradıcı tədqiqatçı | Yüksək prediction score ilə qeyri-sabit feature seçimi yanaşı ola bilər | Probe sabitliyini ölç; növbəti falsifiable sualı çıxart |

**Sintez:** əvvəl məlumat/model semantikasını qorumaq, sonra mövcud iddianı
nəzarət sınağı ilə zəiflətməyə çalışmaq, yalnız bundan sonra yeni omics layihəsi
seçmək daha əsaslıdır. İki audit təcrübəsi 12 layihənin davamıdır; layihə sayını
artırmaq üçün başqa adla təkrar layihə yaradılmayıb.

## Gap və prioritet xəritəsi

Impact/risk/effort aşağı, orta, yüksək kimi nisbi qiymətləndirmədir; saat və ya
formal risk modeli deyil. P1 bu auditdə tətbiq edildi; P2/P3 açıq qalan işdir.

| Kateqoriya və gap | Impact | Risk | Effort | Prioritet / vəziyyət |
|---|---|---|---|---|
| Scientific: discovery ilə assay/bioloji təsdiq arasında boşluq | yüksək | yüksək | yüksək | P2; açıq, scope dəqiqləşdirildi |
| Statistical: GO singleton üçün attainable FDR bilinmir | yüksək | orta | aşağı | P1; tam sayma icra edildi |
| Bioinformatics: eyni ID ilə uyğunsuz annotasiya merge edilə bilər | yüksək | yüksək | aşağı | P1; rədd edilir |
| Dataset: Khan donor/batch və upstream preprocessing məlum deyil | yüksək | yüksək | yüksək | P2; yeni data/metadata tələb edir |
| Validation: selected CV score və feature stability | yüksək | yüksək | orta | P1; nested CV + 99 permutation + Jaccard |
| Architecture: registry və nəticə əlaqəsi boşluğu | orta | orta | aşağı | P1; validator + receipts |
| Testing: səhv metadata və partial output uğur görünə bilər | yüksək | yüksək | aşağı | P1; mənfi regression testləri |
| Reproducibility: runtime/command/output hash yoxdur | yüksək | orta | orta | P1; suite/control lifecycle |
| Documentation: hazır layihə, gələcək protokol və köhnə audit rəqəmləri qarışa bilər | orta | orta | aşağı | P1; tarixli audit, cari girişlər və scope |
| Education: nəticəyə baxış həmişə modeli yenidən fit etmir | orta | orta | aşağı | P1; açıq readback qeydi və nəzarət notebook-u |
| Visualization: custom RNA plot-da sabit Pasilla adı | yüksək | yüksək | aşağı | P1; dataset/design parametrinə keçirildi |
| Automation: downloads/Conda bütün PR-lərə bağlanıb | orta | orta | aşağı | P1; offline və integration ayrıldı |
| Research questions: protokolların çoxunda accession/primary metric seçilməyib | yüksək | orta | orta | P1 iki sualda; qalanları P2 |
| Scale: full genome/böyük cohort memory və runtime benchmark yoxdur | orta | orta | yüksək | P3; mövcud kiçik scope saxlanır |

## Konkret ziddiyyətlər və düzəlişlər

- `scripts/analyze_counts.py` custom input qəbul edirdi, `plot_expression` isə
  həmişə Pasilla/type+condition yazırdı. Dataset adı və design indi ötürülür.
- Count merge gen adlarını tutuşdururdu, koordinatları yox. İndi Chr/Start/End/
  Strand/Length birlikdə yoxlanır; sıralama dəyişməsi qəbul edilir, annotasiya
  dəyişməsi rədd edilir. Fractional featureCounts bu raw-integer modeldə
  dəstəklənmir və səssiz yuvarlaqlaşdırılmır.
- Suite `exit_code=0` saxlayırdı, konkret analiz nəticəsini göstərmirdi. İndi
  command, vaxt, log və run_paths var; nəticə qeyd etməyən script uğurlu sayılmır.
- Köhnə README yalnız ilk iki offline layihəni qeyd edirdi; actual registry-də
  səkkizdir. İcra girişləri və CI təsviri yeniləndi.
- Roadmap expression layihəsini yalnız protokol kimi təsvir edirdi; actual
  Khan implementasiyası və onun nəzarət təcrübəsi keçid meyarına bağlandı.

## Scientific nəticə və özünü tənqid

[Ətraflı təcrübə qeydi](../experiments/controls/README.md) və
[saxlanmış sübut](../results/research-audit/README.md).

1. GO: 84 possible singleton × 62 eligible term; heç bir seçim BH<0.05 vermir.
   Minimum attainable adjusted p=0.2767857. Deməli mövcud sıfır discovery-ni
   yalnız ümumi “low power” sözü ilə izah etmək əvəzinə, bu sabit dizaynda
   singleton discovery-nin alınmadığını birbaşa göstərə bilirik. Bu hesab
   real bioloji effect-size power analizi və ya yolun fəaliyyətsizliyi sübutu deyil.
2. Khan: outer-fold balanced accuracy orta 0.99, fold-lar 0.95–1.00; dummy 0.25.
   Tam pipeline yenidən fit edilən 99 label permutation-da orta 0.241936,
   mərkəzi 95% null intervalı 0.1375–0.362125; Monte Carlo p=0.01.
   Bu, yüksək score-un sadəcə random labels altında asan alınmadığını göstərir.
   0.01 testin ən kiçik mümkün p-dəyəridir; daha dəqiq p iddiası yoxdur.
3. Seçilmiş probe sayları 25/500/100/100/25; orta pairwise Jaccard 0.2569.
   Seçim ölçüləri fərqlidir, outer training dəstləri üst-üstə düşür. Bu metrik
   gene-level sabit biomarker təsdiqi deyil, həmin təsdiqin çatışmadığını göstərir.

Nəticəni görüb k/C grid, alfa və foreground həddi dəyişdirilmədi. Protokol yeni
icradan əvvəl yazıldı, lakin əvvəlki benchmark məlum idi: bu post-hoc auditdir,
prospektiv preregistration deyil. Fold fərqləri CI kimi etiketlənmir. Label
exchangeability unknown donor dependence olduqda pozula bilər. Köhnə 20-sample
test nəticəsi bu yeni sınağın müstəqil xarici validasiyasına çevrilmir.

## Təkrar icra və proqram keyfiyyəti

`src/biolab` daxilində yeni sərhədlər kiçikdir: counts, registry, health,
sensitivity. Əvvəlki layihə əmrləri və plot defaults saxlanır. Yeni run.json
Python/paket/OS/git/input/source yanında command saxlayır. Suite və
`recorded_run` istifadə edən girişlər status, müddət və output hash-ləri də
yazır. Daha köhnə standalone girişlər lifecycle-ə tam köçürülməyib; onların
metadata-sı yeni suite vasitəsilə tamamlanır. Qəfil process kill zamanı
başlanmış suite.json qala bilər; recovery/resume scheduler qurulmayıb.

`check_repository.py` artıq registry paths/types/IDs, example metadata/hash,
research node/edge əlaqələri və dövrələri yoxlayır. `check_all_results.py`
köhnə source archive-lərini, yeni möhürlənmiş output-ları və snapshot-ları
yoxlayır. Hash dəyişmə detektorudur; saxtalaşdırmaya qarşı rəqəmsal imza deyil.

Python 3.11/3.12 offline jobs lint, test, repository/snapshot, səkkiz layihə və
GO control işlədir. Main push/manual integration bütün 12 layihəni və
notebook-ları təmiz checkout-da işlədərək endirmə problemlərini ayrıca göstərir.
Manual `controls=true` 99-permutation sınağını da işlədə bilər. Linux FASTQ smoke
ayrı job olaraq qalır. Geniş statik type-check bu dəyişiklikdə tətbiq edilməyib;
type safety-nin təmin olunduğu iddia edilmir.

## Növbəti ən yüksək dəyərli beş iş

Yekun local validation: **57 test**, correctness lint, **12/12 layihə**,
**8/8 notebook hesablaması**, qalereya, registry/data/graph və bütün snapshot
yoxlamaları keçdi. Custom RNA düzəlişi real altı-sample yeast counts ilə də
işlədildi. [Machine-readable validation](../results/research-audit/validation.json)
Windows Jupyter shutdown mesajlarını və hesablamaların vəziyyətini ayrıca saxlayır.

1. Khan üçün təsdiqlənmiş probe-gene mapping və donor/batch metadata tapmaq;
   uyğun cohort varsa modeli yeni seçim etmədən xarici validasiyadan keçirmək.
2. Pasilla-da əvvəlcədən yazılmış design ablation: `~ condition` ilə
   `~ type + condition` effect istiqamətini və FDR sabitliyini müqayisə etmək.
3. Yeast-də eyni universe/annotasiya prinsipi ilə tam transcriptome dataset-i
   işlətmək; nəticə sayını artırmaq üçün mövcud alfa həddini dəyişməmək.
4. Variant workflow-a eyni reference/confident-region üzrə həqiqi truth-set
   precision/recall əlavə etmək; hazır tiny fixture-ni klinik benchmark saymamaq.
5. Bir accession-u seçilmiş advanced protokolu external-validation planı ilə
   tamamlamaq; yeni ümumi protokolların sayını artırmağı dayandırmaq.
