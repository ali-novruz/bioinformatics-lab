# Real ardıcıllıqlardan filogenetik ağac

```bash
python scripts/lab.py run phylogeny --offline
```

**Giriş:** Biopython-un sabit revision-undan alınmış 7 Opuntia DNA fraqmentinin [hazır çoxlu alignment-i](../../../datasets/examples/phylogeny/opuntia.aln). [Mənbə kartı](../../../datasets/examples/README.md). GenBank accession-ları ağac uclarında saxlanılır. Yeni alignment hesablanmır; hazır alignment-dən ağac çıxarılır.

## Hesablama

1. 156 sütundan hər hansı taxonda gap və ya qeyri-ACGT olan sütunlar birlikdə çıxarılır.
2. Qalan 146 sütunda cütlər üzrə mismatch payı, yəni düzəlişsiz p-distance hesablanır.
3. Neighbor joining ilə **köksüz** ağac qurulur. Ekrandakı başlanğıc nöqtəsi bioloji əcdad kökü deyil.
4. Sütunlar yerinə qoymaqla 200 dəfə yenidən seçilir, hər replicate-də ağac qurulur.
5. Köksüz bipartition-lar kanonik formada müqayisə edilir. Complement tərəflər eyni bölünmə sayılır; dəstək faizləri saxlanılır.

Çıxış: `tree.nwk`, `distances.csv`, saxlanmış/çıxarılmış sütunlar, bootstrap split-ləri, ağac şəkli və icra mənşəyi. [Hazır nəticələr](../../../results/expanded-projects/phylogeny).

## Faktiki nəticə və şərh

7 taxon, 146 tam sütun, cəmi **8 dəyişkən sütun**; 200 bootstrap replicate. Bu icrada mənfi branch length yoxdur. Metod ümumi halda mənfi uzunluq verə bilər; kod onu səssizcə sıfırlamır və xülasədə sayını göstərir.

Qısa fraqment və az dəyişkən mövqe səbəbindən nəticə tam növ filogeniyası deyil. Bootstrap faizi kladın “doğru olma ehtimalı” kimi şərh edilmir. Site independence fərziyyəsi və p-distance-in çoxsaylı əvəzlənmələri düzəltməməsi qeyd olunur. Molekulyar saat və təkamül tarixləri hesablanmır.

Yoxlama: ayrılması məlum dörd sintetik taxonda gözlənilən split 100% dəstək alır; gap/ambiguous sütunların çıxarılması və complement split uyğunluğu ayrıca yoxlanır. Sintetik testlə real analiz ayrı saxlanılır.
