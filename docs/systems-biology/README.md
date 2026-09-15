# Systems biology

### Şəbəkə modeli
Node gen/protein/metabolit ola bilər; edge fiziki interaction, tənzimləmə və ya funksional assosiasiyadır. Edge tiplərini qarışdırmayın. Degree yüksəkliyi essentiality sübutu deyil, araşdırma bias-ını da əks etdirə bilər.

### Pathway və enrichment
Reactome reaksiyalar və pathways, STRING associations verir. Fon genlərini ölçülən/test edilən genlərlə məhdudlaşdırın. Hypergeometric ORA çoxlu pathway testləri üçün düzəliş tələb edir. Eyni gen bir neçə pathway-də olduğu üçün nəticələr asılıdır.

### Dinamika və metabolizm
ODE-lər zaman davranışını, flux balance analysis isə S·v=0 və flux constraints altında steady-state axınları modelləşdirir. FBA obyektiv funksiyası (məsələn biomass) biological assumption-dır. Optimal həllin yeganəliyini və alternativ flux-ları yoxlayın.

### Araşdırma
Problem: network incomplete və tissue-specific deyil. Eksperiment: müxtəlif confidence threshold-ları ilə centrality sıralamasını müqayisə edin. Data: STRING/Reactome. Yeni sual: prioritet gen sırasi edge confidence-ə nə qədər həssasdır?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://reactome.org/userguide/analysis). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
