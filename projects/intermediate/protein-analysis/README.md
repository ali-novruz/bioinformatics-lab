# Protein ardıcıllığı və eksperimental struktur

```bash
python scripts/lab.py run proteins
```

Başladıcı UniProt P01308 FASTA-sını və RCSB 1CRN PDB-sini əvvəlki yoxlanmış mənbə manifestinə uyğun endirir. Hazır giriş varsa hash-lə yoxlayır. [Dataset mənşəyi](../../../datasets/reference-manifest.json).

P01308 insan insulin prekursorunun ardıcıllığıdır; 1CRN isə **crambin** strukturudur. Bu iki müxtəlif protein səhvən bir molekul kimi birləşdirilmir. Ardıcıllıq hissəsi uzunluq və amin turşusu tərkibini, struktur hissəsi 1CRN model 0, chain A üzrə Cα məsafələrini hesablayır.

Nəticələr: 110 aa insulin prekursoru, 46 Cα qalığı olan crambin strukturu, məsafə matrisi, <8 Å Cα cütləri və 3D trace. Təmaslar ardıcıllıq qonşularını da əhatə edir və kimyəvi rabitələr kimi adlandırılmır. Matrisin simmetriyası və sıfır diaqonalı yoxlanır.

Hər icra `results/runs/proteins/` daxilində yeni nəticə qovluğu yaradır. [Bütün layihələrin icra hesabatı](../../../results/expanded-projects/README.md). Bu layihə folding proqnozu və ya AlphaFold reproduksiyası deyil; real eksperimental koordinatların təsviri analizidir.
