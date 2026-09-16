# İlkin tədqiqat nəticələri

Yeni: [Linux-da xam FASTQ-dan real RNA və xarici DNA nəticələri](raw-examples/README.md).
Altı RNA sample-ında 300,000 read pair işləndi; 84 gen modelə daxil oldu.
[Sintetik positive control](linux-smoke/README.md) ayrıca pipeline doğrulamasıdır.

Bu hesabat faktiki local run-lardan avtomatik çıxarılan metriklərə əsaslanır. Məqalələrin orijinal benchmark-larının reproduksiyası deyil.

| Analiz | Faktiki nəticə | Nə deməkdir? |
|---|---|---|
| Variant VCF | 1000 record, 1003 ALT; 867 SNV, 136 indel | Bir record birdən çox ALT daşıya bilər |
| Ti/Tv | 2.8194 | Yalnız bu genomik prefix üçün descriptive nisbət |
| Pasilla | 7 sample, 14599 input gene; 9921 prefilter sonrası | ~type+condition modeli |
| RNA FDR<0.05 | 1113 gene | Model altında adjusted-p discovery; hər gen ayrıca biological validation tələb edir |
| FDR<0.05 və abs(log2FC)>1 | 232 gene | Effect-size həddi ilə vurğulanan subset; əlavə formal FDR zəmanəti deyil |
| WDBC test | 143 sample; logistic | Seçim training-only CV ilə |
| WDBC AUROC | 0.996226 | Fixed internal heldout split |
| WDBC PR-AUC | 0.994299 | Positive=malignant |
| WDBC sensitivity / specificity | 0.9245 / 0.9889 | Threshold 0.5; clinical threshold optimizasiyası deyil |
| WDBC bootstrap AUROC 95% | [0.9887, 1.0000] | Fitted modelə şərtli, 1000 resample; training variasiyası daxil deyil |
| Protein | P01308: 110 aa; 1CRN: 46 Cα residue | Ayrı proteinlər, ayrı tədris nümunələri |

## Bioloji interpretasiya

**RNA-seq:** müsbət log2FC treated qrupunda daha yüksək expression deməkdir. Sequencing type covariate qrup fərqini texniki təsirdən qismən ayırır, bütün confounder-ləri aradan qaldırmır. 1539 gene üçün padj yoxdur; bunlar “p=1” və ya “p=0” kimi doldurulmayıb. Independent filtering/outlier handling və aşağı information səbəbləri ayrıca audit edilə bilər. Bu count analysis pasilla haqqında splicing məqaləsini bütövlükdə reproduce etmir.

**Variantlar:** GIAB benchmark prefix-ində SNV/indel payı və Ti/Tv hesablana bilir. Genome-wide variant burden, ancestry və patogenlik nəticəsi çıxarıla bilməz. Truth-set-in özü ilə onun keyfiyyət statistikasını hesablamaq variant caller precision/recall-u ölçmür. Biological consequence annotation bu icrada aparılmayıb.

**ML:** morphology features internal test-də malignant/benign etiketini yaxşı ayırır. Test confusion matrix (true rows benign/malignant; predicted columns benign/malignant): `[[89, 1], [4, 49]]`. Gene-expression classifier deyil. External cohort və prospective test olmadığından klinik istifadəyə yararlılıq iddia edilmir. Bootstrap interval yeni xəstəxana/platforma uncertainty-sini ölçmür.

**Protein:** Cα məsafə xəritəsi sequence üzrə uzaq residue-lərin spatial yaxınlığını göstərir; contact cutoff kimyəvi binding və ya activity ölçüsü deyil. P01308 insulin və 1CRN crambin bir-birinə hizalanmış cüt kimi təqdim edilmir.

## Statistik mənalılıq

RNA nəticəsi seçilmiş negative-binomial model və FDR assumptions-a şərtlidir. Effekt, sample size və outlier məlumatı ilə birlikdə baxılmalıdır. VCF/protein xülasələri hypothesis test deyil. WDBC-də ayrıca model-comparison significance testi aparılmayıb; fold standard deviation model üstünlüyünün p-value-su deyil.

## Əvvəlki tədqiqatlarla əlaqə

[DESeq2 qeydi](../research/papers/deseq2.md) count overdispersion və dispersion shrinkage motivasiyasını izah edir. Repo həmin metod ailəsinin Python tətbiqidir; original paper rəqəmləri ilə eynilik iddiası yoxdur. [Salmon qeydi](../research/papers/salmon.md) upstream quantification bias-ının downstream nəticələrə təsirini göstərir; burada quantifier müqayisəsi aparılmayıb.

## Yeni suallar

1. Pasilla-da `~condition` və `~type+condition` modelləri arasında effekt/rank fərqi nədir?
2. FDR discovery-lərindən hansı exon-level/splicing və pathway evidence ilə dəstəklənir?
3. GIAB difficult/indel regionlarında caller-in real precision/recall-u necədir?
4. WDBC classifier başqa cohort və measurement pipeline-da kalibrasiyasını saxlayırmı?

## Fayllar və təkrar icra

[Example run snapshots](example-runs) metadata, metrik və kiçik cədvəlləri saxlayır. Full derived tables `results/runs/` altında yaradılır, Git-ə daxil edilmir. [Qrafik qalereyası](../visualizations/README.md) data tipini göstərir. `run.json` commit-i və working-tree dirty statusunu olduğu kimi saxlayır; yaradılma zamanı bütün sonrakı sənədlər hələ commit edilməmiş ola bilər.
