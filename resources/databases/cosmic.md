# COSMIC

## Nəyi saxlayır

COSMIC expert-curated somatic alterations in cancer üçün istifadə olunur. Əsas vahidlər: COSV mutation IDs, genes, samples, tumour site and publication evidence.

## Giriş və versiyalama

Giriş yolu: licensed downloads and web interface. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Coverage and licensing vary by product; mutation recurrence reflects ascertainment and cohort design.

## Praktiki tapşırıq

Audit one TP53 alteration across tumour sites and separate sample count from patient count. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [COSMIC](https://cancer.sanger.ac.uk/cosmic/help).
