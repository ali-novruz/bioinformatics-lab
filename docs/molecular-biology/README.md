# Molekulyar biologiya

## DNA

**Nədir?** Dezoksiribonuklein turşusu A, C, G, T nukleotidlərindən qurulan, irsi informasiyanı daşıyan polimerdir. İki zəncir antiparaleldir: biri 5′→3′, digəri 3′→5′.

**Bioloji rol:** Genetik məlumatın saxlanılması və replikasiya üçün şablon.

**Bioinformatik istifadə:** Oxunuşların referensa hizalanması, motif axtarışı və variant analizi.

**Real nümunə:** İnsan HBB genində kodlaşdırıcı dəyişiklik hemoqlobinin amin turşusunu dəyişə bilər; təsiri transkript və alleldən asılıdır.

**Data formatları:** FASTA: referens; FASTQ: cihaz oxunuşu; BAM: hizalanma; VCF: referensə nisbətən dəyişiklik.

## RNA

**Nədir?** Ribonuklein turşusu adətən təkzəncirlidir, T əvəzinə U daşıyır. mRNA, rRNA, tRNA və tənzimləyici RNA-ların rolları fərqlidir.

**Bioloji rol:** İnformasiyanın ötürülməsi, tərcümə, kataliz və gen tənzimlənməsi.

**Bioinformatik istifadə:** RNA-seq ilə transkript bolluğu və splicing analizi.

**Real nümunə:** Pasilla knockdown RNA bağlayan proteinin azalmasının Drosophila transkriptomuna təsirini araşdırır.

**Data formatları:** FASTQ, BAM, GTF, gene-by-sample count TSV. RNA-seq FASTQ-larında çox vaxt cDNA səbəbilə T yazılır.

## Protein

**Nədir?** Amin turşularından yaranan polipeptid; ardıcıllıq, struktur və mühit birlikdə funksiyaya təsir edir.

**Bioloji rol:** Ferment, reseptor, struktur komponent və siqnal ötürücüsü.

**Bioinformatik istifadə:** Homologiya, domain annotasiyası və struktur müqayisəsi.

**Real nümunə:** İnsulin əvvəl preproinsulin kimi sintez olunur; yetkin zəncirlərin annotasiyası tam prekursorla eyni deyil.

**Data formatları:** Protein FASTA, UniProt JSON/TSV, PDB/mmCIF, mzML.

## Gene

**Nədir?** Funksional RNA və ya protein məhsuluna töhfə verən genomik region. Bir gen birdən çox transkript yarada bilər.

**Bioloji rol:** İfadə edilən məhsulun genetik vahidi.

**Bioinformatik istifadə:** Reads-in genlərə sayılması və variantların genlə əlaqələndirilməsi.

**Real nümunə:** HBB və onun konkret transkriptinin koordinatları eyni anlayış deyil.

**Data formatları:** GFF3/GTF, BED və FASTA; gene ID ilə gene symbol fərqləndirilməlidir.

## Genome

**Nədir?** Orqanizmin və ya hüceyrənin genetik materialının bütöv toplusu; nüvə və orqanel genomları nəzərə alınmalıdır.

**Bioloji rol:** İrsi informasiyanın sistem səviyyəsində təşkili.

**Bioinformatik istifadə:** Assembly, müqayisəli genomika və pangenome analizləri.

**Real nümunə:** E. coli K-12 MG1655 referensi NC_000913.3 bir ştamı təsvir edir, bütün E. coli növünü deyil.

**Data formatları:** FASTA, assembly report, GFF3, indeks faylları.

## Chromosome

**Nədir?** DNA və əlaqəli proteinlərdən təşkil olunan genom vahidi.

**Bioloji rol:** DNA-nın paketlənməsi və bölünmə zamanı paylanması.

**Bioinformatik istifadə:** Koordinat sistemi, copy-number və struktur variant təhlili.

