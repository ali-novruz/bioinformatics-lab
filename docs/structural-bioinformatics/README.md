# Structural bioinformatics

### Struktur səviyyələri
Primary = amin turşusu ardıcıllığı; secondary = helix/sheet kimi lokal təşkiletmə; tertiary = bir zəncirin üçölçülü qatı; quaternary = çoxzəncirli kompleks. Folding yalnız statik koordinat deyil; konformasiya və mühit rol oynayır.

### Molekulyar əlaqələr
Hydrogen bonds, hidrofob təsir, elektrostatika və disulfid əlaqələri sabitlik və binding-ə töhfə verir. Cα məsafə cutoff-u contact map üçün sadələşdirmədir, kimyəvi bağ siyahısı deyil. Binding site analizi ligand, protonation, su, metal və missing residue-lərə həssasdır.

### Alətlər
PDB/mmCIF eksperimental model və metadata verir; resolution, occupancy və biological assembly-ni yoxlayın. AlphaFold proqnozunda pLDDT lokal etibar, PAE isə regionlar arasındakı nisbi yerləşmə qeyri-müəyyənliyi üçün faydalıdır. Yüksək etibar ligand binding və ya funksiyanın eksperimental sübutu deyil. PyMOL və ChimeraX struktur baxışı və ölçmə üçündür; versiya və sessiya əmrlərini saxlayın.

### Docking
AutoDock Vina kimi alətlər konformasiya axtarışı və approximate score ilə pose-ları sıralayır. Receptor preparation, ligand tautomerləri və grid əvvəlcədən yazılmalıdır. Redocking RMSD və məlum inactive kontrollar faydalıdır; docking score klinik effektivlik deyil.

### Araşdırma
Problem: etibarlı monomer modeli dinamik kompleks funksiyasını tam izah etmir. Eksperiment: predicted və experimental structure contact map-lərini hizalanmış residue-lərdə müqayisə edin. Zəiflik: missing regions və crystal packing. Yeni sual: aşağı confidence region-lar alternativ konformasiyanı əks etdirirmi?

## Mənbə və davamı

[Rəsmi və ya ilkin mənbə](https://www.nature.com/articles/s41586-021-03819-2). [Məqalə təhlilləri](../../research/papers/README.md) və [layihələr](../../projects/README.md) ilə birlikdə oxuyun. Buradakı eksperiment sualları təklifdir, əldə edilmiş nəticə deyil.
