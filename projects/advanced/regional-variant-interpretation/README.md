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
