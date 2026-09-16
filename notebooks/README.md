# Notebook laboratoriyası

Hər notebook **Problem → Theory → Data → Method → Code → Result → Interpretation → Conclusion** ardıcıllığını saxlayır.

- [DNA sequence analizi](exploratory-analysis/01-dna.ipynb)
- [Sequence alignment](experiments/02-alignment.ipynb)
- [Genomik variant analizi](experiments/03-variants.ipynb)
- [RNA-seq differential expression](experiments/04-rnaseq.ipynb)
- [Disease classification](experiments/05-ml.ipynb)

Paket və real dataset-ləri əvvəlcədən quraşdırın. Notebook yeni run qovluğu yaradır. Çıxışlar təkrar icrada dəyişərsə versiya, checksum, parametr və random seed-i müqayisə edin.

## UNEC nəticələrinin yoxlanması

[06-unec-practice.ipynb](experiments/06-unec-practice.ipynb): saxlanmış proqnozlardan metriklər, real SQLite sorğusu və null simulyasiyasının təkrar icrası. Başdan sona işlədilib.

## Yeni analizlər

[07-expanded-projects.ipynb](experiments/07-expanded-projects.ipynb): real GO enrichment, filogenetik distance və ORF koordinatlarının yoxlanması.

## Tənqidi control nəticələri

[08-research-controls.ipynb](experiments/08-research-controls.ipynb): GO singleton p-lərini xüsusi formuldan, nested-CV score və permutation p-ni saxlanmış cədvəldən yenidən hesablayır. 99-permutation model fit-i ayrıca `scripts/run_controls.py` ilə icra olunur.

Bütün notebook-ları təkrar yoxlamaq: `python scripts/validate_notebooks.py`.
Yeni icra nüsxələri `results/runs/notebook-validation/` daxilində saxlanır;
əvvəlki notebook output-ları dəyişdirilmir. İlk beş notebook modeli/analizi
işlədir, 06–08 isə yuxarıda göstərilən həcmdə saxlanmış nəticələri yenidən yoxlayır.