**Real nümunə:** chr1 və 1 eyni referensdə fərqli adlandırma konvensiyaları ola bilər.

**Data formatları:** FASTA contig adları, BAM @SQ, VCF CHROM, BED.

## Mutation

**Nədir?** Nukleotid ardıcıllığında yaranan dəyişiklik; somatik və ya irsi ola bilər. Variant müşahidə edilən allel fərqini daha neytral təsvir edir.

**Bioloji rol:** Təkamül, müxtəliflik və bəzi funksional dəyişikliklərin mənbəyi.

**Bioinformatik istifadə:** SNP/indel/SV aşkarlanması və funksional prioritetləşdirmə.

**Real nümunə:** Bir şişdə somatik variantı germline variantdan ayırmaq üçün uyğun normal nümunə faydalıdır.

**Data formatları:** VCF/BCF, MAF, BEDPE. Referens build həmişə yazılmalıdır.

## SNP

**Nədir?** Tək nukleotid polimorfizmi; SNV istənilən tək nukleotid variantını bildirir, SNP isə populyasiya kontekstində işlənir.

**Bioloji rol:** Genetik müxtəlifliyin geniş yayılmış növü.

**Bioinformatik istifadə:** Genotipləmə, GWAS və populyasiya strukturu.

**Real nümunə:** dbSNP rs identifikatoru patogenlik sübutu deyil.

**Data formatları:** VCF, PLINK BED/BIM/FAM və PGEN.

## Genotype

**Nədir?** Müəyyən lokusda nümunənin allel tərkibi; ploidlikdən asılıdır.

**Bioloji rol:** İrsi allellərin konkret kombinasiyasını təsvir edir.

**Bioinformatik istifadə:** Assosiasiya, segregasiya, allel tezliyi və keyfiyyət analizi.

**Real nümunə:** VCF-də 0/1 referens və birinci ALT allelini, 1|0 isə fazası məlum sıranı bildirir.

**Data formatları:** VCF FORMAT/GT, PLINK, BGEN. ./. itkin genotipdir, 0/0 deyil.

## Phenotype

**Nədir?** Ölçülən və ya müşahidə olunan xüsusiyyət; genotip, mühit və ölçmə prosesi ilə bağlıdır.

**Bioloji rol:** Orqanizmin xüsusiyyətlərinin müşahidə edilən ifadəsi.

**Bioinformatik istifadə:** GWAS outcome, ML label və klinik fenotip uyğunlaşdırması.

**Real nümunə:** Şiş diaqnozu ilə mikroskopik nüvə forması arasındakı əlaqə WDBC-də öyrənilə bilər.

**Data formatları:** CSV/TSV metadata, HPO terminləri; vahid və ölçmə vaxtı vacibdir.

## Central Dogma

**Nədir?** Ardıcıllıq informasiyasının DNA-dan RNA-ya və RNA-dan proteinə ötürülməsi üçün əsas çərçivədir; reverse transcription RNA→DNA mümkündür.

**Bioloji rol:** Gen ifadəsinin molekulyar əsasını əlaqələndirir.

**Bioinformatik istifadə:** Genom, transkriptom və proteomu eyni gene/transcript identifikatorları ilə bağlamaq.

**Real nümunə:** Retroviruslarda RNA-dan DNA sintezi bu sadə ox sxeminin bütün biologiya olmadığını göstərir.

**Data formatları:** FASTA + GTF + protein FASTA + count/protein abundance matrices.

## DNA replication

**Nədir?** DNA polimerazalar yeni zənciri 5′→3′ istiqamətində şablona komplementar sintez edir.

**Bioloji rol:** Hüceyrə bölünməsindən əvvəl genomun surətlənməsi.

**Bioinformatik istifadə:** Replikasiya mənşəyi, strand bias və mutasiya mexanizmlərinin tədqiqi.

**Real nümunə:** Bakterial genomda GC skew replikasiya konteksti ilə əlaqəli ola bilər; təkbaşına origin sübutu deyil.

