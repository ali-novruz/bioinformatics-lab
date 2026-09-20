# gnomAD

## Nəyi saxlayır

gnomAD population allele frequency, coverage and constraint üçün istifadə olunur. Əsas vahidlər: variant, gene and ancestry-aware frequency fields.

## Giriş və versiyalama

Giriş yolu: GraphQL/API, browser and release downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Absence is not proof of pathogenicity; ancestry, coverage, sex chromosome ploidy and release must be recorded.

## Praktiki tapşırıq

Compare a ClinVar assertion with ancestry-specific frequency without turning frequency into a diagnosis. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [gnomAD](https://gnomad.broadinstitute.org/help).
