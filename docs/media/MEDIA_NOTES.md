# Dizayn, mənbələr və yoxlama

## Vizual istiqamət

16:9 təqdimat tünd göy, yaşıl, nanə və açıq fon rənglərini birləşdirir. Proses sxemləri, zaman xətti, böyük göstəricilər, native cədvəllər və müxtəlif ölçüdə elmi şəkillər məzmunun növünə görə dəyişir. Arial istifadə olunur. Mətn və sxemlər şəkilə çevrilmədən PPTX obyektləri kimi saxlanır.

Üz qabığı built-in ImageGen ilə yaradılmış dekorativ illüstrasiyadır. [Tam prompt və mənbə qeydi](../../assets/readme/README.md). Bu şəkil elmi ölçmə və ya real laboratoriya fotoşəkli kimi təqdim edilmir.

Elmi qrafiklərin orijinalları dəyişdirilməyib. Təqdimat onları ölçüsünü uyğunlaşdıraraq yerləşdirir. Mənbələr hər slaydın danışıq qeydlərində və [mətn qeydlərində](PRESENTATION_NOTES.md) göstərilir. Offline/endirmə dairəvi qrafikinin qiymətləri [layihə qeydiyyatından](../../projects/registry.json) götürülüb və PPTX daxilində workbook ilə saxlanır.

## Animasiya

26 slaydda fade keçidi var. 234 obyekt üçün mərhələli giriş effekti əlavə edilib. Bir mərhələnin fade müddəti 550 ms, mərhələlər arasında gecikmə 260 ms-dir. Eyni mərhələyə aid mətn və forma birlikdə açılır. Növbəti slayda keçid kliklədir. Makro və xarici media bağlantısı tələb olunmur.

Native animasiya strukturunun istinadları:

- [Microsoft: Slide Timing](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.presentation.timing?view=openxml-3.0.1)
- [Microsoft: Shape Target və fade effekti](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.presentation.shapetarget?view=openxml-3.0.1)
- [Microsoft: Slide Transition](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.presentation.transition?view=openxml-3.0.1)

## Yoxlama əhatəsi

- PPTX paketinin strukturu, əlaqələri, slayd ölçüsü, font siyasəti və obyekt həndəsəsi yoxlanıb.
- 3 native cədvəl və 1 native qrafik, qrafikin workbook qiymətləri yoxlanıb.
- Animasiya hədəflərinin mövcud obyekt ID-lərinə işarə etməsi və timing ID-lərinin unikallığı yoxlanıb.
- Yekun PPTX yenidən import edilib, bütün 26 slayd render olunub və vizual baxışdan keçib.
- PDF-lərin 26 və 6 səhifə olması, şəkillər və video formatı yoxlanıb.

Bu yoxlamalar masaüstü PowerPoint-də canlı playback testi deyil. Animasiya məlumatı PPTX-də mövcuddur, faktiki playback həmin proqramda yoxlanmayıb. Fərqli viewer-lər animasiyanı eyni şəkildə göstərməyə bilər. PDF və PNG-lər bütün elementləri görünən statik nüsxələrdir.

## Fayl bütövlüyü

[Media manifesti](media-manifest.json) təqdimat, PDF, PNG, video və subtitr faylları üçün ölçü və SHA-256 saxlayır. Elmi nəticələr dəyişdirilməyib. Bu paket 19 sentyabr 2026-da hazırlanıb, elmi göstəricilər 16 sentyabr auditindən götürülüb.
