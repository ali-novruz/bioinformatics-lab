# mzML və MGF

mzML spectrum, retention time, precursor və instrument metadata-nı XML-də saxlayır. MGF sadə tandem-MS peak list-dir:

```text
BEGIN IONS
TITLE=scan=42
PEPMASS=445.34
CHARGE=2+
100.1 250
175.2 430
END IONS
```

MGF-yə çevirmədə chromatogram və instrument metadata itə bilər; raw fayl, `msconvert` versiyası və command saxlanmalıdır. QC: spectrum sayı, MS level, charge, retention time, empty spectrum və m/z diapazonı. [HUPO-PSI mzML](https://www.psidev.info/mzML) · [MGF](https://www.matrixscience.com/help/data_file_help.html).
