# Newick

Newick ağac topologiyasını mötərizə, vergül, branch length və daxili node label-ları ilə saxlayır: `((a:0.02,b:0.03)87:0.01,(c:0.04,d:0.04)72:0.02);`. `87` bootstrap faizidirsə bunu ayrıca yazın; format label-in mənasını demir. Unrooted ağacın faylda çəkilmə istiqaməti təkamül kökü deyil.

QC: terminal adları unikal, taxon sayı gözlənən, branch length qeyri-mənfi, support miqyası 0–1 və ya 0–100 olaraq açıq olmalıdır. Biopython `Phylo.read(path, "newick")` ilə oxuyur. [Opuntia layihəsi](../../projects/intermediate/phylogeny/README.md) və [Biopython Phylo](https://biopython.org/wiki/Phylo).
