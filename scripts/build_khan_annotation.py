"""Recover Khan class names and probe annotation by numeric matching to SRBCT.

The ISLP split ships anonymous labels 1-4 and columns V1..V2308. The CRAN
package plsgenomics distributes the same Khan et al. (2001) arrays with named
classes and IMAGE clone annotation. This script accepts the mapping only when
every ISLP sample matches exactly one SRBCT sample and every column matches the
same-index SRBCT gene; any other outcome raises.

Run once with the optional reader:  uv run --with rdata python scripts/build_khan_annotation.py
"""

import hashlib
import io
import json
import tarfile
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import rdata
from fetch_khan import fetch

from biolab.expression_ml import load_khan

ROOT = Path(__file__).resolve().parents[1]
SOURCE = {
    "package": "plsgenomics",
    "version": "1.5-3",
    "url": "https://cran.r-project.org/src/contrib/plsgenomics_1.5-3.tar.gz",
    "archive_url": "https://cran.r-project.org/src/contrib/Archive/plsgenomics/plsgenomics_1.5-3.tar.gz",
    "sha256": "d9e6a9f81ea86d203d79024524d57009edc835d9ca99fe77929e8226d7fd3b28",
    "member": "plsgenomics/data/SRBCT.rda",
}
# plsgenomics/man/SRBCT.Rd: EWS coded 1, BL 2, NB 3, RMS 4.
SRBCT_NAMES = {1: "EWS", 2: "BL", 3: "NB", 4: "RMS"}
SAMPLE_MIN_CORR = 0.999
PROBE_MIN_CORR = 0.99


def download() -> bytes:
    for url in (SOURCE["url"], SOURCE["archive_url"]):
        try:
            with urllib.request.urlopen(url, timeout=90) as response:
                data = response.read()
        except OSError:
            continue
        if hashlib.sha256(data).hexdigest() != SOURCE["sha256"]:
            raise ValueError(f"plsgenomics archive checksum mismatch: {url}")
        return data
    raise ConnectionError("plsgenomics 1.5-3 archive is unreachable")


def load_srbct(archive: bytes) -> tuple[np.ndarray, np.ndarray, pd.DataFrame]:
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        member = tar.extractfile(SOURCE["member"])
        if member is None:
            raise ValueError("SRBCT.rda missing from archive")
        staged = ROOT / "datasets/raw/khan/.SRBCT.rda"
        staged.write_bytes(member.read())
    try:
        srbct = rdata.read_rda(staged)["SRBCT"]
    finally:
        staged.unlink()
    x = np.log(np.asarray(srbct["X"], dtype=float))
    y = np.asarray(srbct["Y"]).astype(int)
    genes = srbct["gene.names"].copy()
    genes.columns = ["image_id", "description"]
    genes["image_id"] = genes["image_id"].astype("Int64")
    if x.shape != (83, 2308) or len(genes) != 2308:
        raise ValueError(f"Unexpected SRBCT shape {x.shape}")
    return x, y, genes


def match_samples(xs: np.ndarray, reference: np.ndarray) -> tuple[np.ndarray, float]:
    corr = np.corrcoef(np.vstack([xs, reference]))[: len(xs), len(xs) :]
    index = corr.argmax(axis=1)
    best = float(corr.max(axis=1).min())
    if best < SAMPLE_MIN_CORR or len(set(index)) != len(xs):
        raise ValueError(f"Sample matching not one-to-one (min corr {best:.4f})")
    return index, best


def main() -> None:
    xtrain, xtest, ytrain, ytest = load_khan(fetch())
    x, y, genes = load_srbct(download())
    class_map: dict[int, str] = {}
    report = {"source": SOURCE, "splits": {}}
    matched_train = None
    for split, xs, ys in [("train", xtrain, ytrain), ("test", xtest, ytest)]:
        index, min_corr = match_samples(xs.to_numpy(float), x)
        if split == "train":
            matched_train = x[index]
        table = pd.crosstab(ys.to_numpy(), y[index])
        for label, row in table.iterrows():
            if (row > 0).sum() != 1:
                raise ValueError(f"Label {label} maps to several SRBCT classes")
            name = SRBCT_NAMES[int(row.idxmax())]
            if class_map.setdefault(int(label), name) != name:
                raise ValueError(f"Label {label} maps differently in {split}")
        report["splits"][split] = {
            "samples": len(xs),
            "min_sample_correlation": round(min_corr, 6),
            "srbct_rows": (index + 1).tolist(),
        }
    probe_corr = np.array(
        [
            np.corrcoef(xtrain.iloc[:, j], matched_train[:, j])[0, 1]
            for j in range(xtrain.shape[1])
        ]
    )
    if probe_corr.min() < PROBE_MIN_CORR:
        raise ValueError(f"Probe alignment failed (min corr {probe_corr.min():.4f})")
    report["class_map"] = {str(k): v for k, v in sorted(class_map.items())}
    report["probe_alignment"] = {
        "columns": int(len(probe_corr)),
        "min_correlation": round(float(probe_corr.min()), 6),
        "median_correlation": round(float(np.median(probe_corr)), 6),
        "rule": "column Vj equals SRBCT gene j after natural log",
    }
    annotation = genes.assign(
        probe_column=xtrain.columns,
        description=genes["description"].astype(str).str.strip(),
        alignment_correlation=probe_corr.round(6),
    )[["probe_column", "image_id", "description", "alignment_correlation"]]
    folder = ROOT / "datasets/annotations"
    folder.mkdir(exist_ok=True)
    annotation.to_csv(folder / "khan_probe_annotation.csv", index=False)
    (folder / "khan_annotation_verification.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print("Class map:", report["class_map"])
    print("Probe alignment min corr:", report["probe_alignment"]["min_correlation"])


if __name__ == "__main__":
    main()
