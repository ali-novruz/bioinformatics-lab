# Repository üçün video hazırlama bələdçisi

## Hazır paket

- [İki dəqiqəlik MP4 önizləmə](repo-intro-preview.mp4): 12 səhnə, səssiz montaj, yumşaq keçidlər.
- [Azərbaycan dilində SRT subtitrləri](intro-az.srt): 24 hissə, 120 saniyə. MP4 daxilində də seçilə bilən subtitr track-i var.
- [Vaxt bölgüsü və səsləndirmə mətni](video-storyboard.json): hər səhnənin başlanğıcı, sonu, slayd nömrəsi və oxunacaq mətn.
- [Animasiya əlavə edilmiş PowerPoint](bioinformatics-lab-animated.pptx): tam 26 slayd və danışıq qeydləri.

MP4 slaydlar əsasında hazırlanmış **səssiz tanıtım maketidir**. Real ekran yazısı və səsləndirmə daxil deyil. PowerPoint-dəki obyekt animasiyaları MP4-də təkrar edilməyib, video ayrıca yumşaq görüntü keçidlərindən istifadə edir.

## İki dəqiqəlik tanıtımın səhnələri

| Vaxt | Slayd | Görüntü | Danışığın mövzusu |
|---|---:|---|---|
| 00:00-00:10 | 1 | DNA üz qabığı | Azərbaycan dilində bioinformatika laboratoriyası |
| 00:10-00:20 | 2 | Sualdan nəzarətə proses sxemi | Öyrənmə və yoxlama iş axını |
| 00:20-00:30 | 3 | Saylar və layihə qrafiki | 13 layihə, 16 notebook, 9 offline layihə |
| 00:30-00:40 | 4 | Layihə kataloqu | DNA, alignment, genom və protein istiqamətləri |
| 00:40-00:50 | 6 | Pasilla PCA | Real RNA-seq analizi və model dizaynı |
| 00:50-01:00 | 9 | Permutation nəzarəti | Nəticənin təsadüfdən fərqlənməsi |
| 01:00-01:10 | 11 | Opuntia ağacı | Qısa fraqmentlərin filogeniyası |
| 01:10-01:20 | 16 | UNEC materiallarının dərsə çevrilməsi | Dərslər, tapşırıqlar, PDF praktikum |
| 01:20-01:30 | 15 | Mənşə və icra sxemi | Parametrlər, hash və təkrar icra |
| 01:30-01:40 | 19 | Elmi iddianın sərhədi | Klinik validasiya ilə benchmark fərqi |
| 01:40-01:50 | 23 | İlk offline əmri | Alignment nümunəsini işlətmək |
| 01:50-02:00 | 26 | Başlanğıc və töhfə yolları | Bir layihədən öz tədqiqat sualına |

Səsləndirmənin tam mətni `video-storyboard.json` faylındakı `narration` sahələrindədir. SRT eyni mətnin beş saniyəlik bölmələrini saxlayır. Səsi yazdıqdan sonra subtitr vaxtlarını real danışığa uyğunlaşdırın.

## Beş dəqiqəlik real ekran təlimatı

Bu ikinci format tanıtımı praktiki nümayişə çevirir. Təxmini montaj vaxtlarıdır, icranın sürətinə zəmanət deyil.

| Vaxt | Çəkiləcək əməliyyat | İzah |
|---|---|---|
| 00:00-00:35 | README və `docs/START_HERE.md` açılır | Repo kim üçündür, ilk yol hansıdır? |
| 00:35-01:15 | `SETUP.md`, repo kökü və virtual mühit | Python 3.12, aktivləşdirmə və paketlər |
| 01:15-01:40 | `python scripts/lab.py list` | Offline və download işarələri |
| 01:40-02:30 | `python scripts/lab.py run alignment --offline` | Real icra, gözləmə və status |
| 02:30-03:25 | Yeni suite qovluğunda `suite.json`, log və `run_paths` | Nəticəni tapmaq və düzgün oxumaq |
| 03:25-04:05 | Saxlanmış RNA-seq və nəzarət qrafikləri | Əvvəlki icra nəticəsi olduğunu bildirmək |
| 04:05-04:35 | UNEC dərsləri və PDF kitabxanası | Praktiki tapşırıq və oxu yolu |
| 04:35-05:00 | `CONTRIBUTING.md` və bir yeni sual | İstifadəçinin növbəti addımı |

Quraşdırma və icra gözləmələrini montajda qısaldanda ekranda “gözləmə hissəsi qısaldılıb” qeydini verin. Nəticəni yaratmadan uğurlu terminal çıxışı göstərməyin. Təlimat şəkilləri ekran yazısı deyil, redaktə edilən slaydlardan hazırlanmış izah səhifələridir.

## Görüntü və səs istiqaməti

- Əsas format: 16:9. Önizləmə 1280×720, təqdimat və bələdçi PNG-ləri 1920×1080-dır.
- Rənglər: tünd göy `#092333`, yaşıl `#087F83`, açıq nanə `#79DEC5`.
- Ekran yazısında mətnləri rahat oxunacaq ölçüyə böyüdün. Qrafikin oxlarını və izahını kəsməyin.
- Səhnə keçidləri sakit olsun. Elmi qrafikin rəqəmlərini animasiya ilə dəyişməyin.
- Azərbaycan dilində təbii, aydın danışıq istifadə edin. Fon musiqisi varsa, səsin altında zəif saxlayın və istifadə icazəsini yoxlayın.
- GitHub ekranında token, şəxsi bildiriş və başqa layihələrin məlumatını göstərməyin. Repo private olduğuna görə tamaşaçıya giriş şərtini izah edin.

## Hazır paylaşım mətni

**Başlıq:** Bioinformatics Research Lab: layihələr, real analiz və elmi nəzarətlər

**Təsvir:** Azərbaycan dilində bioinformatika laboratoriyası ilə tanış olun. Repository 13 işlək layihəni, 16 notebook-u, PDF kitabxanasını və UNEC praktikumunu birləşdirir. Videoda RNA-seq, filogeniya, model nəzarəti və ilk offline icra yolunu göstəririk. Nəticələr tədris və tədqiqat nümunələridir. Tam materiallar və məhdudiyyətlər repository-dədir.

[Repository](https://github.com/ali-novruz/bioinformatics-lab) giriş icazəsi olan hesabla açılır.

## Yayımdan əvvəl son yoxlama

Göstərilən sayları cari `STATUS.md` ilə tutuşdurun. `0.99` Khan training auditi, `19/20` isə tarixi ayrılmış test nəticəsidir. Bu rəqəmləri bir-birinin yerinə işlətməyin. ORF-ləri təsdiqlənmiş gen, variant saylarını dəqiqlik benchmark-ı və AI üz qabığını elmi ölçmə kimi təqdim etməyin.
