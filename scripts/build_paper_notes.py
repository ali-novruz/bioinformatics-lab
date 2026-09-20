"""Build structured analytical notes for foundational bioinformatics papers."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research/papers"

PAPERS = {
    "needleman-wunsch": (
        "A general method applicable to the search for similarities in the amino acid sequence of two proteins",
        "Needleman & Wunsch",
        1970,
        "https://doi.org/10.1016/0022-2836(70)90057-4",
        "global dynamic programming",
        "an optimal end-to-end alignment under an explicit scoring model",
        "quadratic time/memory and score-model dependence",
        "notebooks/learn/02-alignment.ipynb",
    ),
    "smith-waterman": (
        "Identification of common molecular subsequences",
        "Smith & Waterman",
        1981,
        "https://doi.org/10.1016/0022-2836(81)90087-5",
        "local dynamic programming with zero reset",
        "an optimal local alignment under the chosen scores",
        "quadratic cost and no database-scale statistical calibration",
        "notebooks/learn/02-alignment.ipynb",
    ),
    "clustal-omega": (
        "Fast, scalable generation of high-quality protein multiple sequence alignments",
        "Sievers et al.",
        2011,
        "https://doi.org/10.1038/msb.2011.75",
        "guide trees and profile HMM alignment",
        "scalable protein multiple alignment",
        "alignment quality depends on homology, sequence composition and benchmark choice",
        "projects/intermediate/phylogeny/README.md",
    ),
    "hmmer3": (
        "Accelerated profile HMM searches",
        "Eddy",
        2011,
        "https://doi.org/10.1371/journal.pcbi.1002195",
        "profile hidden Markov models with filter pipelines",
        "sensitive family/domain sequence search",
        "a significant family hit is not direct functional validation",
        "resources/databases/pfam.md",
    ),
    "bowtie2": (
        "Fast gapped-read alignment with Bowtie 2",
        "Langmead & Salzberg",
        2012,
        "https://doi.org/10.1038/nmeth.1923",
        "FM-index seed-and-extend alignment",
        "fast gapped short-read mapping",
        "multi-mapping and reference bias remain analysis decisions",
        "workflows/variants.sh",
    ),
    "star": (
        "STAR: ultrafast universal RNA-seq aligner",
        "Dobin et al.",
        2013,
        "https://doi.org/10.1093/bioinformatics/bts635",
        "sequential maximum mappable seed search and splice-aware stitching",
        "fast splice-junction-aware RNA-seq alignment",
        "index resources, annotation and multi-mapping policy affect counts",
        "workflows/rnaseq.sh",
    ),
    "hisat2": (
        "Graph-based genome alignment and genotyping with HISAT2 and HISAT-genotype",
        "Kim et al.",
        2019,
        "https://doi.org/10.1038/s41587-019-0201-4",
        "hierarchical FM indexes and graph references",
        "memory-efficient spliced/variant-aware alignment",
        "graph content and benchmark composition influence apparent gains",
        "workflows/README.md",
    ),
    "samtools": (
        "The Sequence Alignment/Map format and SAMtools",
        "Li et al.",
        2009,
        "https://doi.org/10.1093/bioinformatics/btp352",
        "SAM/BAM specification and indexed manipulation",
        "interoperable alignment storage and processing",
        "valid BAM does not imply correct mapping or sample provenance",
        "docs/data-formats/sam.md",
    ),
    "bedtools": (
        "BEDTools: a flexible suite of utilities for comparing genomic features",
        "Quinlan & Hall",
        2010,
        "https://doi.org/10.1093/bioinformatics/btq033",
        "interval algebra",
        "streaming overlap, coverage and proximity operations",
        "coordinate convention, strand and overlap fraction must be explicit",
        "docs/data-formats/bed.md",
    ),
    "edger": (
        "edgeR: a Bioconductor package for differential expression analysis",
        "Robinson, McCarthy & Smyth",
        2010,
        "https://doi.org/10.1093/bioinformatics/btp616",
        "negative-binomial models with empirical Bayes dispersion",
        "replicate-aware count comparison",
        "design, normalization and dispersion assumptions remain decisive",
        "projects/intermediate/rnaseq/README.md",
    ),
    "limma-voom": (
        "voom: precision weights unlock linear model analysis tools for RNA-seq read counts",
        "Law et al.",
        2014,
        "https://doi.org/10.1186/gb-2014-15-2-r29",
        "mean-variance trend and precision-weighted linear models",
        "linear-model analysis of transformed RNA-seq counts",
        "low counts and trend estimation require diagnostics",
        "docs/statistics/README.md",
    ),
    "tsne": (
        "Visualizing Data using t-SNE",
        "van der Maaten & Hinton",
        2008,
        "https://www.jmlr.org/papers/v9/vandermaaten08a.html",
        "neighbour-probability matching with KL divergence",
        "local-neighbour visualization",
        "global distance, cluster size and run-to-run stability are not preserved",
        "notebooks/learn/05-machine-learning.ipynb",
    ),
    "umap": (
        "UMAP: Uniform Manifold Approximation and Projection",
        "McInnes, Healy & Melville",
        2018,
        "https://doi.org/10.21105/joss.00861",
        "neighbour graph and low-dimensional fuzzy-set optimization",
        "fast nonlinear embedding",
        "embedding geometry depends on metric, neighbours, min_dist and seed",
        "notebooks/learn/05-machine-learning.ipynb",
    ),
    "scanpy": (
        "Scanpy: large-scale single-cell gene expression data analysis",
        "Wolf, Angerer & Theis",
        2018,
        "https://doi.org/10.1186/s13059-017-1382-0",
        "Python single-cell preprocessing and graph analysis",
        "scalable AnnData-centred workflows",
        "default pipelines do not solve donor replication, batch or annotation validity",
        "docs/data-formats/h5ad-10x.md",
    ),
    "harmony": (
        "Fast, sensitive and accurate integration of single-cell data with Harmony",
        "Korsunsky et al.",
        2019,
        "https://doi.org/10.1038/s41592-019-0619-0",
        "iterative clustering and diversity-penalized correction",
        "embedding-level batch integration",
        "overcorrection can remove biological signal; labels and donor structure require audit",
        "docs/data-formats/h5ad-10x.md",
    ),
    "scvi": (
        "Deep generative modeling for single-cell transcriptomics",
        "Lopez et al.",
        2018,
        "https://doi.org/10.1038/s41592-018-0229-2",
        "hierarchical variational autoencoder for counts",
        "probabilistic latent representation and uncertainty",
        "model fit and latent separation do not establish biological causality",
        "docs/data-formats/h5ad-10x.md",
    ),
    "minimap2": (
        "Minimap2: pairwise alignment for nucleotide sequences",
        "Li",
        2018,
        "https://doi.org/10.1093/bioinformatics/bty191",
        "minimizer seeding, chaining and dynamic-programming extension",
        "fast long-read and assembly alignment",
        "preset, error profile and secondary alignment policy change results",
        "docs/data-formats/long-read.md",
    ),
    "spades": (
        "SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing",
        "Bankevich et al.",
        2012,
        "https://doi.org/10.1089/cmb.2012.0021",
        "multi-k de Bruijn graph assembly",
        "short-read microbial assembly",
        "repeat resolution and contamination depend on coverage and library assumptions",
        "docs/data-formats/gfa.md",
    ),
    "flye": (
        "Assembly of long, error-prone reads using repeat graphs",
        "Kolmogorov et al.",
        2019,
        "https://doi.org/10.1038/s41587-019-0072-8",
        "repeat-graph construction and consensus",
        "long-read de novo assembly",
        "coverage, heterozygosity, repeats and polishing determine final accuracy",
        "docs/data-formats/gfa.md",
    ),
    "metaphlan2": (
        "MetaPhlAn2 for enhanced metagenomic taxonomic profiling",
        "Truong et al.",
        2015,
        "https://doi.org/10.1038/nmeth.3589",
        "clade-specific marker mapping",
        "species-level community profiling",
        "relative abundance is compositional and database coverage limits discovery",
        "resources/databases/silva-mgnify.md",
    ),
    "qiime2": (
        "Reproducible, interactive, scalable and extensible microbiome data science using QIIME 2",
        "Bolyen et al.",
        2019,
        "https://doi.org/10.1038/s41587-019-0209-9",
        "provenance-tracked plugin workflows",
        "auditable amplicon/microbiome analysis",
        "provenance does not repair biased sampling, contaminants or compositional inference",
        "resources/databases/silva-mgnify.md",
    ),
    "plink": (
        "PLINK: a tool set for whole-genome association and population-based linkage analyses",
        "Purcell et al.",
        2007,
        "https://doi.org/10.1086/519795",
        "efficient genotype QC and association tests",
        "large-cohort GWAS workflows",
        "population structure, relatedness and phenotype definition drive false associations",
        "docs/data-formats/plink.md",
    ),
    "esm2": (
        "Evolutionary-scale prediction of atomic-level protein structure with a language model",
        "Lin et al.",
        2023,
        "https://doi.org/10.1126/science.ade2574",
        "protein language modelling and structure prediction",
        "sequence representations and predicted folds",
        "training-corpus leakage, confidence and function inference require separate evaluation",
        "resources/databases/alphafold-db.md",
    ),
    "enformer": (
        "Effective gene expression prediction from sequence by integrating long-range interactions",
        "Avsec et al.",
        2021,
        "https://doi.org/10.1038/s41592-021-01252-x",
        "long-context convolution and attention",
        "sequence-to-functional-track prediction",
        "prediction does not identify causal mechanism; cell type and training distribution matter",
        "resources/databases/encode.md",
    ),
    "t2t-chm13": (
        "The complete sequence of a human genome",
        "Nurk et al.",
        2022,
        "https://doi.org/10.1126/science.abj6987",
        "long-read, HiFi and assembly finishing",
        "telomere-to-telomere reference sequence",
        "one haploid-derived reference does not represent global human diversity",
        "docs/data-formats/long-read.md",
    ),
    "human-genome": (
        "Initial sequencing and analysis of the human genome",
        "International Human Genome Sequencing Consortium",
        2001,
        "https://doi.org/10.1038/35057062",
        "hierarchical clone-based genome sequencing and annotation",
        "a public draft human reference",
        "draft gaps, assembly errors and limited representation shaped downstream analyses",
        "docs/molecular-biology/README.md",
    ),
}


def main() -> None:
    for slug, (
        title,
        authors,
        year,
        source,
        method,
        supports,
        limitation,
        link,
    ) in PAPERS.items():
        note = f"""# {title}

**Authors:** {authors}

**Year:** {year}

**Primary source:** [{source}]({source})
**Reading status:** method, principal evidence and limitations reviewed; no full-paper reproduction claimed.

## Question and method

The paper asks how to obtain {supports}. Its central method is **{method}**. Input unit, objective function, validation dataset and comparison baseline must be read together; the tool name alone does not define an analysis.

## What the evidence supports

The reported experiments support the method in the paper's datasets and benchmark design. They do not automatically validate a new species, instrument, cohort or clinical use. Reproduction means matching versioned inputs, parameters and evaluation—not merely invoking a similarly named package.

## Main limitation to carry into this repository

{limitation}. Any local result must therefore report data origin, split/unit, parameter version, uncertainty and the claim boundary.

## Repository connection

See [`{link}`](../../{link}). A useful exercise is to identify which paper assumptions are satisfied there, which are only approximated, and one control that would falsify the local interpretation.

## Next experiment

Freeze one small input and metric, run the baseline and one controlled variation, preserve all outputs, and explain disagreement before expanding the dataset. Negative and unstable results belong in `research/findings/` as much as positive results.
"""
        (OUT / f"{slug}.md").write_text(note, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
