# Real GO-slim funksional zənginləşmə

**Sual:** yeast RNA-seq analizində seçilən genlər, ölçülmüş genlərlə müqayisədə hansı bioloji proseslərdə çox təmsil olunur?

```bash
python scripts/lab.py run enrichment --offline
```

Girişlər repo daxilindədir: [real differential expression cədvəli](../../../results/raw-examples/rna-model/differential_expression.csv) və [SGD annotasiya alt dəsti](../../../datasets/examples/enrichment/sgd_go_slim_chrI.tsv). İlk endirmə tələb olunmur. [Mənbə və çevirmə qaydası](../../../datasets/examples/README.md).

## Metod

- Universe: adjusted p-value-su sonlu olan 84 ölçülmüş gen. Bütün genomun genlərini fon kimi götürmürük.
- Foreground: əvvəlki analizdə padj<0.05 olan 1 gen, YAL005C. Yeni nəticə almaq üçün seçim həddi dəyişdirilməyib.
- SGD GO-slim biological-process annotasiyaları; root term çıxarılıb, gen-term cütləri unikal saxlanılıb.
- Universe daxilində ən azı 2 geni olan, bütün universe-i örtməyən hər term yoxlanır. Sıfır overlap olan term-lər də çoxsaylı test düzəlişinə daxildir.
- Bir tərəfli hypergeometric upper-tail p-value və bütün 62 uyğun term üzrə BH düzəlişi.

Nəticə: **62 test, FDR<0.05 səviyyəsində 0 əhəmiyyətli kateqoriya**. 84 gendən 67-si seçilmiş GO-slim BP dəstində annotasiyalıdır, 17-si deyil. Annotasiyasız ölçülmüş genlər fonda saxlanılıb; natamam annotasiyanın təsiri limit kimi qeyd olunur.

Çıxışlar: `enrichment.csv`, dəqiq universe/foreground siyahıları, qrafik, `summary.json`, `run.json`. [Saxlanmış icra](../../../results/expanded-projects/go-enrichment).

## Nəticənin sərhədi

Bir seçilmiş gen ilə statistik güc çox zəifdir. GO term-ləri üst-üstə düşə bilir; BH nəticəsi eksplorativ şərh edilməlidir. Bu, GO-slim over-representation analizidir, pathway aktivliyinin ölçülməsi və ya səbəb-nəticə sübutu deyil. Real məlumatdan nəticə alınması “mütləq əhəmiyyətli nəticə” tələb etmir.

Yoxlama: hypergeometric p-value müstəqil Fisher exact hesablaması ilə tutuşdurulur; boş seçim və universe xaricində gen halları test edilir. Növbəti elmi mərhələ bütün genom üzrə əvvəlcədən planlaşdırılmış, annotasiya versiyası uyğun analizdir.
