# Mövcud iddiaları sınayan iki nəzarət təcrübəsi

**Status:** 2026-09-16-da icra edilib. Əvvəlki nəticələrin post-hoc robustness
auditidir. [Dondurulmuş parametr faylı](protocol.json),
[nəticələr](../../results/research-audit/README.md),
[research əlaqələri](../../research/graph.json).

## CONTROL-GO-001: bir gen seçildikdə BH discovery mümkündürmü?

**Hipotez:** cari 84-gen universe və 62 eligible GO-slim biological-process
term ailəsində ən azı bir mümkün singleton foreground BH<0.05 verə bilər.
**Təkzib meyarı:** bütün 84 seçimi hesablayanda heç birində discovery yoxdur.

Giriş: dondurulmuş real yeast raw RNA differential_expression.csv və
2026-09-16 SGD GO-slim çıxarışı. Source/input hash və file bytes run.json-dadır.
Universe finite padj genləridir, unannotated genlər saxlanır; min term size=2,
universe-in bütün genlərini tutan term çıxarılır. Hər singleton üçün bütün
eligible term-lərdə hypergeometric upper tail və BH yenidən hesablanır.
Tam sayma olduğundan random seed və Monte Carlo qeyri-müəyyənliyi yoxdur.

**Nəticə:** 84/84 mümkün seçimdə sıfır discovery. Minimum adjusted p=0.2767857;
observed YAL005C də həmin minimumu verir. Bu konfiqurasiyada bir-gen discovery
hipotezi təkzib olundu. Bunu pathway “aktiv deyil” nəticəsi kimi oxumaq olmaz.
Term dependence və annotation coverage dəyişəndə cavab dəyişə bilər.

**Növbəti sual:** daha geniş, əvvəlcədən seçilmiş measured universe-də nəticə
annotation coverage-ə həssasdırmı? Yeni data ayrıca versiyalanmalıdır.

## CONTROL-ML-001: seçim daxil olmaqla yüksək score təsadüfdən ayrılırmı?

**Null:** 63 training nümunəsində label-lar feature-lərdən müstəqildir;
label permutation class counts-u saxlayır. **Statistika:** beş outer fold-un
balanced accuracy ortası. **Qərar:** exploratory p<=0.05. Bu ayrı GO testi ilə
vahid klinik/təsdiqləyici hypothesis family kimi təqdim edilmir.

Data: ISLP revision `a1f4e43ca88d4c9a6f186930181d628b9270015d`, 63×2308
processed microarray matrisi, class sayları 8/23/12/20. Yalnız xtrain və ytrain
oxunur və pinned manifestə qarşı hash yoxlanır. Test CSV-ləri bu control
skripti tərəfindən açılmır; ilk fetch onların da cache-ini yarada bilər.

Seed=20260916, outer=5, inner=3. Variance filter → ANOVA k selection → scaling
→ class-weighted LinearSVC hər training fold-da öyrənilir. k=[25,100,500],
C=[0.01,0.1,1]. Inner search outer validation məlumatına çıxmır. Hər 99
permutation-da bütün outer/inner seçim və preprocessing yenidən qurulur.
`p=(1 + null>=observed sayı)/(99+1)`. Permutation label-ları, train/validation
indeksləri, seçilən features və model parametrləri saxlanır.

**Nəticə:** mean outer balanced accuracy=0.99; dummy=0.25, fərq=0.74.
Fold-lar 1.00/0.95/1.00/1.00/1.00. Null mean=0.241936,
central 95% null range=0.1375–0.362125, p=0.01. Mean selection Jaccard=0.256909.
Raw feature indeksləri 0-based, V sütun kimliklərinə aiddir, gene symbol deyil.

**Alternativ izah:** tarixi dataset-in upstream processing/duplicate donor
strukturunu bu fayllardan təsdiqləmək mümkün deyil. Yüksək discrimination
sabit gene marker, calibration və ya screening utility göstərmir. Null
intervalı klinik performance CI deyil; outer fold-lar müstəqil təkrar cohort deyil.

**Növbəti falsifiable sual:** eyni k sabit saxlandıqda yüksək accuracy ilə aşağı
probe sabitliyi yenə qalırmı? Əvvəlcədən k və resampling dizaynı yazılacaq;
bu sual cari test dəstində əlavə tuning icazəsi vermir.

## Təkrar icra

Repo kökündə paket quraşdırıldıqdan sonra:

```bash
python scripts/run_controls.py --experiment enrichment
python scripts/fetch_khan.py
python scripts/run_controls.py --experiment expression
```

İki təcrübəni birlikdə: `python scripts/run_controls.py --experiment all`.
Giriş yoxdursa expression control açıq xəta verir; özü internetə çıxmır.
Parametrlər [protocol.json](protocol.json)-da əvvəlcədən yazılır. Nəticə qovluğu
yeni timestamp/ID alır; köhnə nəticə silinmir. Command, runtime, packages,
source/input hashes, cədvəl/şəkil output hashes və complete/failed status
run.json-da saxlanır. Son notebook statistikaları saxlanmış cədvəldən
yenidən hesablayır; 99-permutation fit-i notebook-da təkrar etmir.
