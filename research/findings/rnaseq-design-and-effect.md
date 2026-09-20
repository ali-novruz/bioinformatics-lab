# RNA-seq dizaynı, batch və effekt

## Sual

Kiçik real RNA-seq nümunəsində modelin verdiyi diferensial ifadə siqnalı hansı dizayn və input sərhədləri daxilində şərh edilə bilər?

## Müşahidə

GSE110004 subsample analizində 6 nümunə və 84 modelə daxil olan gen üzrə 1 FDR discovery saxlanılıb. Nəticə [custom RNA summary](../../results/research-audit/custom-rnaseq/summary.json) və run provenance-də qeyd olunur. Ayrı pasilla count layihəsi real sayımlar üzərində işləyir, lakin raw FASTQ-dan tam pasilla reproduksiyası deyil.

## Şərh

Modelin çıxışı seçilmiş contrast, design matrix, filtr və subsample-a şərtlidir. Effekt istiqaməti, ölçüsü, intervalı və q-value birlikdə verilməlidir. Sequencing type və batch treatment ilə qarışırsa model əmsalı bioloji və texniki təsiri təmiz ayıra bilməz.

## Məhdudiyyət

Altı nümunə kompleks interaction və donor variasiyasını etibarlı ayırmaq üçün azdır. 84 gen bütün transkriptomu təmsil etmir. Bir discovery mexanizm və ya klinik biomarker sübutu deyil. Sample-level QC, batch visualization və xarici cohort olmadan ümumiləşdirmə edilməməlidir.

## Növbəti eksperiment

Tam count matrisi üçün əvvəlcədən yazılmış design istifadə edin; batch daxil/istisna modellərinin effect istiqaməti və intervalını müqayisə edin. PCA və sample correlation ilə outlier-ləri göstərin, nəticəni müstəqil dataset-də eyni contrast-la yoxlayın. [Power planı](../../docs/statistics/power-sample-size.md) bioloji replikat sayını seçmək üçün çərçivə verir.
