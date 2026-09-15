# Genomic Variant Analysis

## Problem və data
GIAB HG001 GRCh38 v4.2.1-in ilk 1000 real VCF qeydi.

## Metod
PASS və QUAL>=20, multi-allelic ALT ayrılması, genotip allel sayı, SNV/indel/SV sinifləri və Ti/Tv.

## İcra
Repository kökündən, paket quraşdırıldıqdan sonra:
```bash
python scripts/fetch_data.py --dataset giab
python scripts/run_projects.py --project variants
```

## Çıxış
Yeni `results/runs/variants/UTC-randomID/` qovluğu yaradılır; köhnə run əvəz olunmur. variants.csv, summary.json, variant_types.png. `run.json` input checksum, paketlər, parametrlər və Git commit-i saxlayır.

## Qiymətləndirmə və interpretasiya
Bu seçmə genomun başlanğıc prefix-idir, representative random sample deyil. Truth-set-in özünü xülasə etmək caller accuracy benchmark-ı deyil. Frequency bir HG001 nümunəsinə aiddir, population frequency deyil.

Faktiki run nəticələri [results](../../../results/README.md) bölməsindədir. Testlər: `python -m pytest`. Nəticə yalnız dataset, parametr və model fərziyyələri ilə birlikdə etibarlıdır.

## Genişləndirmə
Layihə kataloqunda uyğun research extension seçin, hipotezi əvvəlcədən yazın və ayrı run açın. Parametri nəticəyə baxıb dəyişirsinizsə bunu exploratory kimi işarələyin.
