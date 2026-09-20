# HDF5 və Zarr

HDF5 iyerarxik group/dataset/attribute-ları bir faylda, Zarr isə chunk-ları filesystem və ya object storage-da saxlayır. Chunk shape access pattern-ə uyğun seçilməlidir; gene-row və sample-column sorğuları fərqli I/O yaradır.

Schema versiyası, shape, dtype, missing representation, axis adları, compressor və chunk grid metadata-da olmalıdır. Zarr minlərlə kiçik obyekt yarada bilər; HDF5 paralel write və cloud access üçün başqa məhdudiyyət daşıyır. [h5py](https://docs.h5py.org/) · [Zarr spec](https://zarr-specs.readthedocs.io/).
