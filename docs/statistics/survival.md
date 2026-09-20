# Survival analizi

Survival analizi hadisəyə qədər vaxtı modelləşdirir. Hadisə ölüm, residiv və ya müalicəyə cavab ola bilər. İzləmə bitəndə hadisə baş verməyibsə müşahidə **sağdan senzurlanmışdır**; bu, hadisənin heç vaxt olmayacağı demək deyil.

## Əsas obyektlər

- `time`: başlanğıcdan hadisə və ya son izləməyə qədər vaxt;
- `event`: hadisə baş veribsə 1, senzurlanıbsa 0;
- Kaplan–Meier: zaman üzrə hadisəsiz qalma ehtimalının qeyri-parametrik qiyməti;
- log-rank: qrupların bütün izləmə boyunca survival əyrilərini müqayisə edən test;
- Cox modeli: kovariatlarla hazard arasındakı əlaqəni `hazard ratio` kimi verir.

## İş axını

1. Başlanğıc nöqtəsini, hadisəni və senzurlama qaydasını əvvəlcədən yazın.
2. İtirilmiş izləməni və qruplar üzrə follow-up müddətini göstərin.
3. Kaplan–Meier əyrisində risk altında olanların sayını verin.
4. Cox modeli üçün proportional-hazards fərziyyəsini Schoenfeld residual-ları ilə yoxlayın.
5. HR, 95% interval və mütləq zaman ölçüsünü birlikdə şərh edin.

`HR=2` median survival-ın iki dəfə qısa olması demək deyil. Competing risk olduqda adi Kaplan–Meier müəyyən hadisənin kumulyativ riskini şişirdə bilər; cumulative-incidence yanaşması seçilməlidir. Biomarker həddini eyni cohort-da seçib nəticəni həmin cohort-da qiymətləndirmək optimist nəticə yaradır.

## Mini nümunə

```python
from lifelines import CoxPHFitter

# df sütunları: time, event, treatment, age
model = CoxPHFitter().fit(df, duration_col="time", event_col="event")
model.check_assumptions(df)
model.print_summary()
```

Bu kod yalnız model skeletidir. Klinik nəticə üçün endpoint tərifi, confounder planı, missing-data siyasəti və xarici validasiya lazımdır. [TCGA-CDR qeydi](../../research/papers/tcga-cdr.md) endpoint seçiminin niyə vacib olduğunu göstərir.
