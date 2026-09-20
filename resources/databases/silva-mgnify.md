# SILVA və MGnify

## Nəyi saxlayır

SILVA və MGnify ribosomal RNA taxonomy and microbiome analysis resources üçün istifadə olunur. Əsas vahidlər: sequence/taxon identifiers, study/sample accessions and pipeline version.

## Giriş və versiyalama

Giriş yolu: SILVA releases; MGnify API and downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Database release, primer region and classifier alter taxonomy; read abundance is compositional and not absolute biomass.

## Praktiki tapşırıq

Classify a tiny 16S set against one SILVA release and record unclassified reads. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [SILVA və MGnify](https://www.ebi.ac.uk/metagenomics/api/).
