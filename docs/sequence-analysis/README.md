# Sequence analysis və alqoritmlər

### Nəzəri baza
DNA/RNA əlifbasında ambiguous IUPAC simvollarını ayırın. Protein similarity substitution matrix ilə qiymətləndirilə bilər; identity hizalanmış eyni simvolların payıdır. Məxrəc aligned columns, non-gap columns və ya query length ola bilər: nəticədə hansını istifadə etdiyinizi yazın. Conserved region evolution və selection ilə uyğun gələ bilər, funksiyanı təkbaşına sübut etmir.

### Needleman–Wunsch — global alignment
D[i,j]=max(D[i-1,j-1]+s(aᵢ,bⱼ), D[i-1,j]+g, D[i,j-1]+g). Sərhədlər D[i,0]=i*g və D[0,j]=j*g. Traceback sağ-alt küncdən başlayır. Bütün iki sequence hizalanır. Vaxt və yaddaş O(mn); bu implementasiya teaching üçündür, insan genomu üçün deyil.

### Smith–Waterman — local alignment
Eyni recurrence-a 0 əlavə edilir; sərhədlər 0-dır. Traceback maksimum hüceyrədən 0-a qədərdir. Ortadakı yaxşı segment tapılır. Tie-breaking deterministikdir, optimal alignment yeganə olmaya bilər. `src/biolab/sequence.py` hər iki metodu özümüz implementasiya edir; test Biopython score-u ilə müqayisə edir.

### Multiple sequence alignment
Tam çoxardıcıllıqlı dynamic programming ölçülə bilməz dərəcədə böyüyür. Progressive alignment pairwise distances → guide tree → profile alignment yolu ilə yaxınlaşma edir; erkən səhvlər qala bilər. MAFFT və MUSCLE real MSA üçündür. Əvvəl qısa sequence cütlərini öz DP ilə yoxlayın, sonra `mafft input.fa > aligned.fa` və column conservation hesablayın. Bu repo production MSA-nı sıfırdan yenidən yazmır.

### BLAST
BLAST seed→extend heuristic-dir; bütün mümkün alignment-ləri yoxlamır. E-value database ölçüsü və score statistikasından asılıdır; percent identity E-value deyil. `seed_search` eyni k-mer seed-ləri sayan tədris nümunəsidir, BLAST əvəzi və ya E-value hesablayıcısı deyil. Müqayisə: `makeblastdb -in db.fa -dbtype nucl`, sonra `blastn -query q.fa -db db.fa -outfmt 6`.

### Motif discovery
Known motif üçün regex/IUPAC scan; de novo üçün foreground/background k-mer enrichment və PWM/EM yanaşmaları mümkündür. Sliding pəncərələr müstəqil deyil; GC-matched background seçin. K-mer enrichment implementasiyasında pseudocount sıfır tezlikləri sabitləşdirir. Overlapping motif-lər qaçırılmamalıdır.

### RNA və protein
RNA strukturunda complementary pairing əlavə məhdudiyyət verir. Protein üçün BLOSUM62 və affine gap daha uyğun ola bilər; DNA scoring-ni protein üçün avtomatik seçməyin. Əvvəl linear gap implementasiyasını anlayın, sonra Biopython ilə gap-open/gap-extend sınağı aparın.

### Araşdırma
Problem: qısa oxşarlıq təsadüfi ola bilər. Data: UniProt və shuffled controls. Eksperiment: gap penalty, GC və sequence length üzrə score paylanması. Yeni sual: eyni identity fərqli coverage-də nə qədər etibarlıdır?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://biopython.org/docs/latest/Tutorial/chapter_pairwise.html). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
