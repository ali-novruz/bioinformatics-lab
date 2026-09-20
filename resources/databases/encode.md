# ENCODE

## Nəyi saxlayır

ENCODE functional genomics assays, biosamples and processed tracks üçün istifadə olunur. Əsas vahidlər: experiment, biosample, assay, file, assembly and audit flags.

## Giriş və versiyalama

Giriş yolu: REST API, portal and cloud downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Replicate structure, antibody validation, blacklist filtering, assembly and revoked files are essential metadata.

## Praktiki tapşırıq

Select one ChIP-seq experiment using audit status and biological replicate rules before downloading. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [ENCODE](https://www.encodeproject.org/help/rest-api/).
