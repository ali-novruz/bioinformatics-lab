# Bioinformatika üçün statistika

### Probability və distributions
Probability qeyri-müəyyənliyi modelləşdirir. Bernoulli variantın var/yox, binomial sabit sayda müstəqil cəhdlərdə allel sayı, Poisson count, negative binomial overdispersed count, normal isə bəzi çevrilmiş davamlı ölçmələr üçün modeldir. Var(count)>mean(count) olduqda Poisson həddən artıq əmin ola bilər.

### Hypothesis testing və p-value
P-value null model və fərziyyələr doğru olduqda müşahidə edilən və ya daha ekstremal statistikanın ehtimalıdır; hipotezin doğru olma ehtimalı deyil. Testi data-ya baxıb seçmək false-positive riskini dəyişir. Kiçik p-value kiçik effektlə də yarana bilər.

### Confidence intervals
95% frequentist interval proseduru təkrar nümunələmədə 95% örtmə hədəfləyir. Bootstrap resampling vahidi müstəqil donor olmalıdır, donor daxilindəki hüceyrələr deyil. WDBC test-set AUROC intervalı yalnız sabit modelin həmin split üzrə qeyri-müəyyənliyidir; training/split variasiyasını əhatə etmir.

### Multiple testing
Bonferroni α/m family-wise error üçün sadə sərt düzəlişdir. Benjamini–Hochberg p-ləri sıralayır, qᵢ=minⱼ≥ᵢ(m·pⱼ/j), sonra 1-də kəsir. Uyğun independence/positive dependence şərtlərində FDR, yəni false discovery proportion-un gözlənilən qiyməti nəzarətdədir; hər seçilmiş genin 5% səhv ehtimalı deyil. `src/biolab/statistics.py` bu alqoritmi və input validation-u verir.

### Correlation, regression, ANOVA
Pearson linear əlaqə, Spearman rank monotonic əlaqə ölçür. Confounding korrelyasiyanı dəyişə bilər. Regression outcome-u predictor və covariate-lərlə əlaqələndirir. ANOVA uyğun linear modeldə qrup mean-lərinin bərabərliyini yoxlayır; residual və variance assumptions yoxlanmalıdır. RNA count-ları üçün avtomatik normal ANOVA seçməyin.

### Bayesian statistics
Posterior ∝ likelihood × prior. Prior biological məlumatı ifadə edə bilər; sensitivity analysis vacibdir. Beta-binomial model allel payının qeyri-müəyyənliyini göstərmək üçün sadə nümunədir. Credible interval seçilmiş prior və modelə şərtlidir.

### Təcrübə
10,000 null p-value simulyasiya edib nominal p<0.05 və BH q<0.05 discovery sayını müqayisə edin; bir run nəzəri zəmanəti sübut etmir. Bir gen üçün group means, effect size, CI və q-value-ni birlikdə yazın. Yeni sual: batch covariate daxil ediləndə effect direction dəyişirmi?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
