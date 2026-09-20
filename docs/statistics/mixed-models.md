# Qarışıq effektli modellər

Repeated measures, donor daxilində hüceyrələr və çoxmərkəzli tədqiqatlarda müşahidələr müstəqil deyil. Mixed model sabit effektləri ümumi əlaqə, təsadüfi effektləri isə qrup səviyyəli dəyişkənlik kimi ayırır.

## Nümunə dizayn

`expression ~ treatment + time + treatment:time + (1 | donor)` donor üçün random intercept verir. Donorların zaman trendi də fərqlənirsə `(time | donor)` random slope düşünülə bilər. Random-effect strukturu dizaynla əsaslandırılmalıdır; yalnız AIC azaldığı üçün sonsuz mürəkkəblik seçilməməlidir.

## Bioinformatik tətbiqlər

- donor daxilində çox hüceyrə;
- eyni fərddən təkrar zaman nöqtələri;
- plate, batch və mərkəz üzrə qruplaşma;
- növ daxilində populyasiya və ailə strukturu.

Single-cell data-da hüceyrələri müstəqil bioloji replikat saymaq pseudoreplication yaradır. Donor səviyyəli pseudobulk və ya uyğun hierarchical model daha düzgün vahid seçə bilər.

## Yoxlama

Residual qrafikləri, singular fit, random-effect variasiyası, təsirli qruplar və model müqayisəsini göstərin. Qrup sayı çox azdırsa random-effect variasiyası zəif qiymətləndirilir. Missingness və balanssız dizaynın mexanizmini ayrıca müzakirə edin.

[RNA-seq dizayn qeydi](../../research/findings/rnaseq-design-and-effect.md) effect və batch ayrımına praktik nümunə verir.
