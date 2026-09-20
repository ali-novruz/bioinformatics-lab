# Kompozisional məlumat

Microbiome relative abundance, cell-type fraction və bəzi proteomik ölçülər cəmi sabit olan kompozisiyalardır. Bir komponentin payı artanda başqalarının payı mexaniki azalır; adi korrelyasiya yalnış əlaqə yarada bilər.

## Log-ratio yanaşması

- CLR: hər komponenti nümunənin geometrik ortasına nisbətləndirir;
- ALR: seçilmiş referens komponentə nisbət götürür;
- ILR: ortonormal balans koordinatları qurur.

Sıfırlar log-ratio üçün problemdir. Pseudocount seçimi neytral deyil və az-abundant xüsusiyyətlərə güclü təsir edə bilər. Sampling zero ilə struktur sıfırı ayırmaq, zero-replacement sensitivity göstərmək lazımdır.

## Praktik protokol

1. Mütləq sayım, kitabxana ölçüsü və detection limit-i saxlayın.
2. Filtr və sıfır siyasətini əvvəlcədən yazın.
3. Analizi raw count-a uyğun model və log-ratio yanaşması ilə müqayisə edin.
4. Effektləri “faiz artdı” əvəzinə hansı denominatora nisbət olduğunu qeyd etməklə verin.
5. Spike-in və ya qPCR kimi absolute-abundance məlumatı varsa nəticəni onunla yoxlayın.

[Systems biology modulu](../systems-biology/README.md) və [QIIME 2 məqalə qeydi](../../research/papers/qiime2.md) workflow kontekstini verir.
