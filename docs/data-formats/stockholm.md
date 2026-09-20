# Stockholm

Stockholm çoxlu alignment ilə file, sequence, residue və column annotasiyasını saxlayır.

```text
# STOCKHOLM 1.0
seqA AC-GU
seqB ACGGU
#=GC SS_cons ..((.
#=GF ID toy_family
//
```

`#=GF`, `#=GS`, `#=GR`, `#=GC` fərqli annotasiya səviyyələridir. Interleaved bloklar birləşdirilir. QC: bütün sequence-lərin yekun uzunluğu, unikal ID, annotasiya uzunluğu və `//` terminatoru. [Pfam Stockholm](https://pfam-docs.readthedocs.io/en/latest/stockholm.html).
