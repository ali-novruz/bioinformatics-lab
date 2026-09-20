# Open Targets

## Nəyi saxlayır

Open Targets target–disease evidence integration for drug discovery üçün istifadə olunur. Əsas vahidlər: target, disease, evidence source, association score and tractability.

## Giriş və versiyalama

Giriş yolu: GraphQL API, platform and downloads. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

The aggregate score is a prioritization aid, not a causal effect or clinical efficacy probability.

## Praktiki tapşırıq

Decompose one target score by evidence source and remove one source as a sensitivity analysis. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [Open Targets](https://platform-docs.opentargets.org/data-access).
