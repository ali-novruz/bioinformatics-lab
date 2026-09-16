# nf-core/sarek — xarici DNA inteqrasiya nümunəsi

[nf-core/sarek test data qeydi](https://github.com/nf-core/test-datasets/blob/24cdbea48c4415a29f668a724ce602fef8fed813/README.md)
və həmin revision-dakı `testdata/tiny/normal` beş paired lane istifadə edilir:
L001, L002, L004, L007, L008. Eyni normal sample-a aid olduqları
[tiny.tsv](https://github.com/nf-core/test-datasets/blob/24cdbea48c4415a29f668a724ce602fef8fed813/testdata/tsv/tiny.tsv)
ilə yoxlanıb. Kiçik GRCh37 reference həmin mənbədən gəlir.

```bash
python scripts/fetch_raw_examples.py --dataset variants
```

[Manifest](../raw-examples-manifest.json) URL, commit, ölçü və SHA-256-nı saxlayır.
Eyni mate-in lane-ləri gzip members kimi birləşdirilir.
FastQC → Cutadapt quality trimming → BWA-MEM → fixmate/sort/markdup →
BCFtools call/normalize/filter → MultiQC işləyir. Diploid model seçilir.

Bu nümunə **xarici software test dataset-i** kimi işarələnir. Açılmış mənbə
orijinal donor accession-u və müstəqil truth set vermədiyi üçün real insan
cohort-u, accuracy benchmark və ya patogenlik nəticəsi kimi təqdim edilmir.
Variant sayının sıfır olması özü xətaya bərabər deyil; pipeline mapped reads
olmasını ayrıca yoxlayır. Annotation matching GFF3 olmadan işə salınmır.

Caller-in ən azı bir məlum variantı düzgün tapması ayrıca
[sintetik positive control](../fixtures/raw-smoke/README.md) ilə yoxlanılır.
Bu nəzarət test dataset-inə gizli biological truth aid etmir.

