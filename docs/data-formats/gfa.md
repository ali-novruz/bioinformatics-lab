# GFA assembly graphı

GFA segment (`S`), oriented link (`L`) və path (`P`) saxlayır:

```text
H VN:Z:1.0
S 1 ACGT
S 2 TTAA
L 1 + 2 + 2M
P contig1 1+,2+ 4M,2M
```

Sequence `*` olduqda ayrıca FASTA lazım ola bilər. Overlap CIGAR və orientation itirilərək sadə edge list-ə çevrilməməlidir. QC: link endpoint, path ardıcıllığı, reverse orientation, segment uzunluğu və assembly xülasəsi. [GFA specification](https://github.com/GFA-spec/GFA-spec).
