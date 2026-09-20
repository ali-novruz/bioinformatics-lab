# InterPro

## Nəyi saxlayır

InterPro integrated protein family, domain and site signatures üçün istifadə olunur. Əsas vahidlər: InterPro entry, member-database signature, protein match and location.

## Giriş və versiyalama

Giriş yolu: REST API and release downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Overlapping signatures are expected; family, domain and active-site matches have different semantics.

## Praktiki tapşırıq

Map an insulin sequence to domains and compare member-database agreement. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [InterPro](https://www.ebi.ac.uk/interpro/api/).
