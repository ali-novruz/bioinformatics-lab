# Repo auditi və layihələrin tamamlanması

Bu, əvvəlki 43-test/7-notebook mərhələsinin tarixli qeydidir. Cari tənqidi baxış,
elmi nəzarətlər və validation: [RESEARCH_AUDIT.md](RESEARCH_AUDIT.md).

Tarix: 2026-09-16. Audit kod girişlərini, data mənşəyini, layihə icrasını, sənəd keçidlərini və saxlanmış nəticələri əhatə edir.

## Tapılan və düzəldilən problemlər

| Problem | Əvvəlki davranış | Düzəliş və yoxlama |
|---|---|---|
| VCF duplicate sample adları | Dictionary-də əvvəlki nümunənin məlumatı itə bilərdi | Təkrar/boş sample adı rədd edilir |
| VCF FORMAT uyğunsuzluğu | `zip` artıq qiymətləri səssiz kəsə bilərdi | Artıq qiymət, təkrar açar, yanlış FORMAT header və GT sırası yoxlanır; icazəli trailing missing saxlanır |
| SQLite kimlikləri | SQLite text primary key NULL qəbul edə bilərdi; boş adlar məhdudlaşdırılmırdı | NOT NULL və nonempty qaydası sample/gene səviyyəsində əlavə edildi |
| Replicate tipi | Müsbət kəsr replicate qəbul edilə bilərdi | Integer tipinə database constraint qoyuldu |
| Cache etibarlılığı | Dəyişmiş lokal data ilə onun lokal manifesti bir-birinə uyğun ola bilərdi | Sabit referens manifesti ilə əlavə müqayisə edilir |
| Köhnə mənbə hash-ləri | Kod düzəlişi tarixi nəticə yoxlamasını poza bilərdi | Əvvəlki dəqiq mənbə arxivi və current/archived uyğunluğunun ayrı yoxlanması |
| Layihə başlanğıcı | Bir neçə ayrı skript və köhnə beş-layihə girişi vardı | 12 layihə üçün registry, vahid başladıcı, loglar və ümumi uğur/xəta statusu |
| Layihə sənədləri | Beginner/intermediate indeksləri çox ümumi idi | İşlək layihələrə konkret əmrlər, girişlər, çıxışlar və məhdudiyyətlər əlavə edildi |

## Əlavə edilmiş işlək layihələr

- [GO-slim enrichment](../projects/intermediate/go-enrichment/README.md): real RNA-seq nəticələri + SGD annotasiyaları, explicit measured universe, hypergeometric test və BH.
- [Filogeniya](../projects/intermediate/phylogeny/README.md): real Opuntia alignment-i, complete deletion, p-distance, neighbor joining və 200 bootstrap.
- [Dairəvi ORF axtarışı](../projects/beginner/orf-discovery/README.md): real PhiX174 genomu, iki strand, origin keçidi, koordinatlar və protein FASTA.

## Yoxlama əhatəsi

43 Python test; 12 layihənin tam icrası; 7 icra edilmiş notebook; lokal Markdown keçidləri; real input hash-ləri; kitab hash-ləri; köhnə/yeni nəticə snapshot-ları və mənbə mənşəyi. Yeni metodlarda müstəqil hesabla müqayisə və gözlənən cavabı məlum olan testlər var: Fisher exact uyğunluğu, məlum tree split və ORF koordinatından coding sequence-in bərpası.

GitHub CI Python 3.11-də bütün 8 offline layihəni, Python 3.12-də təmiz checkout-dan bütün 12 layihəni icra edir. Xam FASTQ smoke workflow ayrıca saxlanılır. [Cari CI](https://github.com/ali-novruz/bioinformatics-lab/actions/workflows/ci.yml). [Faktiki nəticə snapshot-u](../results/expanded-projects/README.md).

## Əhatə sərhədi

Bu audit işlək layihə paketinin keyfiyyətini artırır. [30 ideya](../projects/IDEAS.md) və advanced tədqiqat protokolları gələcək işlərdir; hamısının implementasiya olunduğu iddia edilmir. Tam genom miqyası, müstəqil klinik cohort, GWAS və AlphaFold təlimi bu yoxlamada icra edilməyib. Hər hazır layihədə nəticənin konkret bioloji və texniki sərhədi ayrıca yazılıb.
