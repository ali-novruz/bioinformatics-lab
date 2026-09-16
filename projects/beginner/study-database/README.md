# Real RNA sayımlarından SQLite kataloqu

UNEC database dərslərindəki primary key, foreign key və bütövlük anlayışlarını real yeast nümunələrinə tətbiq edir.

```bash
python scripts/run_study_database.py
```

Şəbəkə tələb etmir. Girişlər repoda saxlanmış [counts](../../../results/raw-examples/rna-model/counts.tsv) və [metadata](../../../results/raw-examples/rna-model/metadata.csv) fayllarıdır. Onların xam məlumatdan yaranma yolu [buradadır](../../../results/raw-examples/README.md).

Sxem: `sample`, `gene`, `gene_count`, `source_file`. Nümunə-gen cütü unikaldır; sayım qeyri-mənfi tam ədəd olmalıdır; mövcud olmayan nümunə/gen kimliyi rədd edilir. SQLite foreign-key yoxlaması açıq aktivləşdirilir.

Nəticə: **6 nümunə, 124 gen, 744 ölçmə**, integrity check `ok`, foreign-key pozuntusu yoxdur. SQL ilə hesablanan library totals ilkin matrislə tutuşdurulur. Çıxışda database, sorğu, CSV xülasəsi və icra mənşəyi saxlanılır.

[Hazır database](../../../results/course-projects/study-database/laboratory.sqlite), [SQL sorğusu](../../../results/course-projects/study-database/queries.sql), [nəticə](../../../results/course-projects/study-database/summary.json).

Bu, kiçik tədris kataloqudur; klinik məlumat idarəetmə sistemi deyil. İstifadəçi girişi, çoxistifadəçili icazələr və audit serveri bu layihənin əhatəsində deyil.
