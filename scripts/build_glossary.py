"""Build the bilingual glossary from a compact, reviewed term catalog."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CATEGORIES = [
    (
        "Molekulyar biologiya",
        "docs/molecular-biology/README.md",
        "molekulyar prosesləri və bioloji vahidləri dəqiq adlandırmaq üçün işlədilir",
        "DNT|DNA;RNT|RNA;gen|gene;genom|genome;xromosom|chromosome;allel|allele;lokus|locus;nukleotid|nucleotide;baza cütü|base pair;DNT replikasiyası|DNA replication;transkripsiya|transcription;translyasiya|translation;kodon|codon;antikodon|anticodon;ekzon|exon;intron|intron;promotor|promoter;enhancer|enhancer;fenotip|phenotype;genotip|genotype",
    ),
    (
        "Ardıcıllıq analizi",
        "docs/sequence-analysis/README.md",
        "ardıcıllıqların müqayisəsi, axtarışı və keyfiyyət nəzarətində istifadə olunur",
        "ardıcıllıq|sequence;read|read;contig|contig;k-mer|k-mer;motiv|motif;uyğunlaşdırma|alignment;qlobal uyğunlaşdırma|global alignment;lokal uyğunlaşdırma|local alignment;gap|gap;gap açma cəzası|gap-open penalty;gap uzatma cəzası|gap-extension penalty;əvəzləmə matrisi|substitution matrix;uyğunluq faizi|percent identity;əhatə|coverage;E-qiyməti|E-value;bit score|bit score;çoxlu uyğunlaşdırma|multiple sequence alignment;profil HMM|profile HMM;konsensus ardıcıllıq|consensus sequence;tərs komplement|reverse complement",
    ),
    (
        "Genomika",
        "docs/genomics/README.md",
        "genom miqyaslı məlumatın qurulması və ölçülməsini təsvir edir",
        "referens genom|reference genome;genom yığımı|genome assembly;iskele|scaffold;gap bağlama|gap closing;xəritələmə|mapping;çoxxəritələnən read|multi-mapping read;xəritələmə keyfiyyəti|mapping quality;insert ölçüsü|insert size;paired-end|paired-end;read dərinliyi|read depth;genom əhatəsi|genome coverage;duplikat read|duplicate read;GC qərəzi|GC bias;unikal bölgə|unique region;təkrar element|repetitive element;sentromer|centromere;telomer|telomere;pangenom|pangenome;haplotip|haplotype;fazalama|phasing",
    ),
    (
        "Variantlar və annotasiya",
        "docs/data-formats/vcf.md",
        "genetik variantın təqdimatı, filtri və annotasiyasında istifadə olunur",
        "variant|variant;SNV|single-nucleotide variant;indel|indel;struktur variant|structural variant;copy-number variant|copy-number variant;referens allel|reference allele;alternativ allel|alternate allele;genotip keyfiyyəti|genotype quality;allel dərinliyi|allele depth;variant keyfiyyəti|variant quality;filter statusu|filter status;normallaşdırma|normalization;sola hizalama|left alignment;multiallelik sahə|multiallelic site;funksional nəticə|functional consequence;missense variant|missense variant;nonsense variant|nonsense variant;synonymous variant|synonymous variant;splice variantı|splice variant;variant allel tezliyi|variant allele frequency",
    ),
    (
        "Transkriptomika",
        "docs/transcriptomics/README.md",
        "RNT ifadəsinin ölçülməsi və diferensial analizində istifadə olunur",
        "transkriptom|transcriptome;transkript|transcript;izoform|isoform;gen ifadəsi|gene expression;raw count|raw count;kitabxana ölçüsü|library size;normallaşdırma faktoru|normalization factor;TPM|TPM;CPM|CPM;dispersiya|dispersion;overdispersion|overdispersion;diferensial ifadə|differential expression;log fold change|log fold change;design matrix|design matrix;contrast|contrast;batch effekti|batch effect;size factor|size factor;pseudocount|pseudocount;allele-specific expression|allele-specific expression;splice junction|splice junction",
    ),
    (
        "Tək hüceyrə və spatial",
        "docs/transcriptomics/README.md",
        "tək hüceyrə və məkan məlumatında bioloji vahid və texniki effekti ayırmağa kömək edir",
        "tək hüceyrə RNT-seq|single-cell RNA-seq;damcı|droplet;barcode|cell barcode;UMI|unique molecular identifier;doublet|doublet;dropout|dropout;hüceyrə tipi|cell type;klaster|cluster;marker gen|marker gene;pseudobulk|pseudobulk;pseudotime|pseudotime;trajectory|trajectory;latent space|latent space;inteqrasiya|integration;anchor|anchor;batch correction|batch correction;spatial transcriptomics|spatial transcriptomics;spot|spot;deconvolution|deconvolution;donor effekti|donor effect",
    ),
    (
        "Proteomika",
        "docs/proteomics/README.md",
        "proteinlərin quruluşu, bolluğu və kütlə spektrometriyası analizində istifadə olunur",
        "protein|protein;peptid|peptide;amin turşusu|amino acid;protein domeni|protein domain;aktiv sahə|active site;post-translyasiya modifikasiyası|post-translational modification;proteom|proteome;proteoform|proteoform;kütlə spektrometriyası|mass spectrometry;prekursor ion|precursor ion;fragment ion|fragment ion;kütlə-yük nisbəti|mass-to-charge ratio;retention time|retention time;spektr uyğunluğu|peptide-spectrum match;peptid-səviyyəli FDR|peptide-level FDR;label-free quantification|label-free quantification;izobarik etiket|isobaric tag;missed cleavage|missed cleavage;decoy database|decoy database;protein inference|protein inference",
    ),
    (
        "Struktur bioinformatikası",
        "docs/structural-bioinformatics/README.md",
        "biomolekulun üçölçülü quruluşunu və qarşılıqlı təsirini təsvir edir",
        "zülal quruluşu|protein structure;ilkin quruluş|primary structure;ikincili quruluş|secondary structure;üçüncülü quruluş|tertiary structure;dördüncülü quruluş|quaternary structure;alfa spiral|alpha helix;beta təbəqə|beta sheet;kontakt xəritəsi|contact map;RMSD|root-mean-square deviation;Ramachandran qrafiki|Ramachandran plot;confidence score|confidence score;docking|molecular docking;ligand|ligand;reseptor|receptor;binding pocket|binding pocket;molekulyar dinamika|molecular dynamics;force field|force field;enerji minimallaşdırması|energy minimization;solvent accessibility|solvent accessibility;homologiya modelləşdirməsi|homology modeling",
    ),
    (
        "Statistika",
        "docs/statistics/README.md",
        "qeyri-müəyyənliyi ölçmək və nəticəni düzgün şərh etmək üçün istifadə olunur",
        "ehtimal|probability;random dəyişən|random variable;gözlənilən qiymət|expected value;variasiya|variance;standart xəta|standard error;confidence interval|confidence interval;credible interval|credible interval;null hipotez|null hypothesis;alternativ hipotez|alternative hypothesis;p-qiyməti|p-value;test statistikası|test statistic;effekt ölçüsü|effect size;statistik güc|statistical power;çoxlu test|multiple testing;ailəvi xəta faizi|family-wise error rate;yanlış kəşf faizi|false discovery rate;bootstrap|bootstrap;permutation test|permutation test;confounder|confounder;sensitivity analysis|sensitivity analysis",
    ),
    (
        "Maşın öyrənməsi",
        "docs/machine-learning/README.md",
        "proqnoz modelinin hazırlanması və qərəzsiz qiymətləndirilməsində istifadə olunur",
        "xüsusiyyət|feature;etiket|label;training set|training set;validation set|validation set;test set|test set;cross-validation|cross-validation;nested cross-validation|nested cross-validation;data sızması|data leakage;overfitting|overfitting;underfitting|underfitting;hiperparametr|hyperparameter;pipeline|pipeline;kalibrasiya|calibration;confusion matrix|confusion matrix;dəqiqlik|precision;həssaslıq|recall;specificity|specificity;balanced accuracy|balanced accuracy;ROC əyrisi|ROC curve;AUROC|area under the ROC curve",
    ),
    (
        "Populyasiya və filogeniya",
        "docs/genetics/README.md",
        "populyasiya quruluşunu və təkamül əlaqələrini modelləşdirmək üçün istifadə olunur",
        "allel tezliyi|allele frequency;Hardy-Weinberg tarazlığı|Hardy-Weinberg equilibrium;linkage disequilibrium|linkage disequilibrium;rekombinasiya|recombination;genetik drift|genetic drift;seçmə|selection;effektiv populyasiya ölçüsü|effective population size;populyasiya strukturu|population structure;əsas komponent analizi|principal component analysis;GWAS|genome-wide association study;kinship|kinship;relatedness|relatedness;filogeniya|phylogeny;filogenetik ağac|phylogenetic tree;klad|clade;branch length|branch length;bootstrap support|bootstrap support;neighbor joining|neighbor joining;maximum likelihood|maximum likelihood;ortoloq|ortholog",
    ),
    (
        "Metagenomika",
        "docs/systems-biology/README.md",
        "mikrob icmasının tərkibi və funksiyasını analiz etmək üçün istifadə olunur",
        "mikrobiom|microbiome;metagenom|metagenome;taksonomiya|taxonomy;OTU|operational taxonomic unit;ASV|amplicon sequence variant;amplicon|amplicon;shotgun metagenomika|shotgun metagenomics;alfa müxtəlifliyi|alpha diversity;beta müxtəlifliyi|beta diversity;növ zənginliyi|species richness;bərabərlik|evenness;relative abundance|relative abundance;absolute abundance|absolute abundance;kompozisional məlumat|compositional data;kontaminasiya|contamination;mock community|mock community;taxonomic classifier|taxonomic classifier;strain profiling|strain profiling;functional profiling|functional profiling;rare taxa|rare taxa",
    ),
    (
        "Formatlar və workflow",
        "docs/data-formats/README.md",
        "məlumat mübadiləsi və təkrar icra olunan pipeline qurmaq üçün istifadə olunur",
        "FASTA|FASTA;FASTQ|FASTQ;SAM|SAM;BAM|BAM;CRAM|CRAM;VCF|VCF;BED|BED;GFF|GFF;Newick|Newick;HDF5|HDF5;Zarr|Zarr;metadata|metadata;manifest|manifest;checksum|checksum;workflow|workflow;dependency lock|dependency lock;container|container;provenance|provenance;run manifest|run manifest;continuous integration|continuous integration",
    ),
    (
        "Klinik və tibbi genetika",
        "docs/regional-genetics/README.md",
        "variant sübutunu klinik kontekstdə məhdud və izlənilə bilən formada təqdim edir",
        "patogenlik|pathogenicity;benign variant|benign variant;uncertain significance|variant of uncertain significance;penetrance|penetrance;ekspressivlik|expressivity;irsi model|mode of inheritance;dominant|dominant;resessiv|recessive;de novo variant|de novo variant;compound heterozygote|compound heterozygote;segregasiya|segregation;fenotip uyğunluğu|phenotype match;klinik validasiya|clinical validation;analitik validasiya|analytical validation;actionability|clinical actionability;carrier|carrier;proband|proband;trio analysis|trio analysis;consent|informed consent;incidental finding|incidental finding",
    ),
    (
        "Epigenomika",
        "roadmap/domain-gaps.md",
        "genomun ardıcıllıq dəyişmədən tənzimlənən vəziyyətini ölçmək üçün istifadə olunur",
        "epigenom|epigenome;DNA metilasiyası|DNA methylation;CpG sahəsi|CpG site;bisulfit sequencing|bisulfite sequencing;ATAC-seq|ATAC-seq;ChIP-seq|ChIP-seq;peak|peak;peak calling|peak calling;chromatin accessibility|chromatin accessibility;histone modification|histone modification;nukleosom|nucleosome;enhancer-promoter əlaqəsi|enhancer-promoter interaction;FRiP|fraction of reads in peaks;TSS enrichment|TSS enrichment;footprinting|footprinting;diferensial əlçatanlıq|differential accessibility;epigenetik saat|epigenetic clock;imprinting|genomic imprinting;X-inaktivasiya|X-inactivation;chromatin state|chromatin state",
    ),
    (
        "Təkrar istehsal və tədqiqat",
        "docs/REPOSITORY_AUDIT.md",
        "elmi işin izlənilməsi, yoxlanması və iddia sərhədinin yazılması üçün istifadə olunur",
        "təkrar istehsal|reproducibility;təkrarlama|replication;hipotez|hypothesis;tədqiqat sualı|research question;protokol|protocol;öncədən qeydiyyat|preregistration;mənfi nəzarət|negative control;müsbət nəzarət|positive control;ablation|ablation study;benchmark|benchmark;truth set|truth set;gold standard|gold standard;xarici validasiya|external validation;daxili validasiya|internal validation;data mənşəyi|data provenance;versiyalama|versioning;toxum dəyəri|random seed;məhdudiyyət|limitation;ümumiləşdirmə|generalization;elmi iddia|scientific claim",
    ),
]


def main() -> None:
    rows: list[tuple[str, str, str, str, str]] = []
    for category, link, purpose, packed in CATEGORIES:
        for item in packed.split(";"):
            az, en = item.split("|", maxsplit=1)
            definition = (
                f"**{az}** {purpose}; ingiliscə qarşılığı **{en}** kimi yazılır."
            )
            rows.append((category, az, en, definition, link))

    english = [row[2].casefold() for row in rows]
    if len(rows) < 300 or len(english) != len(set(english)):
        raise ValueError("Glossary must contain at least 300 unique English terms")

    lines = [
        "# AZ–EN bioinformatika lüğəti",
        "",
        f"Bu lüğətdə **{len(rows)} unikal termin** var. Təriflər tədris üçün qısadır; hər termin daha dərin repository bölməsinə bağlanır.",
        "",
        "| № | Azərbaycan dili | English | Qısa izah və repo keçidi |",
        "|---:|---|---|---|",
    ]
    for number, (_, az, en, definition, link) in enumerate(rows, 1):
        relative_link = (
            link.removeprefix("docs/") if link.startswith("docs/") else f"../{link}"
        )
        lines.append(
            f"| {number} | {az} | {en} | {definition} [Davamı]({relative_link}) |"
        )
    lines.extend(
        [
            "",
            "## İstifadə qaydası",
            "",
            "Termin ilk dəfə işlədiləndə Azərbaycan dilində adı və mötərizədə English qarşılığı verin. Klinik və statistik terminlərdə qısa lüğət tərifini qərar qaydası kimi istifadə etməyin; bağlı bələdçidəki fərziyyə və məhdudiyyətləri oxuyun.",
            "",
            "Bu fayl `python scripts/build_glossary.py` ilə deterministik yaradılır. Yeni termin əlavə edəndə English adı təkrar etməyin.",
        ]
    )
    (ROOT / "docs" / "glossary.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(f"Wrote {len(rows)} unique glossary terms")


if __name__ == "__main__":
    main()
