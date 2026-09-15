# Machine Learning Disease Classification

## Problem və data
UCI Wisconsin Diagnostic Breast Cancer; sklearn vasitəsilə 569 real nümunə, 30 morphology feature.

## Metod
25% stratified untouched test; qalan 75%-də 5-fold CV. Dummy, Logistic Regression və Random Forest; training CV AUROC ilə seçim; sonra yalnız seçilən modelə test.

## İcra
Repository kökündən, paket quraşdırıldıqdan sonra:
```bash

python scripts/run_projects.py --project ml
```

## Çıxış
Yeni `results/runs/ml/UTC-randomID/` qovluğu yaradılır; köhnə run əvəz olunmur. cv.csv, predictions.csv, split.csv, summary.json, roc.png, confusion.png. `run.json` input checksum, paketlər, parametrlər və Git commit-i saxlayır.

## Qiymətləndirmə və interpretasiya
Features gene expression deyil, hüceyrə nüvəsinin morfologiyasıdır. Bu retrospective dataset real prospective diaqnostika validasiyası deyil. Donor/cohort external split üçün metadata yoxdur.

Faktiki run nəticələri [results](../../../results/README.md) bölməsindədir. Testlər: `python -m pytest`. Nəticə yalnız dataset, parametr və model fərziyyələri ilə birlikdə etibarlıdır.

## Genişləndirmə
Layihə kataloqunda uyğun research extension seçin, hipotezi əvvəlcədən yazın və ayrı run açın. Parametri nəticəyə baxıb dəyişirsinizsə bunu exploratory kimi işarələyin.
