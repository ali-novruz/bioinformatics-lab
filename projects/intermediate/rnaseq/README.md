# RNA-Seq Gene Expression Analysis

## Problem və data
Bioconductor pasilla real Drosophila count matrix və sample metadata.

## Metod
Raw counts → total>=10 prefilter → type+condition NB model → treated/untreated Wald test → FDR; normalization → PCA/heatmap/volcano.

## İcra
Repository kökündən, paket quraşdırıldıqdan sonra:
```bash
python scripts/fetch_data.py --dataset pasilla
python scripts/run_projects.py --project rnaseq
```

## Çıxış
Yeni `results/runs/rnaseq/UTC-randomID/` qovluğu yaradılır; köhnə run əvəz olunmur. differential_expression.csv, normalized_counts.csv, metadata.csv, summary.json, pca.png, heatmap.png, volcano.png. `run.json` input checksum, paketlər, parametrlər və Git commit-i saxlayır.

## Qiymətləndirmə və interpretasiya
7 kitabxana və sample annotation məhdudiyyəti; biological replicate/protocol quruluşunu ilkin məqalə ilə yoxlamaq lazımdır. Gene-level DE splicing nəticəsinin reproduksiyası deyil. LFC shrinkage bu icrada tətbiq edilmir.

Faktiki run nəticələri [results](../../../results/README.md) bölməsindədir. Testlər: `python -m pytest`. Nəticə yalnız dataset, parametr və model fərziyyələri ilə birlikdə etibarlıdır.

## Genişləndirmə
Layihə kataloqunda uyğun research extension seçin, hipotezi əvvəlcədən yazın və ayrı run açın. Parametri nəticəyə baxıb dəyişirsinizsə bunu exploratory kimi işarələyin.
