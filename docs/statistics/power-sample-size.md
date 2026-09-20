# Güc və nümunə sayı

Statistik güc həqiqi effekt olduqda onu seçilmiş qayda ilə aşkarlamaq ehtimalıdır. Nümunə sayı effect size, variasiya, dizayn, alfa, çoxlu test və itki faizi ilə birlikdə planlanır.

## Planlama ardıcıllığı

1. Əsas outcome və primary contrast-ı seçin.
2. Bioloji baxımdan minimum vacib effekti yazın.
3. Pilot və ya yaxın cohort-dan dispersiya götürün; pilot effekti həqiqət kimi qəbul etməyin.
4. Batch, pairing, dropout və balanssız qrup ehtimalını simulyasiyaya daxil edin.
5. Çoxlu test və gözlənilən keyfiyyətsiz nümunələr üçün plan qurun.
6. Bir neçə ssenarinin power əyrisini göstərin.

RNA-seq üçün read depth bioloji replikatın yerini tutmur. Dərinlik aşağı count-ları sabitləşdirə bilər, amma donorlar arası dəyişkənliyi öyrənmir. ML-də “sample size” yalnız sətir sayı deyil: müstəqil donor sayı, sinif balansı və xarici test cohort-u əsasdır.

## Simulyasiya skeleti

```python
for n_per_group in (6, 10, 20, 40):
    detections = [simulate_and_test(n_per_group, effect=0.8) for _ in range(1000)]
    print(n_per_group, sum(detections) / len(detections))
```

Simulyasiya funksiyası real count distribution, dispersion, covariate və analiz pipeline-ını təqlid etməlidir. Nəticəni tək rəqəm yox, fərziyyə diapazonu kimi təqdim edin.
