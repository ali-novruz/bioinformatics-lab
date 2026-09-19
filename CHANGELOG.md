# Dəyişikliklər

## Təqdimat və tanıtım paketi — 2026-09-19

README üçün AI üz qabığı, real nəticə qalereyası və qısa naviqasiya əlavə edildi.
26 slaydlıq PowerPoint təqdimatı native giriş animasiyaları və fade keçidləri,
redaktə edilən sxem, qrafik və cədvəllərlə hazırlandı. Statik PDF, 6 şəkilli
başlanğıc səhifəsi, danışıq qeydləri, 2 dəqiqəlik səssiz MP4 önizləmə, Azərbaycan
dilində subtitrlər və video çəkilişi təlimatı əlavə edildi.
[Tanıtım paketi](docs/media/README.md).

## Research audit — 2026-09-16

Custom RNA başlıqları və annotasiya ilə count merge düzəldildi. Registry, data
və research graph yoxlamaları; suite/run əlaqələri, command/runtime/status və
output checksum-ları əlavə edildi. 57 test, correctness lint, offline/integration
CI ayrımı və bütün notebook-ları işlədən giriş var. Khan nested CV/99 permutation
və GO exhaustive singleton control icra edildi; yeni nəticələr ayrıca saxlanır.
[Audit və məhdudiyyətlər](docs/RESEARCH_AUDIT.md).

## Stage 1 — Repository Architecture

README, məlumat siyasəti, töhfə qaydaları, modul struktur və mərhələ izləmə sistemi yaradıldı.

## Stage 2 — Fundamentals

16 bioloji anlayış, 11 format bələdçisi və 11 mövzu modulu yaradıldı; koordinat, statistik fərziyyə və research sualları əlavə edildi.

## Stage 3 — Research Resources

18 database kartı, alət/kitab/kurs xəritəsi və 10 mərhələli learning roadmap yaradıldı. API və istifadə şərtləri üçün rəsmi mənbələr bağlandı.

## Stage 4 — Research Papers

11 primary-source research note və təkrar istifadə edilən research/experiment şablonları yaradıldı. İki qeyd abstract/metadata səviyyəsindədir; tam mətn review-u kimi göstərilmir.

## Stage 5 — Projects

Beş modular Python layihəsi, CLI, deterministic testlər, 30 layihəlik kataloq, beş notebook, UniProt/PDB nümunəsi və raw sequencing workflow-ları quruldu. Python testləri keçdi; raw workflow-ların real icrası Linux mühitindən asılıdır.

## Stage 6 — Experiments

Altı real data mənbəyi üçün kartlar və hash manifest yaradıldı. Beş əsas layihə və əlavə protein analizi icra edildi; beş notebook başdan sona işlədildi. Machine-readable run snapshot-ları saxlanıldı. Test sayı 14-ə çatdı. Bash workflow-ları sintaksis yoxlamasından keçdi, real xam read icrası edilmədi.

## Stage 7 — Findings

Faktiki metriklərdən nəticə hesabatı, biological/statistical interpretation və məhdudiyyətlər yaradıldı. 12 qrafik vizual yoxlanıldı; real/sintetik statusları başlıqlarda yazıldı. Run manifest-lərinə source-file SHA-256 əlavə edildi və notebook-lar son kodla yenidən icra olundu.

## Stage 8 — New Research

9 mini literature review, 6 test edilə bilən research question və 10 advanced experiment protocol əlavə edildi. Hazır baseline-lar ilə gələcək iş arasındakı sərhəd STATUS-da qeyd olundu. Repository private GitHub layihəsi kimi hazırlandı; raw/large data Git-dən kənarda saxlanıldı.

## Stage 9 — End-to-end smoke

Kiçik paired FASTQ/reference/GTF fixture-ləri əlavə edildi. GitHub Actions Linux job-u BWA → SAMtools → BCFtools və STAR → featureCounts yollarını hər push-da real proqramlarla sınaqdan keçirir. Workflow-lara `SKIP_QC`, `SKIP_MULTIQC`, `THREADS` və kiçik genom üçün `STAR_SA_INDEX_NBASES` idarələri əlavə edildi.

## Stage 10 — Repository hygiene

CITATION.cff, issue şablonları və pull request checklist əlavə edildi. Üçüncü tərəf mənbələrinin istifadə şərtləri DATA_POLICY-də saxlanılır.

## Stage 11 — Verified Linux runs (2026-09-16)

İlk smoke fixture-dəki FASTQ keyfiyyət uzunluğu xətası və təkrarlanan reference
əvəz edildi. Deterministik positive control bir məlum PASS variant və 422
assigned fragment tələb edir; Linux-da keçdi. İki regression test əlavə edildi.

25 fayl immutable Git revision və SHA-256 ilə sabitləşdirildi. Altı real
GSE110004 RNA-seq sample-ında FASTQ-dan PyDESeq2 və üç qrafikə qədər yol
tamamlandı. Xarici nf-core/sarek DNA fixture-i 32 variant verdi (27 PASS).
FastQC statusları, input/source hashes, tool versiyaları və kiçik nəticələr
repoda saxlanıldı. 300,000 RNA read pair və 84 model gene analiz edildi.

Repo giriş bələdçisi, data kartları və nəticə keçidləri yeniləndi.
GitHub Actions komponentləri cari release commit-lərinə sabitləşdirildi.

## 2026-09-16 — UNEC praktikum və PDF kitabxanası

- 68 faylın inventarı, 61 unikal mənbə və 7 təkrar qeydi.
- 8 Azərbaycan dilli dərs, 15 həftəlik plan, 24 cavablı tapşırıq və mənbə düzəlişləri.
- Dörd orijinal kitab PDF-i, mənşə/lisenziya qeydləri və ayrıca praktikum PDF-i.
- Khan gen ifadəsi modeli, real RNA SQLite kataloqu və biostatistika simulyasiyası.
- Üç saxlanmış icra, altıncı icra edilmiş notebook və 6 yeni regression test.

## 2026-09-16 — Layihə auditi və genişləndirmə

- VCF-də duplicate sample, səhv FORMAT və artıq sample sahələri səssiz qəbul edilmir.
- SQLite NULL/boş sample kimliklərini və kəsr replicate nömrələrini rədd edir.
- Lokal cache və onun manifesti referens hash-i əvəz edə bilmir.
- Real GO-slim enrichment, bootstrap filogeniya və origin-aware ORF axtarışı əlavə edilib.
- 12 layihə üçün vahid başladıcı, bütün layihələrin icra logları, 7-ci notebook və 43 test.
- Tarixi mənbə arxivi köhnə nəticələri dəyişdirmədən cari kodun inkişafına imkan verir.
