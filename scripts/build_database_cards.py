"""Generate the reviewed expanded database cards from structured metadata."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "resources/databases"

CARDS = {
    "gnomad": (
        "gnomAD",
        "population allele frequency, coverage and constraint",
        "variant, gene and ancestry-aware frequency fields",
        "GraphQL/API, browser and release downloads",
        "Absence is not proof of pathogenicity; ancestry, coverage, sex chromosome ploidy and release must be recorded.",
        "Compare a ClinVar assertion with ancestry-specific frequency without turning frequency into a diagnosis.",
        "https://gnomad.broadinstitute.org/help",
    ),
    "cosmic": (
        "COSMIC",
        "expert-curated somatic alterations in cancer",
        "COSV mutation IDs, genes, samples, tumour site and publication evidence",
        "licensed downloads and web interface",
        "Coverage and licensing vary by product; mutation recurrence reflects ascertainment and cohort design.",
        "Audit one TP53 alteration across tumour sites and separate sample count from patient count.",
        "https://cancer.sanger.ac.uk/cosmic/help",
    ),
    "civic": (
        "CIViC",
        "open, community-curated clinical interpretations of cancer variants",
        "variant, disease, drug, evidence item, evidence level and assertion",
        "GraphQL/REST API and bulk releases",
        "Evidence items may disagree and have different evidence levels; snapshot version and review state matter.",
        "Build an evidence table grouped by disease and evidence level, preserving conflicts.",
        "https://civic.readthedocs.io/",
    ),
    "pharmgkb": (
        "PharmGKB",
        "gene–drug and variant–drug pharmacogenomic knowledge",
        "variant annotation, clinical annotation, guideline and pathway",
        "website, API and licensed downloads",
        "A guideline recommendation depends on diplotype, phenotype translation and jurisdiction; single SNP lookup is insufficient.",
        "Trace one CPIC-linked gene from allele definition to dosing recommendation and list missing patient context.",
        "https://www.pharmgkb.org/page/webServices",
    ),
    "interpro": (
        "InterPro",
        "integrated protein family, domain and site signatures",
        "InterPro entry, member-database signature, protein match and location",
        "REST API and release downloads",
        "Overlapping signatures are expected; family, domain and active-site matches have different semantics.",
        "Map an insulin sequence to domains and compare member-database agreement.",
        "https://www.ebi.ac.uk/interpro/api/",
    ),
    "pfam": (
        "Pfam",
        "profile-HMM protein families and domains",
        "family accession, seed/full alignment, HMM and clan",
        "InterPro/Pfam website and HMM downloads",
        "A domain hit needs gathering threshold, alignment coverage and composition checks; E-value alone is not function proof.",
        "Run an HMM search on a small protein set and inspect borderline coverage.",
        "https://pfam-docs.readthedocs.io/",
    ),
    "alphafold-db": (
        "AlphaFold DB",
        "predicted protein structures with confidence",
        "UniProt accession, model version, pLDDT and PAE",
        "website, API and bulk downloads",
        "Low pLDDT can reflect disorder; a confident fold does not establish interaction, ligand state or biological function.",
        "Compare a high-confidence domain and disordered tail, reporting confidence per residue.",
        "https://alphafold.ebi.ac.uk/api-docs",
    ),
    "hpo-monarch": (
        "HPO və Monarch",
        "phenotype ontology and cross-species disease–gene–phenotype integration",
        "HP term, disease/gene identifiers, evidence and provenance",
        "HPO downloads; Monarch API and knowledge graph",
        "Phenotype absence, age of onset, ontology version and negation must be preserved; propagated ancestors are not independent observations.",
        "Encode a small phenotype profile and rank only after documenting missing/negative terms.",
        "https://hpo.jax.org/data/ontology",
    ),
    "open-targets": (
        "Open Targets",
        "target–disease evidence integration for drug discovery",
        "target, disease, evidence source, association score and tractability",
        "GraphQL API, platform and downloads",
        "The aggregate score is a prioritization aid, not a causal effect or clinical efficacy probability.",
        "Decompose one target score by evidence source and remove one source as a sensitivity analysis.",
        "https://platform-docs.opentargets.org/data-access",
    ),
    "disgenet": (
        "DisGeNET",
        "gene/variant–disease associations aggregated from curated and literature sources",
        "gene, variant, disease, score, evidence and source",
        "API and licensed/download products",
        "Text-mined and curated records have different evidential weight; duplicated source claims must not be counted as independent.",
        "Compare curated-only and all-source rankings for one disease.",
        "https://disgenet.com/",
    ),
    "encode": (
        "ENCODE",
        "functional genomics assays, biosamples and processed tracks",
        "experiment, biosample, assay, file, assembly and audit flags",
        "REST API, portal and cloud downloads",
        "Replicate structure, antibody validation, blacklist filtering, assembly and revoked files are essential metadata.",
        "Select one ChIP-seq experiment using audit status and biological replicate rules before downloading.",
        "https://www.encodeproject.org/help/rest-api/",
    ),
    "thousand-genomes": (
        "1000 Genomes",
        "global human genetic variation reference panels",
        "sample, population, superpopulation, variant and phased haplotype",
        "IGSR FTP, browser and cloud resources",
        "Population labels are sampling categories, not fixed biological races; GRCh37/38 and panel release must be explicit.",
        "Calculate allele counts by declared population and discuss uncertainty for small groups.",
        "https://www.internationalgenome.org/data",
    ),
    "gencode-refseq": (
        "GENCODE və RefSeq",
        "reference gene/transcript annotation",
        "gene, transcript, exon, protein and versioned accession",
        "GTF/GFF, FASTA and APIs",
        "GENCODE and RefSeq models differ; mixing transcript IDs or stripping version suffixes can create silent mismatches.",
        "Join a count table to one annotation release and report unmatched/version-collapsed IDs.",
        "https://www.gencodegenes.org/pages/data_format.html",
    ),
    "mirbase": (
        "miRBase",
        "published microRNA sequences and annotation",
        "MI precursor and MIMAT mature accessions",
        "website and release FTP",
        "Names and confidence change between releases; predicted targets are not stored as validated regulatory effects.",
        "Resolve precursor-to-mature arms with a fixed release and list deprecated IDs.",
        "https://www.mirbase.org/download/",
    ),
    "rfam": (
        "Rfam",
        "non-coding RNA families, covariance models and alignments",
        "RF accession, seed/full alignment, covariance model and clan",
        "website, API and FTP",
        "Covariance-model significance depends on model threshold and sequence composition; family match is not expression evidence.",
        "Search a short RNA sequence and inspect structure-aware alignment coverage.",
        "https://docs.rfam.org/",
    ),
    "silva-mgnify": (
        "SILVA və MGnify",
        "ribosomal RNA taxonomy and microbiome analysis resources",
        "sequence/taxon identifiers, study/sample accessions and pipeline version",
        "SILVA releases; MGnify API and downloads",
        "Database release, primer region and classifier alter taxonomy; read abundance is compositional and not absolute biomass.",
        "Classify a tiny 16S set against one SILVA release and record unclassified reads.",
        "https://www.ebi.ac.uk/metagenomics/api/",
    ),
    "human-cell-atlas": (
        "Human Cell Atlas Data Portal",
        "single-cell datasets with donor, tissue and assay metadata",
        "project, donor, specimen, cell suspension, library and file",
        "portal, API and cloud manifests",
        "Cells are nested within donors; access restrictions, consent, batch and ontology versions must follow the files.",
        "Construct a donor-level pseudobulk design from portal metadata without treating cells as replicates.",
        "https://data.humancellatlas.org/apis",
    ),
    "depmap": (
        "DepMap",
        "cancer-cell-line dependency, expression, mutation and drug-sensitivity data",
        "cell line, gene effect, model metadata and release",
        "portal and release downloads",
        "Cell-line identity, lineage, batch and release are confounders; dependency score is not patient response.",
        "Test whether a dependency remains after lineage stratification.",
        "https://depmap.org/portal/download/",
    ),
    "biogrid": (
        "BioGRID",
        "curated genetic and protein interactions",
        "interactor IDs, experimental system, publication and organism",
        "web services and downloads",
        "Interaction type, assay and evidence count matter; network degree is strongly affected by research popularity.",
        "Build an assay-stratified subnetwork and compare it with the unfiltered graph.",
        "https://wiki.thebiogrid.org/doku.php/biogridrest",
    ),
    "sgd-flybase": (
        "SGD və FlyBase",
        "model-organism genes, alleles, phenotypes and functional annotation",
        "stable gene/allele IDs, GO evidence, strain and publication",
        "official APIs/downloads",
        "Orthology does not transfer phenotype automatically; species, strain, evidence code and release remain explicit.",
        "Trace one yeast GO-slim gene and one Drosophila Pasilla identifier to current records.",
        "https://www.yeastgenome.org/webservice/doc",
    ),
}


def main() -> None:
    for slug, (
        name,
        scope,
        identifiers,
        access,
        caveat,
        exercise,
        url,
    ) in CARDS.items():
        text = f"""# {name}

## Nəyi saxlayır

{name} {scope} üçün istifadə olunur. Əsas vahidlər: {identifiers}.

## Giriş və versiyalama

Giriş yolu: {access}. Hər dataset kartında release/snapshot, retrieval tarixi, query və qaytarılan fayl hash-i saxlanmalıdır. ID-ləri yalnız görünən label ilə əvəz etməyin.

## Əsas şərh riski

{caveat}

## Praktiki tapşırıq

{exercise} Nəticədə source record link-i, daxil edilmə/xaric edilmə qaydası, missingness və iddia sərhədi ayrıca göstərilsin.

## Keyfiyyət nəzarəti

Schema və ID unikallığını, species/build uyğunluğunu, version drift-i, duplicate evidence-i və istifadə şərtlərini yoxlayın. API cavabını bioloji ground truth kimi qəbul etməyin; ilkin mənbəyə və evidence sahəsinə keçin.

Rəsmi başlanğıc: [{name}]({url}).
"""
        (OUT / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
