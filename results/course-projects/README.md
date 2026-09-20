# UNEC praktik layihələrinin icra nəticələri

2026-09-16 tarixində üç yeni analiz yerli Python mühitində uğurla işlədildi. Bu qovluqlar faktiki run çıxışlarını saxlayır; yalnız mətn fayllarının sətir sonları Git üçün LF şəklinə salınıb, qiymətlər dəyişdirilməyib. Hər `run.json` giriş hash-ləri, paket versiyaları, parametrlər və icra anındakı kod hash-lərini saxlayır. İcra yeni fayllar commit edilməzdən əvvəl aparıldığı üçün `working_tree_dirty: true` açıq saxlanılıb.

| Layihə | Müşahidə | Fayl |
|---|---|---|
| Gen ifadəsi ML | 63 train / 20 test; 19/20 düzgün; balanced accuracy 0.9583 | [kanonik nəticə](../expanded-projects/gene-expression-ml/summary.json) |
| SQLite | 6 sample, 124 gene, 744 count; integrity ok | [kanonik nəticə](../expanded-projects/study-database/summary.json) |
| Biostatistika | 1000 sintetik null test; 47 nominal, 0 BH seçimi | [kanonik nəticə](../expanded-projects/biostatistics-lab/summary.json) |

Gen ifadəsi analizi real tarixi mikroarray data-sıdır. Biostatistikada null simulyasiyası sintetikdir; library xülasələri isə real yeast analizindəndir. SQL bazası eyni yeast sayımlarını təşkil edir. Mənbələr və məhdudiyyətlər [layihə dərslərində](../../docs/unec/README.md) izah edilir.

Faylların dəyişmədiyini və qeydə alınmış kod hash-lərini yoxlamaq:

```bash
python scripts/check_learning_assets.py
```

Bayt-bayt eyni 13 nəticə yalnız `results/expanded-projects/` altında saxlanılır; [references.json](references.json) köhnə dərs adlarını kanonik fayllara bağlayır. Kursa məxsus fərqli CV cədvəli, SQLite bazası və tarixi `run.json` qeydləri burada qalır. Bu yoxlama analizi yenidən işlətmir. Yeni icra üçün uyğun `run_expression_ml.py`, `run_study_database.py`, `run_biostatistics_lab.py` skriptlərini işlədin. [Snapshot manifesti](snapshot.json) unikal faylları bağlayır.
