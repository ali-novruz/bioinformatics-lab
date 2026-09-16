# Tarixi nəticələrin mənbə kodu

Əvvəlki nəticələr o vaxt işlədilmiş kodun SHA-256 izlərini saxlayır. Cari kodda səhv düzəldildikdə tarixi nəticənin kodunu cari versiya ilə eyniləşdirmək düzgün deyil.

`cbcbffb.zip` əvvəlki dəqiq Git revision-undakı Python mənbə fayllarını saxlayır. [Manifest](manifest.json) arxivin commit və hash-ini bağlayır. Yoxlayıcı əvvəl cari faylı, uyğun gəlməzsə hash-i təsdiqlənmiş arxivdəki eyni adlı faylı yoxlayır. Heç biri uyğun gəlmədikdə xəta verir. Arxiv kodu avtomatik işə salınmır.

Bu mexanizm tarixi nəticələri dəyişdirmədən layihəni inkişaf etdirməyə imkan verir. Yeni icralar cari kodun hash-lərini saxlayır. Arxiv yeni nəticələrin köhnə kodla işlədiyini iddia etmək üçün istifadə edilmir.
