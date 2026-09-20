# Khan təsnifatında etiket qarışdırma nəzarəti

## Sual

Khan gene-expression təsnifatındakı yüksək score real etiket siqnalı ilə uyğun gəlirmi, yoxsa kiçik data və feature seçimi eyni nəticəni təsadüfən yarada bilər?

## Müşahidə

Nested cross-validation balanced accuracy-ni **0.99** verdi; dummy baseline **0.25** idi. Etiketlərin 99 dəfə qarışdırılmasında orta balanced accuracy **0.241936**, müşahidə olunan nəticə üçün empirik `p=0.01` oldu. Outer fold score-ları 1, 0.95, 1, 1 və 1-dir.

Tam rəqəmlər [summary.json](../../results/research-audit/expression-control/summary.json), fold indeksləri və seçilmiş xüsusiyyətlər [folds.json](../../results/research-audit/expression-control/folds.json), bütün null nəticələr isə [permutations.csv](../../results/research-audit/expression-control/permutations.csv) faylındadır.

## Şərh

Müşahidə olunan ayrılma bu dataset daxilində qarışdırılmış etiket baseline-ından güclüdür. Bu nəzarət pipeline-ın sadəcə sinif balansını əzbərləməsi izahını zəiflədir. Bununla belə, feature selection sabitliyi aşağıdır: fold-lar üzrə orta Jaccard **0.256909**, seçilmiş probe sayı isə 25–500 arasında dəyişir. Proqnoz score-u sabit görünsə də biomarker siyahısı sabit deyil.

## Məhdudiyyət

99 permutation mümkün ən kiçik empirik p-value-ni 0.01 ilə məhdudlaşdırır. Data eyni tədqiqatdandır; platforma, laboratoriya və populyasiya dəyişməsi yoxlanılmayıb. Nəticə klinik diaqnostika, erkən skrininq və ya konkret probe-un səbəb əlaqəsi üçün sübut deyil.

## Növbəti eksperiment

Probe xəritəsini versiyalı annotasiya ilə gen səviyyəsinə çıxarın, modeli toxunulmamış xarici cohort-da əvvəlcədən dondurulmuş parametrlərlə sınayın və calibration, class-specific recall və batch üzrə stratifikasiya verin.
