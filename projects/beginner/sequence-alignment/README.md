# Sequence Alignment Tool

## Problem və data
Sintetik qısa DNA sequence-ləri.

## Metod
Needleman–Wunsch və Smith–Waterman; match=2, mismatch=-1, linear gap=-2. Biopython score parity avtomatik yoxlanır.

## İcra
Repository kökündən, paket quraşdırıldıqdan sonra:
```bash

python scripts/run_projects.py --project alignment
```

## Çıxış
Yeni `results/runs/alignment/UTC-randomID/` qovluğu yaradılır; köhnə run əvəz olunmur. summary.json. `run.json` input checksum, paketlər, parametrlər və Git commit-i saxlayır.

## Qiymətləndirmə və interpretasiya
O(mn) yaddaş və vaxt; max 4 milyon hüceyrə. Ambiguous simvollar yalnız literal equality ilə score alır. Protein scoring, affine-gap və MSA production alətlərdə ayrıca.

Faktiki run nəticələri [results](../../../results/README.md) bölməsindədir. Testlər: `python -m pytest`. Nəticə yalnız dataset, parametr və model fərziyyələri ilə birlikdə etibarlıdır.

## Genişləndirmə
Layihə kataloqunda uyğun research extension seçin, hipotezi əvvəlcədən yazın və ayrı run açın. Parametri nəticəyə baxıb dəyişirsinizsə bunu exploratory kimi işarələyin.
