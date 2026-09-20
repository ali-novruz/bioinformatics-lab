# Rfam

## Nəyi saxlayır

Rfam non-coding RNA families, covariance models and alignments üçün istifadə olunur. Əsas vahidlər: RF accession, seed/full alignment, covariance model and clan.

## Giriş və versiyalama

Giriş yolu: website, API and FTP. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Covariance-model significance depends on model threshold and sequence composition; family match is not expression evidence.

## Praktiki tapşırıq

Search a short RNA sequence and inspect structure-aware alignment coverage. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [Rfam](https://docs.rfam.org/).
