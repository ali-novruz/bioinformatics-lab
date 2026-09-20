# Sahə boşluqları üçün icra xəritəsi

Bu siyahı hazır nəticə deyil. Hər maddə repository-də çatışmayan sahəni işlək layihəyə çevirmək üçün minimum data, metod, qiymətləndirmə və iddia sərhədini verir.

| Sahə | İlk işlək layihə | Data və metod | Qəbul meyarı | İddia sərhədi |
|---|---|---|---|---|
| Epigenomika | ATAC-seq peak QC və differential accessibility | ENCODE kiçik cohort; alignment və peak matrix | FRiP/TSS enrichment, replicate concordance, FDR | Accessibility birbaşa expression səbəbi deyil |
| Populyasiya genetikası/GWAS | PCA, relatedness və association nəzarəti | 1000 Genomes subset; PLINK | genomic inflation, QQ/Manhattan, ancestry sensitivity | Association səbəb əlaqəsi deyil |
| Survival | Endpoint və Cox baseline | TCGA-CDR seçilmiş cohort | PH yoxlaması, HR intervalı, calibration | Retrospektiv cohort klinik qərar qaydası deyil |
| Genome assembly | Short/long-read müqayisəsi | public microbial reads; SPAdes/Flye | QUAST, completeness, contamination | N50 təkbaşına düzgünlük deyil |
| Long-read | SV calling və platform sensitivity | GIAB ONT/PacBio subset | truth-set precision/recall, stratified regions | Bir donor populyasiya tezliyi vermir |
| HMM və MSA | Protein ailəsi profilinin holdout qiymətləndirilməsi | Pfam seed/holdout; HMMER, Clustal Omega | family holdout PR-AUC, shuffled negative | Profile hit funksiya təsdiqi deyil |
| Variant annotation | Eyni VCF üçün annotator müqayisəsi | GIAB + VEP/SnpEff | transcript/version concordance, consequence diff | Annotation klinik hökm deyil |
| Dərin öyrənmə | Sequence classifier baseline və ablation | açıq benchmark; CNN/transformer | family split, calibration, simple baseline | Yüksək score mexanizm deyil |
| Docking/MD | Kiçik ligand pose təkrar istehsalı | PDB redocking set; AutoDock/MD | RMSD, decoy ranking, seed sensitivity | Docking score binding affinity deyil |
| Batch effect | Correction öncə/sonra siqnal qorunması | çox-batch expression data | batch prediction azalması və biology retention | Vizual mixing tam correction sübutu deyil |
| API mühəndisliyi | NCBI/Ensembl cache və rate-limit client | rəsmi API-lər | retry, schema test, immutable response hash | API cavabı dəyişməz dataset deyil |
| Workflow dilləri | Eyni mini pipeline-ı Nextflow/Snakemake-də işlətmək | smoke fixtures | təmiz container run, resume, provenance parity | Smoke production scalability sübutu deyil |
| İmmunoinformatika | HLA binding baseline | IEDB public benchmark | allele-aware split, calibration, external set | Predicted binding immunogenicity deyil |
| Spatial/single-cell | Donor-aware cell-type DE | public multi-donor atlas | donor pseudobulk, batch sensitivity, marker holdout | Hüceyrə sayı donor replikatı deyil |

## Tamamlama qaydası

Hər layihə üçün dataset kartı, əvvəlcədən yazılmış protokol, versiyalı run manifest, ən azı bir mənfi nəzarət, nəticə cədvəli, qrafik və məhdudiyyətli finding tələb olunur. Yeni layihə yalnız `biolab list` kataloquna daxil olduqda, testləri keçdikdə və təmiz mühitdə təkrar işləndikdə “işlək” sayılır.

[30 əsas layihə ideyası](../projects/IDEAS.md) bu xəritədən prioritet seçmək üçün əsas kataloqdur.
