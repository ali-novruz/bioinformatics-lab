# GO singleton mənfi nəzarəti

## Sual

Bir genlik foreground siyahısı bu kiçik yeast universe-də çoxlu test düzəlişindən sonra “əhəmiyyətli enrichment” yarada bilərmi?

## Müşahidə

84 mümkün singleton foreground-un hamısı 62 GO-slim termini üzrə yoxlanıldı. **Heç biri `BH q<0.05` vermədi**; ən kiçik mümkün q-value **0.2767857** oldu. [Tam singleton cədvəli](../../results/research-audit/enrichment-control/singletons.csv) hər gen üçün minimum p/q nəticəsini, [summary](../../results/research-audit/enrichment-control/summary.json) isə universe və term sayını saxlayır.

## Şərh

Bu konkret dizaynda bir seçilmiş genlə FDR discovery almaq riyazi olaraq əlçatmaz görünür. Əsas nəticə “pathway yoxdur” deyil; input siyahısının enrichment nəticəsi çıxarmaq üçün çox zəif olmasıdır. Mənfi nəticə pipeline xətası kimi gizlədilməməlidir.

## Məhdudiyyət

Universe yalnız ölçülmüş 84 gene və SGD GO-slim biological-process annotasiyalarına aiddir. Daha böyük gene set, başqa ontology, weighted metod və fərqli universe başqa nəticə verə bilər. Annotasiya natamamlığı və genlər arasındakı asılılıq ayrıca modelləşdirilməyib.

## Növbəti eksperiment

Əvvəlcədən müəyyən edilmiş effect/q-value həddi ilə daha geniş ranked gene list yaradın. ORA-nı rank-based enrichment ilə müqayisə edin və eyni measured universe-i hər iki metodda qoruyun. [Enrichment modulu](../../src/biolab/enrichment.py) və [vektorlaşdırılmış sensitivity nəzarəti](../../src/biolab/sensitivity.py) bu auditin kod əsasını verir.
