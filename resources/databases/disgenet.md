# DisGeNET

## Nəyi saxlayır

DisGeNET gene/variant–disease associations aggregated from curated and literature sources üçün istifadə olunur. Əsas vahidlər: gene, variant, disease, score, evidence and source.

## Giriş və versiyalama

Giriş yolu: API and licensed/download products. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Text-mined and curated records have different evidential weight; duplicated source claims must not be counted as independent.

## Praktiki tapşırıq

Compare curated-only and all-source rankings for one disease. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [DisGeNET](https://disgenet.com/).
