# 12 işlək layihə

```bash
python scripts/lab.py list
python scripts/lab.py run all --offline
python scripts/lab.py run all
```

Əmrləri repo kökündə [quraşdırmadan](../SETUP.md) sonra işlədin. Offline rejim 8 layihəni işlədir və endirmə tələb edən 4 layihəni açıq skipped statusunda göstərir. Tam rejim bütün 12 layihəni işlədir; RNA-seq üçün research dependencies, ilkin data üçün internet lazımdır. Hər layihə və ümumi suite ayrıca nəticə qovluğu və log yaradır. Hər hansı layihə uğursuz olarsa ümumi əmrin çıxış kodu uğursuzdur.

| Kimlik | Layihə | Offline |
|---|---|---|
| dna | [DNA Sequence Analyzer](beginner/dna-analyzer/README.md) | Bəli |
| alignment | [Sequence Alignment](beginner/sequence-alignment/README.md) | Bəli |
| variants | [GIAB Variant Analysis](intermediate/variant-analysis/README.md) | Xeyr |
| rnaseq | [Pasilla RNA-seq](intermediate/rnaseq/README.md) | Xeyr |
| ml | [WDBC Disease Classification](intermediate/disease-classification/README.md) | Bəli |
| proteins | [Protein Sequence and Structure](intermediate/protein-analysis/README.md) | Xeyr |
| expression-ml | [Khan Gene Expression](intermediate/gene-expression-ml/README.md) | Xeyr |
| database | [RNA SQLite Catalog](beginner/study-database/README.md) | Bəli |
| statistics | [Biostatistics Lab](beginner/biostatistics-lab/README.md) | Bəli |
| enrichment | [Real GO-slim Enrichment](intermediate/go-enrichment/README.md) | Bəli |
| phylogeny | [Opuntia Phylogeny](intermediate/phylogeny/README.md) | Bəli |
| orfs | [Circular Genome ORF Discovery](beginner/orf-discovery/README.md) | Bəli |

Məsələn: `python scripts/lab.py run phylogeny --offline`. [İcra hesabatı və yeni nəticələr](../results/expanded-projects/README.md). [Maşınla oxunan registry](registry.json) bu siyahının əmrlərini saxlayır.

Tam rejimdə DNA analyzer üçün real PhiX FASTA endirilir və yoxlanır. Offline rejimdə lokal PhiX varsa o, yoxsa açıq göstərilmiş sintetik fixture istifadə olunur. ORF layihəsi həmişə repoya daxil edilmiş real PhiX genomunu işlədir.

## Daha böyük eksperimentlər

[Xam FASTQ workflow-ları](../workflows/README.md) əlavə Linux alətləri tələb edir və ayrıca CI-də yoxlanır. [30 ideya və protokol](IDEAS.md) gələcək eksperiment kataloqudur; hamısı işlək tətbiq kimi işarələnməyib. Hazır layihələrin dəqiq siyahısı yuxarıdadır.
