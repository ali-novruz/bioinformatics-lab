# Repository vəziyyəti — 2026-09-20

## Hazır və yoxlanmış

| Sahə | Cari vəziyyət |
|---|---|
| İşlək layihələr | 13 layihə; 9-u tam offline, 4-ü ilk icrada açıq data endirir |
| Notebook-lar | 8 mərhələli öyrənmə + 8 reproduksiya notebook-u; schema və icra yoxlanır |
| Tədris kitabxanası | 16 biologiya anlayışı, 20 format bələdçisi, 320 terminlik AZ–EN lüğət |
| Elmi mənbələr | 38 database kartı, 37 primary-paper note, 9 məqsədli mini-review |
| Statistika | Survival, Bayes, mixed models, power/sample size və kompozisional data bələdçiləri |
| UNEC praktikumu | 8 dərs, 15 həftəlik plan, 24 ayrıca tapşırıq, ayrıca həll açarı, 4 kitab PDF-i və praktikum PDF-i |
| Keyfiyyət | Ruff, mypy, 75% coverage həddi, Linux/Windows CI, `uv.lock` ilə ayrıca locked job |
| Nəticə bütövlüyü | Versioned run manifest, input/source/output SHA-256, tarixi source archive və snapshot yoxlaması |
| Lisenziya | Kod MIT; orijinal sənəd/sintetik data CC BY 4.0; üçüncü tərəf istisnaları ayrıca xəritələnib |

## Faktiki icralar

- **Sequence və genomika:** PhiX DNA/ORF, Needleman–Wunsch və Smith–Waterman, GIAB VCF prefix-i, Opuntia fraqment filogeniyası.
- **Transcriptomics:** real pasilla count modeli, GSE110004 kiçik raw RNA pipeline-ı, GO-slim enrichment və SQLite sayım kataloqu.
- **Machine learning:** WDBC holdout, Khan nested CV və 99 permutation control.
- **Protein:** UniProt P01308 sequence xülasəsi və ayrıca PDB 1CRN kontakt xəritəsi.
- **Regional genetika:** iki açıq ClinVar qeydinin mənbə-hash-li, qeyri-klinik evidence prioritetləndirməsi.
- **Xam workflow:** Linux positive control-da bir məlum PASS SNV və 422/422 gene-assigned fragment; xarici kiçik DNA fixture-də 32 variant, 27 PASS.

[Nəticə kataloqu](results/README.md), [tənqidi finding-lər](research/findings/README.md) və [audit](docs/RESEARCH_AUDIT.md) iddianı mənbə və məhdudiyyətlə bağlayır.

## Elmi sərhədlər

- GIAB prefix və kiçik raw fixture genome-wide caller benchmark deyil.
- Altı nümunəlik, subsample RNA icrası tam məqalə reproduksiyası deyil.
- GO nəticəsi mənfidir: bir genlik foreground-da FDR discovery əldə edilməyib.
- Qısa Opuntia fraqment ağacı tam növ filogeniyası sayılmır.
- Daxili ML score-u xarici cohort və klinik validasiyanı əvəz etmir.
- ClinVar tədris triage-si diaqnoz, fərdi risk və ya müalicə məsləhəti vermir.

## Davam edən uzunmüddətli iş

30 əsas layihə ideyası və [14 sahəlik genişlənmə xəritəsi](roadmap/domain-gaps.md) protokol səviyyəsindədir. External cohort validation, full-scale genom/RNA pipeline, variant annotator benchmark, assembly/long-read, epigenomika, GWAS, docking/MD və immunoinformatika layihələri hələ icra edilmiş nəticə kimi təqdim edilmir.

Bu repository işlək tədris və tədqiqat bazasıdır. Yeni nəticə yalnız dataset kartı, əvvəlcədən yazılmış metod, test, run manifest, nəzarət və məhdudiyyətli finding ilə hazır sayılır.
