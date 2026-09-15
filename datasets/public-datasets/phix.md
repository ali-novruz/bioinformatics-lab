# PhiX174 referens genomu

**Source / version:** NCBI RefSeq NC_001422.1

**Dataset description:** Sequence operations üçün kiçik, real və versiyalanmış genom.

**Files:** NC_001422.1.fasta

**Columns/features və biological meaning:** FASTA: accession və 5,386 nt circular viral genome.

**License / access:** NCBI/INSDC istifadə siyasəti və accession submitter qeydləri qüvvədədir; xüsusi yeni lisenziya verilmir.

**Size / checksum (faktiki endirilən məzmun):** NC_001422.1.fasta: 5,520 bytes; SHA-256 `caa155c83967cc080f4f188f14f1f28c18d77448e87c3d00d3579ed348f4de2a`

## Download instructions
```bash
python scripts/fetch_data.py --dataset phix
```
Raw fayllar `datasets/raw/` daxilində saxlanır və Git-ə daxil edilmir. [Reference manifest](../reference-manifest.json) ilk doğrulanmış snapshot-u göstərir; local manifest hər run-da yoxlanır.

## Məhdudiyyətlər
Circular origin və overlapping genes motif/CDS şərhində nəzərə alınmalıdır.

Rəsmi mənbə: [PhiX174 referens genomu](https://www.ncbi.nlm.nih.gov/nuccore/NC_001422.1).
