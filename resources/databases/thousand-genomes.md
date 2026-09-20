# 1000 Genomes

## Nəyi saxlayır

1000 Genomes global human genetic variation reference panels üçün istifadə olunur. Əsas vahidlər: sample, population, superpopulation, variant and phased haplotype.

## Giriş və versiyalama

Giriş yolu: IGSR FTP, browser and cloud resources. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Population labels are sampling categories, not fixed biological races; GRCh37/38 and panel release must be explicit.

## Praktiki tapşırıq

Calculate allele counts by declared population and discuss uncertainty for small groups. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [1000 Genomes](https://www.internationalgenome.org/data).
