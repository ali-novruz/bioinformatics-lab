# bedGraph və BigWig

bedGraph `chrom`, 0-based `start`, half-open `end`, `value` sütunları ilə genom signalı saxlayır. BigWig indeksli binary qarşılıqdır və uzaq interval sorğusu verir.

```text
chr1 0 100 0.0
chr1 100 150 12.5
```

Interval-ları sort edin, chromosome adlarını `.chrom.sizes` ilə uyğunlaşdırın, overlap siyasəti və normalization növünü (raw depth, CPM/RPGC) yazın. Missing interval həmişə bioloji sıfır deyil. `bedGraphToBigWig signal.bedGraph genome.chrom.sizes signal.bw`. [UCSC BigWig](https://genome.ucsc.edu/goldenPath/help/bigWig.html).
