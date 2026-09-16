# Yeni layihələr üçün kiçik real girişlər

Bu üç giriş offline icra üçün repoda saxlanılır. [Manifest](manifest.json) mənbə URL-i, orijinal mənbə hash-i, saxlanmış fayl hash-i, ölçü və çevirməni göstərir. Hash uyğunluğu elmi doğruluq yoxlamasını əvəz etmir.

## Opuntia alignment

[Biopython təlimatı](https://biopython.org/docs/latest/Tutorial/chapter_msa.html) yeddi prickly-pear, Opuntia DNA ardıcıllığının alignment nümunəsini təqdim edir. Fayl [5bbc6c1 revision-undakı test dəstindən](https://github.com/biopython/biopython/blob/5bbc6c12c505301f2d681f932c30fdb8fcbe9a6e/Tests/Clustalw/opuntia.aln) alınıb. 7 ardıcıllıq, 156 alignment sütunu. Sətir sonları LF edilib; sequence-lər dəyişdirilməyib. Accession-lar AF191658.1-AF191661.1 və AF191663.1-AF191665.1-dir. Bu qısa tutorial fraqmentləri tam genom və ya tam növ nümunələməsi deyil.

Müəlliflik: Biopython contributors; ilkin ardıcıllıq müəllifliyi GenBank qeydlərinə aiddir. [Biopython lisenziyası](phylogeny/LICENSE.biopython) saxlanılır.

## SGD GO-slim annotasiyaları

[Saccharomyces Genome Database](https://www.yeastgenome.org/) tərəfindən yayımlanan [GO-slim mapping](https://downloads.yeastgenome.org/curation/literature/go_slim_mapping.tab) faylı 2026-09-16 tarixində alınıb. Orijinal 4,197,139 baytlıq faylın hash-i manifestdə saxlanır.

Çevirmə: RNA count matrisindəki 124 genin sistematik kimliklərinə uyğun sətirlər; yalnız biological process aspekti; ümumi GO:0008150 root-u çıxarılıb; beş sütun seçilib; təkrar gen-term sətirləri çıxarılıb; GO/gene üzrə sıralanıb. Nəticədə 293 sətir, 69 annotasiyalı gen və 91 GO-slim term qalır. Statistik analizdə finite-padj universe-i ilə kəsişmə və term ölçüsü filtri ayrıca tətbiq olunur.

SGD-yə və GO annotasiya müəlliflərinə istinad saxlanılır; SGD səhifələri CC BY 4.0 lisenziyasına keçid verir. Bu çıxarış ayrıca kurasiya edilmiş yeni bioloji annotasiya kimi təqdim edilmir. Tarix və çevirmə qeydinin saxlanması sonrakı annotasiya dəyişikliklərini aşkar etməyə imkan verir.

## PhiX174

NC_001422.1 referens FASTA-sı əvvəlki yoxlanmış NCBI girişinin dəyişdirilməmiş nüsxəsidir. 5386 nukleotid, dairəvi genom analizi. [Əvvəlki mənşə manifesti](../reference-manifest.json) və [NCBI mənbə qeydi](https://www.ncbi.nlm.nih.gov/nuccore/NC_001422.1). ORF namizədləri bu ardıcıllıqdan alqoritmlə hesablanır, təsdiqlənmiş CDS siyahısından köçürülmür.
