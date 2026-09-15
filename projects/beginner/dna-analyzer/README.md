# DNA Sequence Analyzer

## Problem və data
Real PhiX genomu; şəbəkəsiz synthetic FASTA fallback.

## Metod
GC-də yalnız A/C/G/T məxrəci, IUPAC reverse complement, transcription və frame-0 codon counts. Bütün genomun frame-0 kodonları annotasiya olunmuş CDS demək deyil.

## İcra
Repository kökündən, paket quraşdırıldıqdan sonra:
```bash
python scripts/fetch_data.py --dataset phix
python scripts/run_projects.py --project dna
```

## Çıxış
Yeni `results/runs/dna/UTC-randomID/` qovluğu yaradılır; köhnə run əvəz olunmur. summary.json, gc.png. `run.json` input checksum, paketlər, parametrlər və Git commit-i saxlayır.

## Qiymətləndirmə və interpretasiya
GC biological species comparison və ya function sübutu deyil. PhiX overlapping genes və circular genome konteksti nəzərə alınmalıdır.

Faktiki run nəticələri [results](../../../results/README.md) bölməsindədir. Testlər: `python -m pytest`. Nəticə yalnız dataset, parametr və model fərziyyələri ilə birlikdə etibarlıdır.

## Genişləndirmə
Layihə kataloqunda uyğun research extension seçin, hipotezi əvvəlcədən yazın və ayrı run açın. Parametri nəticəyə baxıb dəyişirsinizsə bunu exploratory kimi işarələyin.
