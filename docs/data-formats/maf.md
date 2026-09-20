# MAF

Mutation Annotation Format xərçəng genomikasında annotasiya edilmiş somatik variant cədvəlidir. Əsas sahələr `Hugo_Symbol`, `Chromosome`, `Start_Position`, `Reference_Allele`, `Tumor_Seq_Allele2`, `Variant_Classification`, `Tumor_Sample_Barcode`-dur.

MAF universal schema deyil; GDC və annotatorlar əlavə sütun verir. Build, caller, matched normal, filter və annotator versiyasını saxlayın. Bir variant bir neçə transcript sətrinə çevrilə bilər, ona görə “mutation count” üçün biological unit əvvəlcədən seçilməlidir. QC: barcode, tumor/normal əlaqəsi, duplicate locus+allele və classification lüğəti. [GDC MAF](https://docs.gdc.cancer.gov/Data/File_Formats/MAF_Format/).