**Data formatları:** FASTA, coverage bigWig/BAM, BED regionları.

## Transcription

**Nədir?** RNA polimeraza DNA şablonundan RNA sintez edir; eukariotlarda transkript emalı və splicing də vacibdir.

**Bioloji rol:** Genetik informasiyanı RNA məhsullarına çevirir.

**Bioinformatik istifadə:** Splice-aware mapping, promotor və transkript annotasiyası.

**Real nümunə:** Eyni gendə alternativ exon kombinasiyaları fərqli izoformlar yarada bilər.

**Data formatları:** FASTQ, spliced BAM CIGAR N, GTF exon/transcript.

## Translation

**Nədir?** Ribosom mRNA kodonlarını genetik koda görə amin turşularına çevirir.

**Bioloji rol:** Protein sintezi.

**Bioinformatik istifadə:** ORF tapılması, kodon istifadəsi və nonsynonymous variant annotasiyası.

**Real nümunə:** ATG DNA kodonu standart kodda metioninə uyğun gəlir; mitoxondrial kod ayrıca seçilməlidir.

**Data formatları:** CDS FASTA, protein FASTA, GFF3 phase. Frame və strand bilinmədən translation edilmir.

## Gene expression

**Nədir?** Gen məhsulunun müəyyən hüceyrə, toxuma və zamanda yaranması/bolluğu. RNA bolluğu protein aktivliyinin birbaşa ölçüsü deyil.

**Bioloji rol:** Hüceyrə vəziyyətini və mühitə cavabı dəyişir.

**Bioinformatik istifadə:** Count model, normalization və differential expression.

**Real nümunə:** Müalicə və kontrol arasında sayım fərqi library size ilə də yarana bilər.

**Data formatları:** Raw integer counts TSV, metadata CSV, AnnData/H5AD. TPM ilə raw counts eyni deyil.

## Epigenetics

**Nədir?** DNA ardıcıllığını dəyişmədən gen fəaliyyətinə bağlı xromatin və tənzimləyici vəziyyətlər; irsilik və səbəbiyyət kontekstdən asılıdır.

**Bioloji rol:** Hüceyrə identikliyi və genlərin əlçatanlığının tənzimlənməsi.

**Bioinformatik istifadə:** DNA methylation, ATAC-seq və histon işarələrinin analizi.

**Real nümunə:** Promotor methylation ilə RNA ifadəsi arasındakı korrelyasiya səbəbiyyəti təkbaşına göstərmir.

**Data formatları:** BED, bigWig, methylation beta-value matrix, BAM.

## Kiçik laboratoriya

`ATGGCTTAA` üçün komplement, reverse complement, RNA və standart kodla translation hesablayın. Komplement `TACCGAATT`, reverse complement `TTAAGCCAT`, RNA `AUGGCUUAA`, protein `MA*` olmalıdır. Bütün genomun ilk bazadan tərcüməsi bioloji protein annotasiyası deyil.

## Araşdırma dövrəsi

Problem: eyni DNA fərqli hüceyrə vəziyyətlərində fərqli ifadə yaradır. Metod: RNA-seq və epigenom ölçmələrini birləşdirmək. Zəiflik: cell composition və batch qarışdırıcıdır. Data: GEO/GTEx açıq xülasələr. Eksperiment: donor/tissue kovariatları ilə assosiasiya; müstəqil kohortda təkrar. Yeni sual: ifadə dəyişməsi hüceyrə sayından asılıdırmı?

Mənbələr: [NCBI Bookshelf — Molecular Biology of the Cell](https://www.ncbi.nlm.nih.gov/books/NBK21054/), [DNA replication](https://www.ncbi.nlm.nih.gov/books/NBK26821/), [pasilla data](https://bioconductor.org/packages/release/data/experiment/html/pasilla.html). HBB nümunəsi konkret klinik variant təsnifatı deyil.
