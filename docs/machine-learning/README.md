# Machine learning for bioinformatics

### Problemi düzgün qurmaq
Classification diskret label, regression davamlı outcome, clustering labelsiz struktur üçündür. Disease label, sample unit, prediction vaxtı və məlumatın həmin vaxt mövcudluğu yazılmalıdır. Donor, ailə, batch, hospital və homolog sequence-lər split sərhədlərini müəyyən edir.

### Classical baseline-lar
Logistic Regression interpretasiya olunan linear baseline; SVM margin əsaslı; Random Forest nonlinear ağac ansamblı; XGBoost gradient boosting-dir. Scaling Logistic/SVM üçün pipeline daxilində edilir. Hyperparameter seçimi training CV ilə, son qiymətləndirmə toxunulmamış test cohort-da aparılır. Imbalanced data üçün AUROC yanında PR-AUC, sensitivity/specificity və calibration verin.

### Feature engineering
DNA üçün k-mer tezlikləri, protein üçün kompozisiya/domain, expression üçün assay-aware transformation. Feature selection-i split-dən əvvəl etmək sızmadır. Batch correction və gene selection fold daxilində öyrənilməlidir. Gene-expression n≪p olduqda regularization və nested CV vacibdir.

### PCA, t-SNE, UMAP
PCA linear variance, t-SNE və UMAP lokal neighbourhood strukturlarına fokuslanır. İkiölçülü qrafikdə adalar real siniflərin sübutu deyil. Random seed, perplexity/neighbours və preprocessing dəyişdirilərək sabitlik yoxlanmalıdır. Visualization-a baxıb label/split seçmək olmaz.

### Deep learning
NN nonlinear əlaqələr, CNN local motifs, RNN sequential dependencies, Transformers attention və pretrained representations üçün istifadə olunur. Biological foundation models böyük pretraining data-dan representation çıxarır; homology, temporal contamination və training data overlap yoxlanmalıdır. Embedding-lər biological truth deyil.

### Layihə istiqamətləri
Expression→disease; cancer subtype; DNA regulatory sequence; protein function; mutation pathogenicity; drug response. Hər birində cohort/sequence/drug split uyğun seçilir. Eyni xəstənin iki ölçməsini train/test-ə bölmək olmaz. Drug response-də unseen drug və unseen cell line iki ayrı generalization sualıdır.

### Araşdırma
Problem: internal accuracy external validity-ni şişirdir. Data: WDBC baseline; sonra GEO cross-cohort expression. Eksperiment: within-cohort və leave-study-out fərqi. Yeni sual: performance azalmasının nə qədəri platforma, nə qədəri case-mix ilə bağlıdır?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://scikit-learn.org/stable/common_pitfalls.html). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
