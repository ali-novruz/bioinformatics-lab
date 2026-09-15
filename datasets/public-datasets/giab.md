# GIAB HG001 benchmark prefix

**Source / version:** NIST GIAB HG001 GRCh38 v4.2.1

**Dataset description:** Məlum benchmark variantlarını format və keyfiyyət analizi üçün istifadə edir.

**Files:** giab_hg001_first1000.vcf

**Columns/features və biological meaning:** VCF header + ilk 1,000 record; 1,003 ALT allele. CHROM/POS/REF/ALT/QUAL/FILTER/INFO/FORMAT və HG001 sample.

**License / access:** NIST/GIAB release istifadəsi və citation qaydalarını source README-dən yoxlayın; burada tam dataset yenidən yayılmır.

**Size / checksum (faktiki endirilən məzmun):** giab_hg001_first1000.vcf: 547,467 bytes; SHA-256 `d40781c1f8502777cb111a11cf0d8e0670fe8066e6d0f6c967aa6a1d20a5162a`

## Download instructions
```bash
python scripts/fetch_data.py --dataset giab
```
Raw fayllar `datasets/raw/` daxilində saxlanır və Git-ə daxil edilmir. [Reference manifest](../reference-manifest.json) ilk doğrulanmış snapshot-u göstərir; local manifest hər run-da yoxlanır.

## Məhdudiyyətlər
Tam compressed source təxminən 120 MB-dir; yalnız stream-in prefix-i saxlanır. Bu alt-dəst random deyil və caller precision/recall üçün təkbaşına kifayət etmir. Benchmark region BED ayrıca lazımdır.

Rəsmi mənbə: [GIAB HG001 benchmark prefix](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/NA12878_HG001/NISTv4.2.1/GRCh38/).
