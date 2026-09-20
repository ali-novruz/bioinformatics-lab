# CIViC

## Nəyi saxlayır

CIViC open, community-curated clinical interpretations of cancer variants üçün istifadə olunur. Əsas vahidlər: variant, disease, drug, evidence item, evidence level and assertion.

## Giriş və versiyalama

Giriş yolu: GraphQL/REST API and bulk releases. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Evidence items may disagree and have different evidence levels; snapshot version and review state matter.

## Praktiki tapşırıq

Build an evidence table grouped by disease and evidence level, preserving conflicts. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [CIViC](https://civic.readthedocs.io/).
