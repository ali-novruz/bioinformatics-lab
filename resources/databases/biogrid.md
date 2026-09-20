# BioGRID

## Nəyi saxlayır

BioGRID curated genetic and protein interactions üçün istifadə olunur. Əsas vahidlər: interactor IDs, experimental system, publication and organism.

## Giriş və versiyalama

Giriş yolu: web services and downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Interaction type, assay and evidence count matter; network degree is strongly affected by research popularity.

## Praktiki tapşırıq

Build an assay-stratified subnetwork and compare it with the unfiltered graph. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [BioGRID](https://wiki.thebiogrid.org/doku.php/biogridrest).
