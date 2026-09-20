# Pfam

## Nəyi saxlayır

Pfam profile-HMM protein families and domains üçün istifadə olunur. Əsas vahidlər: family accession, seed/full alignment, HMM and clan.

## Giriş və versiyalama

Giriş yolu: InterPro/Pfam website and HMM downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

A domain hit needs gathering threshold, alignment coverage and composition checks; E-value alone is not function proof.

## Praktiki tapşırıq

Run an HMM search on a small protein set and inspect borderline coverage. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [Pfam](https://pfam-docs.readthedocs.io/).
