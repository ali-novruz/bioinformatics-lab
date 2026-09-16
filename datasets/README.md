# Dataset idarəetməsi

- [Pasilla RNA-seq gene counts](public-datasets/pasilla.md)
- [PhiX174 referens genomu](public-datasets/phix.md)
- [GIAB HG001 benchmark prefix](public-datasets/giab.md)
- [Wisconsin Diagnostic Breast Cancer](public-datasets/wdbc.md)
- [Human insulin precursor sequence](public-datasets/uniprot.md)
- [Crambin crystal structure](public-datasets/pdb.md)
- [GSE110004 real xam RNA-seq — altı sample](public-datasets/raw-rnaseq.md)
- [nf-core/sarek xarici DNA workflow nümunəsi](public-datasets/raw-variants.md)

## Böyük gələcək dataset-lər

| Resurs | Giriş və endirmə | Feature-lər / məna | Ölçü və şərtlər |
|---|---|---|---|
| [GEO/SRA](https://www.ncbi.nlm.nih.gov/geo/) | GSE/GSM → SRA/ENA run metadata → FASTQ URL/Toolkit | Reads + sample phenotype | Study-dən asılı GB–TB; accession seçilməyib, uydurulmur |
| [TCGA/GDC](https://portal.gdc.cancer.gov/) | Cohort/query → file manifest → GDC transfer | Counts, variants, methylation, clinical covariates | Query seçildikdən sonra portal ölçüsü; open/controlled ayrıdır |
| [GTEx](https://gtexportal.org/home/datasets) | Dated release downloads; individual-level üçün dbGaP | Gene/tissue expression, eQTL | Fayldan asılı ölçü; access və consent ayrıca yoxlanır |
| [ENA](https://www.ebi.ac.uk/ena/browser/) | Portal API run accession üçün fastq_ftp/fastq_bytes/fastq_md5 | Xam reads və assay metadata | API-dən byte ölçüsü çıxarılır; böyük data otomatik endirilmir |

## Reproducibility

`python scripts/fetch_data.py --dataset all` kiçik mənbələri endirir. `reference-manifest.json` gözlənən SHA-256 snapshot-u, `raw/provenance.json` isə yerli retrieval tarixini saxlayır. Mövcud fayl hash-i dəyişibsə skript dayanır. GIAB subset hash-i tam 120 MB arxiv hash-i deyil.

## Fixture-lər

`fixtures/toy.fasta` və `fixtures/toy.vcf` tam sintetik, repoda yaradılmış test nümunələridir. Bunlardan biological discovery çıxarılmır. Bütün nəticələr data tipini bildirir.

## Gen ifadəsi benchmark

[Khan mikroarray məlumat kartı](public-datasets/khan.md). `python scripts/fetch_khan.py` sabit revision-dan dörd CSV endirir və hash-ləri yoxlayır.
