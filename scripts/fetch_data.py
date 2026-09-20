"""Download bounded public datasets, preserving source and SHA-256 provenance."""

import argparse
import gzip
import hashlib
import io
import json
import tarfile
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "datasets/raw"
SOURCES = {
    "pasilla": "https://bioconductor.org/packages/3.23/data/experiment/src/contrib/pasilla_1.40.0.tar.gz",
    "phix": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_001422.1&rettype=fasta&retmode=text",
    "giab": "https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/NA12878_HG001/NISTv4.2.1/GRCh38/HG001_GRCh38_1_22_v4.2.1_benchmark.vcf.gz",
    "uniprot": "https://rest.uniprot.org/uniprotkb/P01308.fasta",
    "pdb": "https://files.rcsb.org/download/1CRN.pdb",
}


def request(url):
    return urllib.request.urlopen(
        urllib.request.Request(
            url, headers={"User-Agent": "bioinformatics-lab/0.1 research teaching"}
        ),
        timeout=90,
    )


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save(name, data, url, transformation):
    RAW.mkdir(parents=True, exist_ok=True)
    manifest = RAW / "provenance.json"
    records = json.loads(manifest.read_text()) if manifest.exists() else {}
    old = records.get(name)
    baseline_path = ROOT / "datasets/reference-manifest.json"
    baseline = json.loads(baseline_path.read_text()) if baseline_path.exists() else {}
    if name in baseline and digest(data) != baseline[name]["sha256"]:
        raise ValueError(
            f"Source differs from reference snapshot for {name}; investigate and version explicitly"
        )
    if old and old["sha256"] != digest(data):
        raise ValueError(f"Source changed for {name}; create a new version explicitly")
    path = RAW / name
    if path.exists() and digest(path.read_bytes()) != digest(data):
        raise ValueError(f"Local file differs: {name}")
    temp = RAW / (name + ".part")
    temp.write_bytes(data)
    temp.replace(path)
    records[name] = {
        "source_url": url,
        "retrieved_at": datetime.now(UTC).isoformat(),
        "bytes": len(data),
        "sha256": digest(data),
        "transformation": transformation,
    }
    staged = manifest.with_suffix(".part")
    staged.write_text(json.dumps(records, indent=2) + "\n")
    staged.replace(manifest)
    print(name, len(data), digest(data), flush=True)


def intact(names):
    manifest = RAW / "provenance.json"
    if not manifest.exists():
        return False
    records = json.loads(manifest.read_text())
    baseline_path = ROOT / "datasets/reference-manifest.json"
    baseline = json.loads(baseline_path.read_text()) if baseline_path.exists() else {}
    for n in names:
        p = RAW / n
        if not p.exists() or n not in records:
            return False
        if digest(p.read_bytes()) != records[n]["sha256"]:
            raise ValueError(f"Checksum mismatch: {n}")
        if n in baseline and digest(p.read_bytes()) != baseline[n]["sha256"]:
            raise ValueError(f"Cached input differs from reference snapshot: {n}")
    return True


def fetch(dataset):
    if dataset == "pasilla":
        names = ["pasilla_gene_counts.tsv", "pasilla_sample_annotation.csv"]
        if intact(names):
            return
        with request(SOURCES[dataset]) as response:
            blob = response.read(80_000_001)
        if len(blob) > 80_000_000:
            raise ValueError("Package exceeds 80 MB download guard")
        with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as archive:
            # Read specific members; never extract arbitrary archive paths.
            for name in names:
                data = archive.extractfile("pasilla/inst/extdata/" + name).read()
                save(
                    name,
                    data,
                    SOURCES[dataset],
                    "Exact package member pasilla/inst/extdata/"
                    + name
                    + "; archive sha256="
                    + digest(blob),
                )
    elif dataset == "giab":
        if intact(["giab_hg001_first1000.vcf"]):
            return
        lines = []
        count = 0
        with request(SOURCES[dataset]) as response:
            with gzip.GzipFile(fileobj=response) as stream:
                for line in stream:
                    lines.append(line)
                    if not line.startswith(b"#"):
                        count += 1
                    if count == 1000:
                        break
        if count != 1000:
            raise ValueError("Expected 1000 complete VCF records")
        save(
            "giab_hg001_first1000.vcf",
            b"".join(lines),
            SOURCES[dataset],
            "Header plus first 1000 records in source order; genomic prefix, NOT random sample; checksum applies to extracted subset, not full remote archive",
        )
    elif dataset in {"phix", "uniprot", "pdb"}:
        name = {
            "phix": "NC_001422.1.fasta",
            "uniprot": "P01308.fasta",
            "pdb": "1CRN.pdb",
        }[dataset]
        if intact([name]):
            return
        with request(SOURCES[dataset]) as response:
            blob = response.read(2_000_001)
        if len(blob) > 2_000_000:
            raise ValueError("Exceeded 2 MB guard")
        if dataset != "pdb" and not blob.startswith(b">"):
            raise ValueError("Expected FASTA, server returned another format")
        if dataset == "pdb" and b"ATOM " not in blob:
            raise ValueError("Expected PDB coordinate records")
        save(name, blob, SOURCES[dataset], "Unmodified response")
    else:
        raise ValueError(dataset)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=[*SOURCES, "all"], required=True)
    args = parser.parse_args()
    for name in SOURCES if args.dataset == "all" else [args.dataset]:
        fetch(name)
