# HPO və Monarch

## Nəyi saxlayır

HPO və Monarch phenotype ontology and cross-species disease–gene–phenotype integration üçün istifadə olunur. Əsas vahidlər: HP term, disease/gene identifiers, evidence and provenance.

## Giriş və versiyalama

Giriş yolu: HPO downloads; Monarch API and knowledge graph. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

Phenotype absence, age of onset, ontology version and negation must be preserved; propagated ancestors are not independent observations.

## Praktiki tapşırıq

Encode a small phenotype profile and rank only after documenting missing/negative terms. Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [HPO və Monarch](https://hpo.jax.org/data/ontology).
