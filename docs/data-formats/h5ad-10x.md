# h5ad/AnnData və 10x Matrix Market

10x paketi `matrix.mtx`, `barcodes.tsv`, `features.tsv` verir. Matrix çox vaxt feature×cell, `AnnData.X` isə cell×feature-dir; shape-i kor-koranə şərh etməyin. `.h5ad` daxilində `X`, `obs`, `var`, `layers`, `obsm` və `uns` saxlanır.

Raw count ilə log-normalized `X` qarışdırılmamalıdır; normalization və feature selection-in layer-i yazılmalıdır. Donor ID `obs`-da saxlanmasa hüceyrələr müstəqil replikat kimi səhv sayıla bilər. QC: unique barcode/feature, sparse dtype, empty droplet, mitochondrial pay, doublet və donor batch. [AnnData](https://anndata.readthedocs.io/) · [10x matrices](https://www.10xgenomics.com/support/software/cell-ranger/latest/analysis/outputs/cr-outputs-mex-matrices).
