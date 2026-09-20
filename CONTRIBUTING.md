# Töhfə və tədqiqat qaydaları

Hər dəyişiklik bir bioloji sualı və ya bir reproduksiya problemini həll etsin. Yeni layihə üçün `research/templates/project.md`, yeni eksperiment üçün `research/templates/experiment.md` istifadə edin.

1. Sualı, data mənbəyini və qiymətləndirmə meyarını əvvəlcədən yazın.
2. Mənbədəki nəticəni öz nəticənizdən ayırın. Əldə edilməyən metriki boş və ya “icra edilməyib” saxlayın.
3. Yeni kodu `src/biolab/` daxilində modul kimi yazın. `notebooks/reproduce/` onu çağırıb audit izini saxlasın; `notebooks/learn/` eyni anlayışı kiçik ara addımlar və özünü-yoxlama sualları ilə öyrətsin.
4. Fayl formatını, koordinat konvensiyasını, random seed və paket versiyalarını saxlayın.
5. Kiçik deterministik test, real data smoke run və link yoxlamasını tamamlayın.
6. CHANGELOG və STATUS-u yeniləyin. Ayrı branch və təsviri commit istifadə edin.

Məqalə qeydi tam məqalənin surəti deyil. Öz sözlərinizlə metod, sübut və məhdudiyyətləri təhlil edin. İnsan genomik məlumatlarında donor məxfiliyini və dataset-in giriş şərtlərini qoruyun.
