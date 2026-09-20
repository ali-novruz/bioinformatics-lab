# miRBase

## Nəyi saxlayır

miRBase published microRNA sequences and annotation üçün istifadə olunur. Əsas vahidlər: MI precursor and MIMAT mature accessions.

## Giriş və versiyalama

Giriş yolu: website and release FTP. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Names and confidence change between releases; predicted targets are not stored as validated regulatory effects.

## Praktiki tapşırıq

Resolve precursor-to-mature arms with a fixed release and list deprecated IDs. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [miRBase](https://www.mirbase.org/download/).
