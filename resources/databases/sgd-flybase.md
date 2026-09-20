# SGD və FlyBase

## Nəyi saxlayır

SGD və FlyBase model-organism genes, alleles, phenotypes and functional annotation üçün istifadə olunur. Əsas vahidlər: stable gene/allele IDs, GO evidence, strain and publication.

## Giriş və versiyalama

Giriş yolu: official APIs/downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Orthology does not transfer phenotype automatically; species, strain, evidence code and release remain explicit.

## Praktiki tapşırıq

Trace one yeast GO-slim gene and one Drosophila Pasilla identifier to current records. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [SGD və FlyBase](https://www.yeastgenome.org/webservice/doc).
