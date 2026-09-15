# Alətlər və seçim meyarları

| Alət | Rol | Sənəd |
|---|---|---|
| BLAST | Seed-extend sequence search | [rəsmi](https://blast.ncbi.nlm.nih.gov/doc/blast-help/) |
| BWA | Short-read DNA mapping | [rəsmi](https://github.com/lh3/bwa) |
| Bowtie2 | Gapped short-read alignment | [rəsmi](https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml) |
| STAR | Splice-aware RNA alignment | [rəsmi](https://github.com/alexdobin/STAR) |
| HISAT2 | Splice-aware və graph alignment | [rəsmi](https://daehwankimlab.github.io/hisat2/) |
| SAMtools | SAM/BAM/CRAM əməliyyatları | [rəsmi](https://www.htslib.org/doc/samtools.html) |
| BCFtools | Variant calling, normalize/filter | [rəsmi](https://samtools.github.io/bcftools/) |
| GATK | Germline/somatic workflows | [rəsmi](https://gatk.broadinstitute.org/) |
| FastQC | Read QC | [rəsmi](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) |
| MultiQC | QC hesabatlarının birləşdirilməsi | [rəsmi](https://docs.seqera.io/multiqc) |
| Cutadapt | Adapter trimming | [rəsmi](https://cutadapt.readthedocs.io/) |
| Trimmomatic | Read trimming | [rəsmi](https://github.com/usadellab/Trimmomatic) |
| VEP | Variant consequence annotation | [rəsmi](https://www.ensembl.org/info/docs/tools/vep/index.html) |
| SnpEff | Variant functional annotation | [rəsmi](https://pcingola.github.io/SnpEff/) |
| Salmon | Transcript quantification | [rəsmi](https://salmon.readthedocs.io/) |
| DESeq2 | Negative binomial differential expression | [rəsmi](https://bioconductor.org/packages/DESeq2/) |
| edgeR | Count GLM və dispersion | [rəsmi](https://bioconductor.org/packages/edgeR/) |
| limma | Linear models və voom | [rəsmi](https://bioconductor.org/packages/limma/) |
| Seurat | Single-cell analiz | [rəsmi](https://satijalab.org/seurat/) |
| Scanpy | Python single-cell analiz | [rəsmi](https://scanpy.readthedocs.io/) |
| PyMOL | Struktur vizuallaşdırması | [rəsmi](https://pymol.org/) |
| ChimeraX | Struktur analizi | [rəsmi](https://www.cgl.ucsf.edu/chimerax/) |
| AutoDock Vina | Molecular docking | [rəsmi](https://vina.scripps.edu/) |

## Seçim protokolu

Assay və bioloji suala görə alət seçin; ən məşhur alət avtomatik ən uyğun alət deyil. Kiçik validasiya dataset-i, versiya, input/output format, thread/RAM/disk ehtiyacı və benchmark meyarı yazılmalıdır. GATK/DeepVariant bütün assay-lərdə və ploidliklərdə eyni konfiqurasiya ilə istifadə olunmur. Annotasiya üçün referens və cache release uyğun olmalıdır.

Python baza: Biopython, NumPy, pandas, SciPy, matplotlib, scikit-learn, statsmodels. RNA inference: PyDESeq2. Əlavə: pysam, Scanpy, AnnData, NetworkX, Jupyter. R alətləri Linux/Conda workflow-lardan ayrıca idarə edilir.
