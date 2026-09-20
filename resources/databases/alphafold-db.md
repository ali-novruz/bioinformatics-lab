# AlphaFold DB

## Nəyi saxlayır

AlphaFold DB predicted protein structures with confidence üçün istifadə olunur. Əsas vahidlər: UniProt accession, model version, pLDDT and PAE.

## Giriş və versiyalama

Giriş yolu: website, API and bulk downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Low pLDDT can reflect disorder; a confident fold does not establish interaction, ligand state or biological function.

## Praktiki tapşırıq

Compare a high-confidence domain and disordered tail, reporting confidence per residue. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [AlphaFold DB](https://alphafold.ebi.ac.uk/api-docs).
