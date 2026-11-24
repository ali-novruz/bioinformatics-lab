"""Snapshot every ClinVar record for MEFV and HBB plus UniProt domain maps.

Writes two dated files into datasets/examples/regional/ and registers them in
datasets/examples/manifest.json with size and SHA-256. ClinVar changes weekly,
so analyses read the snapshot, never the live service.

    python scripts/fetch_regional_clinvar.py
"""

import hashlib
import json
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datasets/examples/regional"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
GENES = {"MEFV": "O15553", "HBB": "P68871"}
BATCH = 200
PAUSE = 0.4  # NCBI allows three requests per second without an API key


def get_json(url):
    with urllib.request.urlopen(url, timeout=90) as response:
        return json.load(response)


def clinvar_ids(gene):
    query = urllib.parse.urlencode(
        {"db": "clinvar", "term": f"{gene}[gene]", "retmax": 10000, "retmode": "json"}
    )
    result = get_json(f"{EUTILS}/esearch.fcgi?{query}")["esearchresult"]
    ids = result["idlist"]
    if int(result["count"]) != len(ids):
        raise ValueError(
            f"{gene}: esearch returned {len(ids)} of {result['count']} ids"
        )
    return ids


def summarize(record, gene):
    germline = record["germline_classification"]
    variation = record["variation_set"][0]
    gnomad = [
        float(a["value"])
        for a in variation.get("allele_freq_set", [])
        if "gnomAD" in a["source"] and a["value"]
    ]
    location = next(
        (
            loc
            for loc in variation.get("variation_loc", [])
            if loc["assembly_name"] == "GRCh38"
        ),
        {},
    )
    traits = sorted({t["trait_name"] for t in germline.get("trait_set", [])})
    return {
        "variation_id": record["uid"],
        "accession_version": record["accession_version"],
        "gene_query": gene,
        "genes": ";".join(g["symbol"] for g in record["genes"]),
        "obj_type": record["obj_type"],
        "title": record["title"],
        "cdna_change": variation.get("cdna_change", ""),
        "protein_change": record.get("protein_change", ""),
        "molecular_consequence": ";".join(record.get("molecular_consequence_list", [])),
        "classification": germline.get("description", ""),
        "review_status": germline.get("review_status", ""),
        "last_evaluated": germline.get("last_evaluated", ""),
        "traits": ";".join(traits),
        "gnomad_af_max": max(gnomad) if gnomad else "",
        "grch38_chr": location.get("chr", ""),
        "grch38_start": location.get("start", ""),
        "grch38_stop": location.get("stop", ""),
    }


def fetch_clinvar():
    rows = []
    for gene in GENES:
        ids = clinvar_ids(gene)
        time.sleep(PAUSE)
        for i in range(0, len(ids), BATCH):
            chunk = ids[i : i + BATCH]
            data = urllib.parse.urlencode(
                {"db": "clinvar", "id": ",".join(chunk), "retmode": "json"}
            ).encode()
            with urllib.request.urlopen(
                f"{EUTILS}/esummary.fcgi", data=data, timeout=120
            ) as response:
                result = json.load(response)["result"]
            missing = [uid for uid in chunk if uid not in result]
            if missing:
                raise ValueError(
                    f"{gene}: esummary omitted {len(missing)} ids, e.g. {missing[:3]}"
                )
            rows += [summarize(result[uid], gene) for uid in chunk]
            time.sleep(PAUSE)
        print(f"{gene}: {len(ids)} records")
    return pd.DataFrame(rows)


def fetch_uniprot():
    out = {}
    for gene, accession in GENES.items():
        entry = get_json(f"https://rest.uniprot.org/uniprotkb/{accession}.json")
        if entry["genes"][0]["geneName"]["value"] != gene:
            raise ValueError(f"UniProt {accession} is not {gene}")
        out[gene] = {
            "accession": accession,
            "entry_version": entry["entryAudit"]["entryVersion"],
            "length": entry["sequence"]["length"],
            "features": [
                {
                    "type": f["type"],
                    "description": f.get("description", ""),
                    "start": f["location"]["start"]["value"],
                    "end": f["location"]["end"]["value"],
                }
                for f in entry["features"]
                if f["type"]
                in {"Domain", "Zinc finger", "Coiled coil", "Region", "Helix"}
            ],
        }
    return out


def register(paths, today):
    manifest_path = ROOT / "datasets/examples/manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = {
        "clinvar": f"{EUTILS}/esummary.fcgi?db=clinvar (query: MEFV[gene], HBB[gene])",
        "uniprot": "https://rest.uniprot.org/uniprotkb/{O15553,P68871}.json",
    }
    for kind, path in paths.items():
        rel = path.relative_to(ROOT).as_posix()
        data = path.read_bytes()
        manifest["files"] = [f for f in manifest["files"] if f["path"] != rel]
        manifest["files"].append(
            {
                "path": rel,
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "source_url": sources[kind],
                "source_sha256": hashlib.sha256(data).hexdigest(),
                "retrieved": today,
                "transformation": "Selected fields from the live service response (not stored); source_sha256 is the hash of this derived file; see scripts/fetch_regional_clinvar.py"
                + ("; gzip (mtime 0) of the TSV" if kind == "clinvar" else ""),
            }
        )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main():
    today = date.today().isoformat()
    table = fetch_clinvar()
    clinvar_path = OUT / f"clinvar-mefv-hbb-{today}.tsv.gz"
    table.to_csv(
        clinvar_path,
        sep="\t",
        index=False,
        lineterminator="\n",
        compression={"method": "gzip", "mtime": 0},
    )
    uniprot_path = OUT / f"uniprot-mefv-hbb-{today}.json"
    uniprot_path.write_text(
        json.dumps(fetch_uniprot(), indent=1) + "\n", encoding="utf-8", newline="\n"
    )
    register({"clinvar": clinvar_path, "uniprot": uniprot_path}, today)
    print(clinvar_path, len(table))


if __name__ == "__main__":
    main()
