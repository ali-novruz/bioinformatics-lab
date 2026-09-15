# Wisconsin Diagnostic Breast Cancer

**Source / version:** UCI DOI 10.24432/C5DW2B; scikit-learn built-in copy

**Dataset description:** Fine needle aspirate image-dən ölçülmüş nüvə xüsusiyyətləri; gene-expression məlumatı deyil.

**Files:** Paketdən memory-yə yüklənir; raw CSV repo-da saxlanmır

**Columns/features və biological meaning:** 569 sample × 30 continuous nuclear morphology features; labels benign/malignant. ID-lər repo split-də row index-dir.

**License / access:** UCI səhifəsi CC BY 4.0 göstərir; dataset attribution saxlanır.

**Size / checksum (faktiki endirilən məzmun):** WDBC dense numeric matrix: 569×30×8 ≈ 136,560 bytes before labels/metadata; source file/package footprint fərqlidir.

## Download instructions
```bash
python scripts/run_projects.py --project ml
```
Raw fayllar `datasets/raw/` daxilində saxlanır və Git-ə daxil edilmir. [Reference manifest](../reference-manifest.json) ilk doğrulanmış snapshot-u göstərir; local manifest hər run-da yoxlanır.

## Məhdudiyyətlər
Retrospective, bir dataset; external patient/cohort validation yoxdur. Positive class malignant kimi yenidən kodlaşdırılıb.

Rəsmi mənbə: [Wisconsin Diagnostic Breast Cancer](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic).
