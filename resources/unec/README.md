# UNEC mənbə kataloqu

İstifadəçi tərəfindən təqdim olunmuş **68 fayl** inventarlaşdırılıb: **61 bayt baxımından unikal fayl**, **7 tam təkrar**. [CSV](catalog.csv) rahat süzgəc, [JSON](catalog.json) isə proqramla istifadə üçündür. Hər qeyd orijinal adı, SHA-256, ölçünü, mövzunu, baxış səviyyəsini və dərsdə istifadəsini göstərir.

## Seçim və baxış qaydası

DOCX/PPTX fayllarından yerli XML mətnləri, PDF-lərdən pypdf ilə mətn çıxarılıb. Seçilmiş abzas və slaydlar oxunaraq yeni konspektlərə çevrilib. Kitabların bütün səhifələrinin oxunduğu iddia edilmir. Şəkil ağırlıqlı təqdimatlarda yalnız başlıq/mətn üzrə ilkin təsnifat aparılıb; şəkillər tam yoxlanmayıb. Sənədlərdəki göstərişlər istifadəçinin yeni tapşırığı kimi qəbul edilməyib.

Abzas və slayd nömrələri yerli çıxarışdakı ardıcıllıqdır; PDF səhifəsi fiziki səhifə sayıdır, çap olunmuş nömrədən fərqlənə bilər. U4072 kimi qısa kimlik fayl adının son dörd rəqəmidir. Kataloqdakı `handbook_sections` [praktikumdakı](../../docs/unec/handbook.md) bölmələri göstərir.

Əsas mövzular: məlumat, database, data mining, ML, genetika, irsiyyət, sequence bazaları və biostatistika. Bəzi materiallarda müəllim kimi **Sevinc Kərimova**, UNEC-in **Rəqəmsal texnologiyalar və tətbiqi informatika** bölməsi göstərilir. Kitabların ayrıca müəllifliyi aşağıda saxlanılır. Yeni konspektlər və kodlar həmin müəllim və ya universitetin rəsmi işi kimi təqdim edilmir.

## Vacib fərqlər

- U4129-un mövzu nömrəsi aldadıcıdır: məzmun database suallarıdır, genetika dərsi deyil.
- U4230 və U4231 eyni çıxarılmış mətnə malikdir, lakin fayl hash-ləri fərqlidir. Onlar bayt-identik təkrar kimi sayılmayıb.
- U4247 miRNA və tədqiqat xülasələridir; cihaz baxımı mövzusu deyil.
- U4240/U4242 cihaz baxımı əsas hesablama proqramına daxil edilməyib.
- U4209/U4211/U4216/U4218 tarixi şirkət/mərkəz siyahıları cari xidmət kataloqu kimi istifadə edilməyib.
- U4253-ün COVID/vaksin iddiaları ayrıca ilkin mənbə yoxlaması tələb etdiyi üçün yeni elmi nəticələrə çevrilməyib.

## Saxlanmış fayllar

| PDF | Mənşə | Status |
|---|---|---|
| [Statistika, 2015](pdf/statistika-az-2015.pdf) | U4230; F. N. Əliyev, C. İ. Mikayilov, Y. N. Əliyev | İstifadəçinin təqdim etdiyi dəyişdirilməmiş nüsxə |
| [Data Science and Machine Learning](pdf/data-science-machine-learning-2022.pdf) | U4117; Kroese, Botev, Taimre, Vaisman; 8 may 2022 əlyazması | İstifadəçinin təqdim etdiyi dəyişdirilməmiş nüsxə |
| [Bioinformatika praktikumu](bioinformatika-praktikum.pdf) | Bu repo üçün hazırlanmış Azərbaycan dilli tədris bələdçisi | 8 dərs, proqram, 24 tapşırıq və cavablar |

İlk iki kitab üçün açıq yenidən yayım lisenziyası müəyyən edilməyib. Onlar istifadəçinin istəyi ilə şəxsi **private** repoya əlavə olunub; ümumi repo lisenziyası kimi qəbul edilmir. Açıq yayım planlanarsa bu nüsxələrin hüquqları ayrıca yoxlanmalıdır. [Kitab manifesti](../books/pdf-manifest.json) dəyişdirilməmiş mənbə nüsxələrinin hash-lərini saxlayır.

Qalan 66 orijinal faylın hamısını repoya kopyalamaq əvəzinə mənbə kataloqu, seçilmiş konspektlər və mənbəyə bağlı tapşırıqlar əlavə edilib. Onların orijinal nüsxələri istifadəçinin təqdim etdiyi Downloads qovluğundadır.
