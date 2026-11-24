# Regional genetika: ClinVar sübutlarının şəffaf triage-ı

Bu işlək advanced layihə MEFV `p.Val726Ala` və HBB `p.Glu7Val` nümunələrindən istifadə edərək variant sübutunun necə oxunduğunu göstərir. Mövzular region üçün aktual ola bilər, lakin iki variant Azərbaycan və ya Qafqaz üzrə yayılma göstəricisi vermir.

## Bioloji sual

ClinVar-dakı aggregate təsnifat, review status, inheritance və population frequency sahələrini klinik qərar vermədən necə prioritetləşdirə bilərik?

## Məlumat və mənşə

[Saxlanmış TSV](../../../datasets/examples/regional/clinvar-2026-09-20.tsv) NCBI ClinVar ESummary cavabından 20 sentyabr 2026-da seçilmiş sahələri saxlayır. Hər sətirdə Variation ID, accession versiyası, HGVS, dbSNP, GRCh38 SPDI, aggregate significance, review status, condition, inheritance qeydi, tezlik, mənbə URL-i və tarix var. ClinVar həftəlik yenilənir; yeni klinik istifadə üçün canlı record yenidən yoxlanmalıdır.

## Metod

`biolab.clinical.prioritize_clinvar` review səviyyəsini açıq 0–4 çəkiyə çevirir və mənbədə “pathogenic” olan aggregate qeydə 3 bal verir. Bal yeni ACMG təsnifatı deyil; yalnız hansı record-un əvvəl oxunacağını göstərir. Zygosity, phenotype uyğunluğu, condition-specific RCV, segregation, functional evidence və laborator təsdiq avtomatik qərara çevrilmir.

```bash
biolab run regional-variants --offline
```

Çıxışda cədvəl, xülasə və prioritet balının qrafiki yaranır. Hər sətirdə sərhəd cümləsi təkrarlanır ki, cədvəl tibbi hesabatla qarışdırılmasın.

## Tədris tapşırığı

1. VCV ilə condition-specific RCV arasındakı fərqi yazın.
2. Eyni variant üçün inheritance konteksti dəyişəndə şərhin niyə dəyişdiyini izah edin.
3. Population frequency-ni ancestry və penetrance nəzərə alınmadan “benign” qaydasına çevirməyin niyə səhv olduğunu göstərin.
4. Cari ClinVar səhifəsini açıb accession versiyası və review status dəyişibsə fərqi qeyd edin.

## Məhdudiyyət

Bu layihə diaqnoz, daşıyıcı skrininqi, fərdi risk, müalicə və ya reproduktiv qərar üçün istifadə edilmir. Regional başlıq xəstəliklərin yerli təhsil əhəmiyyətini bildirir; yerli cohort məlumatı olmadığı üçün prevalence iddiası yoxdur.

## Genişləndirilmiş analiz: MEFV və HBB-nin bütün ClinVar qeydləri

İki nümunədən iki genin bütün ClinVar qeydlərinə keçid. [`scripts/fetch_regional_clinvar.py`](../../../scripts/fetch_regional_clinvar.py) 2026-11-24 tarixli snapshot yaradır: 3458 qeyd (MEFV 1484, HBB 1974) və UniProt domen xəritəsi; hər ikisi [manifestdə](../../../datasets/examples/manifest.json) SHA-256 ilə qeydə alınıb. [`scripts/run_regional_clinvar_showcase.py`](../../../scripts/run_regional_clinvar_showcase.py) yalnız snapshot-u oxuyur. Saxlanmış nəticə: [`results/showcase/regional-clinvar/`](../../../results/showcase/regional-clinvar/).

**Hansı qeydlər genə aiddir?** `LOC` tənzimləyici elementləri nəzərə alınmadan tək genə aid, kiçik (SNV, delesiya, duplikasiya, indel) və kanonik transkriptdə (NM_000243, NM_000518; istənilən versiya) təsvir edilmiş qeydlər: MEFV 1409, HBB 1822. Kənarda qalanlar ayrıca sayılır (çox genli CNV 106, haplotip 41, genomik təsvir 78).

| Sual | MEFV | HBB |
|---|---:|---:|
| P/LP | 25 | 408 |
| Ziddiyyətli | 274 | 101 |
| VUS | 531 | 283 |
| B/LB | 548 | 844 |
| P/LP-dən ≥2 ulduzlu | 10 | 158 |
| Ekspert panel (3 ulduz) P/LP | 0 | 11 |

**Hotspot.** MEFV-nin P/LP missense dəyişikliklərinin 9/13-ü (69%) B30.2/SPRY domenindədir (580–775). Bütün təsnif olunmuş missense-lərdə bu pay 24.5%-dir, yəni ekzon 10-un daha çox ardıcıllaşdırılması tək başına izah etmir: etiket permutasiyası (10 000) p = 0.0013.

**Tezlik ilə təsnifat ziddiyyəti.** P/LP olub gnomAD-da > 0.005 görünən yeganə qeyd HBB `p.Glu7Val`-dır (HbS, 0.013): resessiv xəstəlik üçün yüksək tezlik patogenliyi inkar etmir. Ən geniş yayılmış ziddiyyətli qeyd MEFV `p.Glu148Gln`-dir (0.071).

```bash
python scripts/fetch_regional_clinvar.py         # yeni snapshot (şəbəkə)
python scripts/run_regional_clinvar_showcase.py  # analiz (offline)
```

Hədlər: ClinVar təsnifatı həftəlik dəyişir və burada ACMG qərarı verilmir; gnomAD dəyəri ClinVar-ın göstərdiyi ən yüksək tezlikdir, əcdad bölgüsü yoxdur; təqdimat qərəzi (ascertainment) qismən nəzarət olunur; regional yayılma, daşıyıcılıq riski və diaqnoz iddiası yoxdur.
