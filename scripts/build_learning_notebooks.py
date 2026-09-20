"""Build and execute the eight step-by-step teaching notebooks."""

from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks/learn"

LESSONS = {
    "01-dna-basics": (
        "DNA ardıcıllığını addım-addım oxumaq",
        [
            (
                "Simvollar və təmizləmə",
                "from biolab.sequence import clean_dna\nraw=' acgt nry '\nclean_dna(raw)",
                "Boşluq və kiçik hərflər nəticəyə niyə təsir etməməlidir?",
            ),
            (
                "Baza sayları",
                "from collections import Counter\nseq=clean_dna(raw)\nCounter(seq)",
                "N və R kimi qeyri-müəyyən simvolları ayrıca niyə sayırıq?",
            ),
            (
                "GC payı",
                "from biolab.sequence import gc_content\ngc_content('AAGCGTNN')",
                "Məxrəcə N daxil edilsə qiymət hansı istiqamətdə qərəzli olar?",
            ),
            (
                "Tərs komplement",
                "from biolab.sequence import reverse_complement\nreverse_complement('ATGCCN')",
                "Sequencer digər strand-i oxusa bu əməliyyat nəyi bərpa edir?",
            ),
            (
                "Kodlar və çərçivə",
                "seq='ATGAAATAGCC'\n[seq[i:i+3] for i in range(0,len(seq)-2,3)]",
                "Bir baza əlavə olunanda bütün sonrakı kodonlar niyə dəyişir?",
            ),
            (
                "Motifin üst-üstə düşməsi",
                "from biolab.sequence import motif_positions\nmotif_positions('AAAAA','AAA')",
                "Adi string count burada niyə səhv cavab verə bilər?",
            ),
            (
                "Yekun audit",
                "from biolab.sequence import sequence_summary\nsequence_summary('ATGAAATAGNN')",
                "Hansı sahələr müşahidədir, hansılar bioloji şərh tələb edir?",
            ),
        ],
    ),
    "02-alignment": (
        "Alignment matrisi və traceback",
        [
            (
                "Skor modelini yazmaq",
                "match,mismatch,gap=2,-1,-2\n{'match':match,'mismatch':mismatch,'gap':gap}",
                "Gap opening və extension ayrı olsa hansı model dəyişir?",
            ),
            (
                "Birinci sətir və sütun",
                "import numpy as np\nm=np.zeros((5,4));m[:,0]=np.arange(5)*gap;m[0,:]=np.arange(4)*gap\nm",
                "Lokal alignment-də bu sərhədlər niyə sıfır qalır?",
            ),
            (
                "Bir hüceyrənin recurrence-i",
                "diag,up,left=3+match,1+gap,2+gap\nmax(diag,up,left)",
                "Bərabərlik olduqda tie-break nəticə ardıcıllığını necə dəyişə bilər?",
            ),
            (
                "Qlobal uyğunlaşdırma",
                "from biolab.sequence import align\na=align('ACGT','AGT','global');a.to_dict()",
                "Skor və identity eyni keyfiyyət ölçüsüdürmü?",
            ),
            (
                "Lokal uyğunlaşdırma",
                "align('TTACGTAA','ACG','local').to_dict()",
                "Başlanğıc və son koordinatların half-open olması nə verir?",
            ),
            (
                "Backend uyğunluğu",
                "p=align('ACGTAC','ACTAC',backend='python');n=align('ACGTAC','ACTAC',backend='numpy');p==n",
                "Sürətli yolun eyni tie siyasətini saxlaması niyə vacibdir?",
            ),
            (
                "Limit və istehsal alətləri",
                "cells=(1500+1)*(1500+1)\n{'cells':cells,'within_teaching_limit':cells<=4_000_000}",
                "Uzun genom üçün niyə BWA/minimap2 kimi indeksli alət seçilir?",
            ),
        ],
    ),
    "03-vcf": (
        "VCF-i sahə-sahə şərh etmək",
        [
            (
                "VCF sətrinin anatomiyası",
                "line='chr1\\t10\\t.\\tA\\tG\\t60\\tPASS\\tDP=20\\tGT:AD\\t0/1:10,10'\nline.split('\\t')",
                "INFO və FORMAT hansı səviyyələrdə məlumat saxlayır?",
            ),
            (
                "Parser ilə oxumaq",
                "from pathlib import Path\nfrom biolab.io import read_vcf\np=Path('datasets/fixtures/toy.vcf')\nrecords=list(read_vcf(p));len(records),records[0]",
                "Parser hansı yanlış başlıqları rədd etməlidir?",
            ),
            (
                "Variant tipi",
                "from biolab.genomics import variant_type\n[(r,a,variant_type(r,a)) for r,a in [('A','G'),('A','AT'),('AC','GT')]]",
                "Eyni uzunluqlu iki bazalı dəyişiklik niyə SNV deyil?",
            ),
            (
                "Genotipdən allel sayı",
                "from biolab.genomics import allele_counts\nallele_counts({'s1':{'GT':'0/1'},'s2':{'GT':'1/1'}},1)",
                "Missing allel tezliyi hansı məxrəclə hesablanmalıdır?",
            ),
            (
                "Keyfiyyət filtrinin təsiri",
                "from biolab.genomics import analyze_vcf\ntable,summary=analyze_vcf(p,min_qual=20);summary",
                "QUAL həddi klinik patogenlik deməkdirmi?",
            ),
            (
                "Çox-allelli qeyd",
                "allele_counts({'s1':{'GT':'1/2'},'s2':{'GT':'0/2'}},2)",
                "Normalization zamanı çox-allelli qeyd niyə ayrıla bilər?",
            ),
            (
                "Sərhəd cümləsi",
                "claim='Bu analiz təsviri filtrdir; klinik təsnifat deyil.'\nclaim",
                "Patogenlik üçün hansı əlavə sübut növləri lazımdır?",
            ),
        ],
    ),
    "04-rnaseq": (
        "RNA-seq count matrisindən modelə",
        [
            (
                "Count və TPM fərqi",
                "import pandas as pd\ncounts=pd.DataFrame({'s1':[100,20,0],'s2':[200,18,1]},index=['g1','g2','g3']);counts",
                "DESeq2 niyə raw integer count istəyir?",
            ),
            (
                "Kitabxana ölçüsü",
                "counts.sum(axis=0)",
                "Sadəcə cəmlə bölmək compositional təsiri tam həll edirmi?",
            ),
            (
                "Sadə CPM yalnız vizualizasiya üçün",
                "cpm=counts.div(counts.sum())*1_000_000;cpm.round(1)",
                "CPM-i diferensial modelə vermək niyə problem ola bilər?",
            ),
            (
                "Metadata və dizayn",
                "meta=pd.DataFrame({'type':['single','paired'],'condition':['untreated','treated']},index=['s1','s2']);meta",
                "Type covariate condition ilə tam qarışsa nə baş verər?",
            ),
            (
                "Prefilter",
                "keep=counts.sum(axis=1)>=10\ncounts.loc[keep]",
                "Aşağı count genləri əvvəlcədən filtrləmək test sayını necə dəyişir?",
            ),
            (
                "Log transform və məsafə",
                "import numpy as np\nnp.log1p(counts).T.corr().round(2)",
                "PCA qrupları göstərsə də diferensial ifadəni sübut edirmi?",
            ),
            (
                "FDR şərhi",
                "from biolab.statistics import benjamini_hochberg\np=[.001,.02,.2,.8];benjamini_hochberg(p)",
                "Raw p<.05 və FDR<.05 niyə eyni siyahı deyil?",
            ),
        ],
    ),
    "05-machine-learning": (
        "Bioloji maşın öyrənməsində leakage-dən qaçmaq",
        [
            (
                "Feature və target",
                "from sklearn.datasets import load_breast_cancer\nd=load_breast_cancer(as_frame=True);d.data.shape,d.target.value_counts().to_dict()",
                "Bu dataset gen ifadəsi deyil; feature-lər nəyi ölçür?",
            ),
            (
                "Stratified split",
                "from sklearn.model_selection import train_test_split\ntr,te=train_test_split(range(len(d.target)),test_size=.25,stratify=d.target,random_state=42);len(tr),len(te)",
                "Stratification kiçik sinfi necə qoruyur?",
            ),
            (
                "Pipeline sərhədi",
                "from sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\npipe=make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000));pipe",
                "Scaler bütün data-da fit olsa leakage harada yaranır?",
            ),
            (
                "Training-only fit",
                "pipe.fit(d.data.iloc[tr],d.target.iloc[tr]);prob=pipe.predict_proba(d.data.iloc[te])[:,1];prob[:5]",
                "Test cohort model seçmək üçün istifadə edilə bilərmi?",
            ),
            (
                "AUROC və threshold",
                "from sklearn.metrics import roc_auc_score,balanced_accuracy_score\nroc_auc_score(d.target.iloc[te],prob),balanced_accuracy_score(d.target.iloc[te],prob>=.5)",
                "AUROC yüksək olsa .5 threshold mütləq optimaldırmı?",
            ),
            (
                "Bootstrap interval",
                "from biolab.statistics import bootstrap_auc\nbootstrap_auc(d.target.iloc[te],prob,repeats=100,seed=7)",
                "Bu interval yeni model fit-lərini deyil, nəyi dəyişir?",
            ),
            (
                "Mənfi nəzarət",
                "import numpy as np\nrng=np.random.default_rng(7);shuffled=rng.permutation(d.target.iloc[tr]);(shuffled==d.target.iloc[tr]).mean()",
                "Etiket qarışdırıldıqdan sonra selection də yenidən icra olunmalıdırmı?",
            ),
        ],
    ),
    "06-statistics": (
        "Hipotez, çoxlu test və güc",
        [
            (
                "Null model",
                "import numpy as np\nrng=np.random.default_rng(12);a=rng.normal(0,1,30);b=rng.normal(0,1,30);a.mean(),b.mean()",
                "Null altında fərqli sample mean görmək niyə normaldır?",
            ),
            (
                "T-test",
                "from scipy.stats import ttest_ind\nttest_ind(a,b,equal_var=False)",
                "p-value effect size deyil: hansı əlavə ölçünü verməliyik?",
            ),
            (
                "Effect size",
                "effect=(a.mean()-b.mean())/np.sqrt((a.var(ddof=1)+b.var(ddof=1))/2);effect",
                "Kiçik effect böyük sample-də əhəmiyyətli ola bilərmi?",
            ),
            (
                "Min p problemi",
                "p=rng.uniform(size=1000);p.min(),(p<.05).sum()",
                "1000 null testdə təxminən neçə nominal discovery gözlənir?",
            ),
            (
                "BH düzəlişi",
                "from biolab.statistics import benjamini_hochberg\nq=benjamini_hochberg(p);(q<.05).sum(),q.min()",
                "BH family-ni əvvəlcədən necə müəyyən etməliyik?",
            ),
            (
                "Güc düşüncəsi",
                "from scipy.stats import norm\n[(n,2*(1-norm.cdf(.5*np.sqrt(n/2)))) for n in [10,30,100]]",
                "Bu sadə yaxınlaşmada effect və variance harada gizlənir?",
            ),
            (
                "Hesabat",
                "{'n_a':len(a),'n_b':len(b),'effect_size':round(float(effect),3),'assumption':'independent synthetic normal samples'}",
                "Assumption pozularsa hansı robust və ya permutation yanaşması seçilər?",
            ),
        ],
    ),
    "07-phylogeny-orfs": (
        "Ardıcıllıqdan ağac və ORF namizədinə",
        [
            (
                "Alignment sütunu",
                "seqs=['ACGT','ACGA','ATGA','ATGT'];list(zip(*seqs,strict=True))",
                "Gap və N olan sütun complete-case məsafədə necə davranmalıdır?",
            ),
            (
                "p-distance",
                "import numpy as np\nm=np.array([list(s) for s in seqs]);(m[:,None,:]!=m[None,:,:]).mean(axis=2)",
                "Multiple substitutions p-distance-i hansı istiqamətdə qərəzləndirir?",
            ),
            (
                "NJ ağacı",
                "from biolab.phylogeny import nj_tree\ntree,dist=nj_tree(['a','b','c','d'],m);tree.count_terminals()",
                "NJ ağacı avtomatik köklənmiş təkamül istiqaməti verirmi?",
            ),
            (
                "Bootstrap sütunları",
                "rng=np.random.default_rng(4);idx=rng.integers(0,m.shape[1],m.shape[1]);m[:,idx]",
                "Bootstrap support branch-in doğru olma ehtimalıdırmı?",
            ),
            (
                "ORF başlanğıcı",
                "dna='CCCATGAAATAACCC';[(i,dna[i:i+3]) for i in range(len(dna)-2) if dna[i:i+3]=='ATG']",
                "Start codon görmək təkbaşına geni təsdiqləyirmi?",
            ),
            (
                "İki strand",
                "from biolab.sequence import reverse_complement\nreverse_complement(dna)",
                "Minus strand koordinatları niyə genom koordinatına çevrilir?",
            ),
            (
                "Namizəd ORF",
                "from biolab.orfs import find_orfs\nfind_orfs('ATG'+('AAA'*10)+'TAA',min_aa=5)",
                "Minimum uzunluq false positive sayına necə təsir edir?",
            ),
        ],
    ),
    "08-research-controls": (
        "Nəticəni sınayan nəzarətlər",
        [
            (
                "İddianı yazmaq",
                "claim={'observation':'model score is high','claim':'signal generalizes','alternative':'leakage or small-sample variance'};claim",
                "Observation ilə causal claim arasında hansı körpü çatmır?",
            ),
            (
                "Data split sərhədi",
                "train=set(range(8));test=set(range(8,10));train.isdisjoint(test)",
                "Feature selection hansı tərəfdə aparılmalıdır?",
            ),
            (
                "Permutation p-value",
                "from biolab.sensitivity import permutation_pvalue\npermutation_pvalue(.9,[.3,.4,.5,.6,.7,.8,.2,.1,.45])",
                "Niyə numerator və denominator-a bir əlavə olunur?",
            ),
            (
                "Singleton GO control",
                "from biolab.sensitivity import singleton_enrichment\nsingleton_enrichment(range(10),{'termA':{0,1},'termB':{2,3,4}},min_size=2).head()",
                "Family eyni saxlanmasa control nəyi dəyişmiş olar?",
            ),
            (
                "Sensitivity analysis",
                "import numpy as np\nthresholds=[.3,.5,.7];prob=np.array([.2,.4,.6,.8]);[(t,int((prob>=t).sum())) for t in thresholds]",
                "Nəticə bir threshold-da kəskin dəyişirsə necə hesabat verərsiniz?",
            ),
            (
                "Reproduksiya qeydi",
                "from pathlib import Path\nrequired=['inputs','parameters','software','outputs','limitations'];required",
                "Hash mənanı yoxsa yalnız byte bütövlüyünü sübut edir?",
            ),
            (
                "Qərar matrisi",
                "import pandas as pd\npd.DataFrame([['positive','repeat'],['negative','report boundary'],['unstable','collect data']],columns=['control','next_step'])",
                "Mənfi nəticəni findings jurnalına yazmaq niyə dəyərlidir?",
            ),
        ],
    ),
}


