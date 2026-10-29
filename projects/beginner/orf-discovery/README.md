# Dairəvi genomda ORF namizədlərinin axtarışı

```bash
python scripts/lab.py run orfs --offline
```

**Giriş:** real PhiX174 referens genomu, NC_001422.1, 5386 nt. Kiçik [FASTA nüsxəsi](../../../datasets/examples/orfs/NC_001422.1.fasta) repo daxilindədir və əvvəlki mənbə hash-i ilə uyğundur.

Alqoritm hər iki istiqamətdə ATG-dən başlayan, eyni oxuma çərçivəsində ilk TAA/TAG/TGA ilə bitən hissələri tapır. Minimum protein uzunluğu 30 amin turşusudur. Genom dairəvi olduğundan origin-i keçən namizədlər də axtarılır. Hər başlanğıc ilk genom nüsxəsində bir dəfə götürülür, bir tam genom dövründən uzun namizəd qəbul edilmir. Daxili ATG-lərdən başlayan nested ORF-lər ayrıca saxlanılır.

## Koordinat və çıxış

`segments0` referens üzərində sıfırdan başlayan, sağ sərhədi daxil etməyən interval siyahısıdır. Origin-i keçən ORF iki intervala bölünür. Minus strand üçün intervallar tərcümə istiqaməti ardıcıllığında verilir; hər parçanın reverse complement-i bu sırada birləşdirilməlidir. Stop kodonu nucleotide uzunluğuna daxildir, protein FASTA-sına daxil deyil. `frame_offset` orientasiya olunmuş ardıcıllığın başlanğıcına aiddir.

Çıxışlar: `orfs.csv`, tam `orfs.json`, namizəd proteinlər üçün `proteins.fasta`, koordinat qrafiki və mənşə qeydi. [Saxlanmış nəticələr](../../../results/expanded-projects/orf-discovery).

Nəticə: **114 namizəd** (93 plus, 21 minus), **24 origin-i keçir**, ən uzun namizəd 522 aa-dır. Bunlar 114 təsdiqlənmiş gen demək deyil. Alternativ start kodonları, coding potential, ifadə sübutu və kurasiya edilmiş gen annotasiyası bu sadə start-stop axtarışında istifadə olunmur.

Yoxlama: ilk stop-da dayanma, məlum proteinə tərcümə, hər iki istiqamətdə origin keçidi və çıxış koordinatlarından ilkin coding sequence-in bərpası test edilir. Mənbədə qeyri-müəyyən nukleotid varsa, kod səssiz fərziyyə etmək əvəzinə aydın xəta verir.

## Genişləndirilmiş analiz: namizədlər həqiqi genlərlə müqayisədə

[`scripts/run_phix174_showcase.py`](../../../scripts/run_phix174_showcase.py) ORF axtarışını dəyişmədən onun nəticəsini NCBI-nin kurasiya edilmiş [GenBank qeydi](../../../datasets/examples/orfs/NC_001422.1.gb) ilə qiymətləndirir. GenBank ardıcıllığı analiz edilən FASTA ilə eynidir; CDS koordinatları namizəd tapmaq üçün yox, yalnız qiymətləndirmə üçün istifadə olunur. Saxlanmış nəticə: [`results/showcase/phix174-orf/`](../../../results/showcase/phix174-orf/).

| Sual | Nəticə |
|---|---|
| 114 namizəd neçə müstəqil lokusdur? | Eyni stop kodonunu paylaşanlar bir lokusdur: **36 lokus** (22 plus, 14 minus) |
| Həqiqi genlər tapılırmı? | 11 CDS, 10 lokus; **10/10 lokus** və **11/11 dəqiq start** namizədlər arasındadır |
| Ən uzun ATG düzgün startdırmı? | Gen A üçün yox: 27 nt yuxarıdakı ATG 522 aa verir, həqiqi A 513 aa-dır |
| Precision | 30 aa-da 0.28; tam recall ilə ən yaxşısı 35 aa-da 0.31. 150 aa-da 0.71, amma recall 0.5-ə düşür (J 38 aa, K 56 aa itir) |
| Minus strand | 14 lokusun heç biri gen deyil: PhiX174-ün bütün genləri plus strand-dadır |
| Təsadüfi gözlənti | 200 kompozisiya saxlayan qarışdırmada ≥100 aa lokus orta 0.5, maksimum 3; həqiqi genomda **10** (p = 0.005). Ən uzun: 522 aa, qarışdırılmışda maksimum 222 aa |
| Üst-üstə düşən genlər | 8 cüt, **hamısı fərqli oxuma çərçivəsində** (A–B, D–E, K–C …); genomun 96%-i kodlaşdırıcıdır |

Çərçivə müqayisəsi birləşdirilmiş seqmentlər boyunca kodon fazası ilə aparılır, çünki 5386 üçə bölünmür və origin-i keçən genlərdə genom koordinatına görə çərçivə yanlış olardı.

```bash
python scripts/run_phix174_showcase.py
```

Hədlər: uyğunlaşdırma strand və stop kodonu ilədir; qarışdırma mononukleotid tərkibini saxlayır, kodon quruluşunu yox; tək, gen sıxlığı yüksək faq genomudur.
