# Bayesian analiz

Bayesian model əvvəlki məlumatı `prior`, müşahidə modelini `likelihood`, yenilənmiş qeyri-müəyyənliyi isə `posterior` ilə ifadə edir:

`posterior ∝ likelihood × prior`.

## Sadə allel tezliyi nümunəsi

`k` alternativ allel `n` müşahidədə görülürsə və `p ~ Beta(a,b)` prior seçilirsə, posterior `Beta(a+k, b+n-k)` olur. Posterior interval parametrin seçilmiş model və prior daxilində ehtimal intervalıdır; frequentist confidence interval ilə eyni mənası daşımır.

## Yoxlama siyahısı

- prior-u data-ya baxmadan əsaslandırın;
- zəif, informativ və skeptik priorlarla sensitivity analysis göstərin;
- posterior predictive check ilə modelin data xüsusiyyətlərini yaradıb-yaratmadığını yoxlayın;
- MCMC üçün zəncir, `R-hat`, effective sample size və divergence-ları verin;
- qərarı yalnız posterior mean ilə deyil, interval və praktiki hədlə yazın.

Az nümunədə prior nəticəyə güclü təsir edə bilər. Çox böyük nümunədə statistik dəqiqlik bioloji əhəmiyyəti avtomatik yaratmır. Batch, seçmə və ölçmə xətası likelihood-da modelləşdirilməyibsə posterior dar, amma yanlış ola bilər.

## Hesabat cümləsi

“Model və prior şərti altında effektin 0-dan böyük olma posterior ehtimalı 0.97-dir; 95% credible interval [-0.02, 0.31] olduğu üçün praktiki istiqamət hələ qeyri-müəyyəndir.”

[Statistika modulu](../../src/biolab/statistics.py) frequentist nəzarət nümunələri verir; iki yanaşmanın sualını və şərhini qarışdırmayın.