def build() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for stem, (title, sections) in LESSONS.items():
        cells = [
            nbformat.v4.new_markdown_cell(
                f"# {title}\n\nBu notebook bir wrapper deyil: hər mərhələdə ara nəticə, fərziyyə və yoxlama sualı görünür."
            ),
            nbformat.v4.new_markdown_cell(
                "## Öyrənmə məqsədi\n\nMəlumat strukturunu oxumaq, hesablamanı kiçik nümunədə görmək, nəticə ilə iddia arasındakı sərhədi yazmaq."
            ),
            nbformat.v4.new_code_cell(
                "from pathlib import Path\nROOT=Path.cwd()\nprint('repo:',ROOT.name)"
            ),
        ]
        for number, (heading, code, question) in enumerate(sections, 1):
            cells.extend(
                [
                    nbformat.v4.new_markdown_cell(
                        f"## {number}. {heading}\n\nƏvvəl kiçik və görünən nümunədə mexanizmi yoxlayın; sonra böyük layihə çıxışına keçin."
                    ),
                    nbformat.v4.new_code_cell(code),
                    nbformat.v4.new_markdown_cell(
                        f"**Özünü yoxla:** {question}\n\nCavabınızı bir cümləlik fərziyyə və onu sınayan bir əmrlə yazın."
                    ),
                ]
            )
        notebook = nbformat.v4.new_notebook(
            cells=cells,
            metadata={
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3",
                },
                "language_info": {"name": "python", "version": "3.12"},
            },
        )
        NotebookClient(
            notebook,
            timeout=120,
            kernel_name="python3",
            resources={"metadata": {"path": str(ROOT)}},
        ).execute()
        nbformat.write(notebook, OUT / f"{stem}.ipynb")


if __name__ == "__main__":
    build()
