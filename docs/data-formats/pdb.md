# PDB

## Struktur
Fixed-width ATOM/HETATM sətirləri: atom, residue, chain, residue number, x/y/z (Å), occupancy, B-factor.

## Nümunə
```text
ATOM      1  N   ALA A   1      11.104  13.207   9.111  1.00 20.00           N  
```
Nümunə sintetikdir; biological finding deyil. Binary formatlar üçün çevirmə əmri göstərilib.

## İstifadə
Struktur məsafəsi, bağlanma regionu və molekulyar vizuallaşdırma.

## Üstünlük və məhdudiyyət
Çox alətdə dəstəklənən klassik format. PDB ölçü/ad məhdudiyyətlərinə malikdir; müasir arxiv üçün PDBx/mmCIF üstün tutulur. Missing residues, insertion codes və alternate locations nəzərə alınmalıdır.

## Python ilə oxuma
```python
from Bio.PDB import PDBParser
s = PDBParser(QUIET=True).get_structure("model", "protein.pdb")
print(sum(1 for a in s.get_atoms()))
```
`pysam` əlavə platforma-asılı paketdir; Linux/WSL tövsiyə olunur. Cədvəl nümunələri yalnız göstərilən sadə alt formatı oxuyur; istehsal üçün format-aware parser seçin.

## Yoxlama və eksperiment
Eyni məlumatı text→binary→text çevirdikdə bioloji məzmunun saxlanmasını yoxlayın. Header, coordinate, strand, missing value və çoxallelli qeydlər üçün ayrıca test yaradın. Parserin qəbul etməsi biological validity demək deyil.

Mənbə: [rəsmi spesifikasiya](https://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html).
