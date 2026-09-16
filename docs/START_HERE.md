# Buradan başlayın

## Məqsədinizə uyğun giriş

| İstək | İlk addım | Gözlənən nəticə |
|---|---|---|
| Bioinformatikanı sistemli öyrənmək | [Roadmap](../roadmap/README.md) → [mövzu xəritəsi](README.md) | Biologiyadan analizə mərhələli yol |
| Kodu tez yoxlamaq | [SETUP](../SETUP.md), sonra `python -m pytest` | Şəbəkəsiz əsas yoxlamalar |
| Beş layihəni işlətmək | `fetch_data.py --dataset all`, sonra `run_projects.py --project all` | Yeni tarixli run qovluqları |
| Xam FASTQ-dan nəticə almaq | [Xam workflow təlimatı](../workflows/README.md) | Linux alətləri, QC, mapping və analiz |
| Hazır nəticəni oxumaq | [Nəticələr](../results/README.md) və [STATUS](../STATUS.md) | İcra edilmiş iş və sübut səviyyəsi |
| Yeni tədqiqat seçmək | [30 layihə](../projects/IDEAS.md) və [suallar](../research/research-questions/README.md) | Hipotez, input, metod və qiymətləndirmə |

## Faylların məntiqi

- `src/biolab/`: təkrar istifadə edilən analiz funksiyaları.
- `scripts/`: endirmə, layihə icrası və hesabat yaratmaq üçün girişlər.
- `workflows/`: xarici bioinformatika proqramlarının ardıcıllığı.
- `datasets/`: data kartları, kiçik test nümunələri və sabit manifestlər.
- `results/example-runs/`: repoya daxil edilmiş kiçik nəticə snapshot-ları.
- `results/runs/`: sizin yeni icralarınız; Git-dən kənarda saxlanılır.
- `notebooks/`: hesablamanın izahı və nəticənin şərhi.
- `experiments/`: növbəti eksperiment protokolları.

## Nəticəni oxuyarkən

Əvvəl data kartını, sonra run parametrlərini, sonda nəticə şərhini oxuyun.
Sintetik test metodun texniki işləməsini yoxlayır. Real dataset analizi isə
yalnız seçilmiş nümunə, dizayn və fərziyyələr çərçivəsində elmi nəticə verir.
Hər yeni dataset üçün yeni accession/manifest və eksperiment qeydi yaradın.

