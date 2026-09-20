# DepMap

## Nəyi saxlayır

DepMap cancer-cell-line dependency, expression, mutation and drug-sensitivity data üçün istifadə olunur. Əsas vahidlər: cell line, gene effect, model metadata and release.

## Giriş və versiyalama

Giriş yolu: portal and release downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Cell-line identity, lineage, batch and release are confounders; dependency score is not patient response.

## Praktiki tapşırıq

Test whether a dependency remains after lineage stratification. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [DepMap](https://depmap.org/portal/download/).
