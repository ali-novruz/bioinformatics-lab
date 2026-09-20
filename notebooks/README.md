# Notebook laboratoriyası

Notebook-lar iki məqsədə görə ayrılır. `learn/` anlayışı addım-addım qurur; `reproduce/` isə saxlanmış analizi mümkün qədər az əlavə məntiqlə yenidən icra edir. Beləliklə pedaqoji izah ilə audit izi bir-birini sıxışdırmır.

## Öyrənmə seriyası

Hər notebook ən azı 24 hücrədən ibarətdir, kiçik ara nəticələri göstərir və hər bölməni özünü-yoxlama sualı ilə bitirir.

1. [DNA əsasları](learn/01-dna-basics.ipynb)
2. [Alignment matrisi və traceback](learn/02-alignment.ipynb)
3. [VCF-i sahə-sahə oxumaq](learn/03-vcf.ipynb)
4. [RNA-seq count matrisindən modelə](learn/04-rnaseq.ipynb)
5. [Maşın öyrənməsi və leakage](learn/05-machine-learning.ipynb)
6. [Hipotez, çoxlu test və güc](learn/06-statistics.ipynb)
7. [Filogeniya və ORF namizədləri](learn/07-phylogeny-orfs.ipynb)
8. [Nəticəni sınayan nəzarətlər](learn/08-research-controls.ipynb)

Bu fayllar `python scripts/build_learning_notebooks.py` ilə deterministik qurulur və icra olunur. Dərsdə kodu dəyişərək fərziyyələri sınamaq üçün şəxsi nüsxə yaradın.

## Reproduksiya seriyası

Bu səkkiz notebook əvvəlki audit notebook-larıdır: [DNA](reproduce/01-dna.ipynb), [alignment](reproduce/02-alignment.ipynb), [variantlar](reproduce/03-variants.ipynb), [RNA-seq](reproduce/04-rnaseq.ipynb), [ML](reproduce/05-ml.ipynb), [UNEC praktikası](reproduce/06-unec-practice.ipynb), [genişləndirilmiş layihələr](reproduce/07-expanded-projects.ipynb), [tədqiqat nəzarətləri](reproduce/08-research-controls.ipynb).

Reproduksiya notebook-u moduldakı hesablamanı çağırır, parametrləri və nəticəni şərh edir. Məqsəd alqoritmi hücrələrdə yenidən yazmaq deyil, eyni kod yolunun sübutunu saxlamaqdır.

## Yoxlama

```bash
python scripts/check_notebook_curriculum.py
python scripts/validate_notebooks.py
```

Birinci əmr struktur və saxlanmış execution state-i yoxlayır. İkinci əmr bütün notebook-ları təmiz kernel-də işlədib yeni nüsxələri `results/runs/notebook-validation/` altında saxlayır; yayımlanmış notebook-ları səssizcə əvəz etmir.
