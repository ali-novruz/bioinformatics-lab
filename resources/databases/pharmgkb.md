# PharmGKB

## Nəyi saxlayır

PharmGKB gene–drug and variant–drug pharmacogenomic knowledge üçün istifadə olunur. Əsas vahidlər: variant annotation, clinical annotation, guideline and pathway.

## Giriş və versiyalama

Giriş yolu: website, API and licensed downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

A guideline recommendation depends on diplotype, phenotype translation and jurisdiction; single SNP lookup is insufficient.

## Praktiki tapşırıq

Trace one CPIC-linked gene from allele definition to dosing recommendation and list missing patient context. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [PharmGKB](https://www.pharmgkb.org/page/webServices).
