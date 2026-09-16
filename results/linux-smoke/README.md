# Linux positive-control nəticəsi

[Uğurlu CI run](https://github.com/ali-novruz/bioinformatics-lab/actions/runs/35044952917),
commit `2923a27c8983c7dcdc4d39bb88c86bf67cc05894`.

Sintetik 6 kb reference və 422 fərqli paired fragment istifadə edildi.
Məlum haploid SNV yeganə PASS call kimi dəqiq tapıldı; STAR 422/422 cütü
unikal hizaladı, featureCounts 422 fragment-i genə saydı.
[Yoxlama nəticəsi](validation.json), [truth](fixture/truth.json),
[provenance](provenance.json).

Bu sınaq real biological accuracy benchmark-ı deyil. Məqsəd malformed FASTQ,
boş VCF və boş count nəticəsinin uğurlu workflow kimi qəbul edilməsinin qarşısını almaqdır.
