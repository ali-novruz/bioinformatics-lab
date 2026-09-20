# GENCODE və RefSeq

## Nəyi saxlayır

GENCODE və RefSeq reference gene/transcript annotation üçün istifadə olunur. Əsas vahidlər: gene, transcript, exon, protein and versioned accession.

## Giriş və versiyalama

Giriş yolu: GTF/GFF, FASTA and APIs. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

GENCODE and RefSeq models differ; mixing transcript IDs or stripping version suffixes can create silent mismatches.

## Praktiki tapşırıq

Join a count table to one annotation release and report unmatched/version-collapsed IDs. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [GENCODE və RefSeq](https://www.gencodegenes.org/pages/data_format.html).
