# Human Cell Atlas Data Portal

## Nəyi saxlayır

Human Cell Atlas Data Portal single-cell datasets with donor, tissue and assay metadata üçün istifadə olunur. Əsas vahidlər: project, donor, specimen, cell suspension, library and file.

## Giriş və versiyalama

Giriş yolu: portal, API and cloud manifests. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Cells are nested within donors; access restrictions, consent, batch and ontology versions must follow the files.

## Praktiki tapşırıq

Construct a donor-level pseudobulk design from portal metadata without treating cells as replicates. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [Human Cell Atlas Data Portal](https://data.humancellatlas.org/apis).
