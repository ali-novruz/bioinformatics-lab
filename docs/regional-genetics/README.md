# Regional genetika modulu

Bu modul Azərbaycan və Qafqaz auditoriyası üçün irsi xəstəlik sübutunu düzgün oxumağı öyrədir. Mövzunun yerli əhəmiyyəti haqqında ehtimalı yerli prevalence nəticəsi kimi təqdim etmir.

## Nümunə 1: MEFV və ailəvi Aralıq dənizi qızdırması

MEFV variantının ClinVar aggregate record-u bir neçə condition və inheritance kontekstini birləşdirə bilər. Tələbə variantın adını görüb “xəstəlik var” nəticəsi çıxarmamalıdır. Əvvəl zygosity, condition-specific RCV, phenotype uyğunluğu, ailə segregasiyası, review status və cari submitter sübutu ayrılır.

## Nümunə 2: HBB və hemoglobinopatiyalar

HBB `p.Glu7Val` üçün heterozygous trait ilə biallelic xəstəlik fərqlidir. Eyni allel üçün genotype və ikinci allel klinik mənanı dəyişir. Population frequency də ancestry kontekstində oxunmalıdır.

## Təhlükəsiz iş axını

1. Variantı genome build və HGVS ilə normallaşdırın.
2. VCV aggregate record-u və uyğun RCV condition record-unu ayırın.
3. Review status və son evaluation tarixini yazın.
4. Inheritance və zygosity-ni phenotype ilə əlaqələndirin.
5. Population frequency-ni ancestry, penetrance və xəstəlik mexanizmi ilə birlikdə qiymətləndirin.
6. Laborator təsdiq, genetic counseling və cari peşəkar guideline olmadan klinik qərar verməyin.

[İşlək layihə](../../projects/advanced/regional-variant-interpretation/README.md) · [ClinVar məlumatına çıxış](https://www.ncbi.nlm.nih.gov/clinvar/docs/access/) · [ClinVar review status](https://www.ncbi.nlm.nih.gov/clinvar/docs/review_status/)
