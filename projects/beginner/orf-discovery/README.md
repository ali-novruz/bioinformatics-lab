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
