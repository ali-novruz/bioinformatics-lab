"""Run small pinned Linux FASTQ examples, then require nonempty mapped evidence."""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fetch_raw_examples import fetch
from sklearn.decomposition import PCA

from biolab.transcriptomics import differential_expression

ROOT = Path(__file__).resolve().parents[1]


def run(command, **kwargs):
    subprocess.run([str(value) for value in command], check=True, cwd=ROOT, **kwargs)


def save_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def rna_plots(results, normalized, metadata, output):
    log_counts = np.log1p(normalized)
    pca = PCA(n_components=2)
    coordinates = pca.fit_transform(log_counts)
    fig, ax = plt.subplots(figsize=(8, 5))
    for group, label in [
        ("untreated", "Rap1-AID uninduced"),
        ("treated", "Rap1-AID + IAA 30 min"),
    ]:
        mask = metadata.loc[log_counts.index, "condition"].eq(group)
        ax.scatter(coordinates[mask, 0], coordinates[mask, 1], label=label, s=65)
    for index, sample in enumerate(log_counts.index):
        ax.annotate(
            sample,
            coordinates[index],
            fontsize=7,
            xytext=(3, 5),
            textcoords="offset points",
        )
    ax.set(
        xlabel=f"PC1 ({pca.explained_variance_ratio_[0]:.1%})",
        ylabel=f"PC2 ({pca.explained_variance_ratio_[1]:.1%})",
        title="GSE110004: chromosome I subsample; log1p normalized counts",
    )
    ax.margins(0.2)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(output / "pca.png", dpi=150)
    plt.close(fig)
    genes = log_counts.var().nlargest(30).index
    z = log_counts[genes].T
    z = z.sub(z.mean(axis=1), axis=0).div(z.std(axis=1).replace(0, 1), axis=0)
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(z, cmap="RdBu_r", vmin=-2, vmax=2, aspect="auto")
    ax.set_xticks(range(len(z.columns)), z.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(z)), z.index, fontsize=7)
    ax.set_title("GSE110004 chrI: 30 most variable genes; row z-score")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(output / "heatmap.png", dpi=150)
    plt.close(fig)
    valid = results.dropna(subset=["padj", "log2FoldChange"])
    significant = (valid.padj < 0.05) & (valid.log2FoldChange.abs() > 1)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(
        valid.log2FoldChange,
        -np.log10(valid.padj.clip(lower=1e-300)),
        c=np.where(significant, "#bf414d", "#5f7e89"),
        s=15,
    )
    ax.axhline(-np.log10(0.05), color="black", ls="--", lw=0.7)
    ax.set(
        xlabel="log2 fold change: IAA 30 min / uninduced (unshrunken)",
        ylabel="-log10 adjusted p",
        title="GSE110004: chrI subset, exploratory differential expression",
    )
    fig.tight_layout()
    fig.savefig(output / "volcano.png", dpi=150)
    plt.close(fig)


def rna_example(raw, output):
    metadata = pd.read_csv(ROOT / "datasets/raw-rnaseq-samples.csv", index_col=0)
    folder = raw / "rnaseq"
    env = {
        **os.environ,
        "THREADS": "2",
        "STAR_SA_INDEX_NBASES": "7",
        "SJDB_OVERHANG": "100",
        "SKIP_QC": "0",
        "SKIP_MULTIQC": "0",
    }
    rows = []
    mapping = {}
    for sample in metadata.index:
        sample_out = output / "rnaseq" / sample
        run(
            [
                "bash",
                "workflows/rnaseq.sh",
                folder / "genome.fa",
                folder / "genes.gtf",
                folder / f"{sample}_1.fastq.gz",
                folder / f"{sample}_2.fastq.gz",
                sample,
                sample_out,
                2,
            ],
            env=env,
        )  # Verified reverse-stranded library.
        rows.append(
            {
                "sample_id": sample,
                "counts_path": str(sample_out / f"{sample}.counts.tsv"),
            }
        )
        lines = (sample_out / f"{sample}.Log.final.out").read_text().splitlines()
        star = {
            line.split("|", 1)[0].strip(): line.split("|", 1)[1].strip()
            for line in lines
            if "|" in line
        }
        input_pairs = int(star["Number of input reads"])
        unique = int(star["Uniquely mapped reads number"])
        if input_pairs != 50000 or unique < input_pairs * 0.5:
            raise ValueError(f"Unexpected read count or poor mapping: {sample}: {star}")
        mapping[sample] = {
            "input_pairs": input_pairs,
            "uniquely_mapped_pairs": unique,
            "uniquely_mapped_percent": star["Uniquely mapped reads %"],
        }
    model = output / "rna-model"
    model.mkdir()
    samples_path = model / "counts_manifest.tsv"
    pd.DataFrame(rows).to_csv(samples_path, sep="\t", index=False)
    run(
        [
            sys.executable,
            "scripts/combine_counts.py",
            "--samples",
            samples_path,
            "--output",
            model / "counts.tsv",
        ]
    )
    counts = pd.read_csv(model / "counts.tsv", sep="\t", index_col=0).T
    if (counts.sum(axis=1) < 1000).any():
        raise ValueError("Insufficient assigned fragments in at least one sample")
    results, normalized, summary = differential_expression(
        counts, metadata, design="~ condition"
    )
    results.to_csv(model / "differential_expression.csv", index_label="gene_id")
    normalized.to_csv(model / "normalized_counts.csv", index_label="sample_id")
    metadata.to_csv(model / "metadata.csv")
    summary.update(
        dataset="GSE110004, nf-core chromosome I subsample",
        biological_contrast="Rap1-AID + IAA 30 minutes / Rap1-AID uninduced",
        limitation="Chromosome-targeted subsampling; not genome-wide inference or reproduction of the full paper",
        mapping=mapping,
        assigned_fragments=counts.sum(axis=1).astype(int).to_dict(),
    )
    save_json(model / "summary.json", summary)
    rna_plots(results, normalized, metadata, model)
    return summary


def variant_example(raw, output):
    folder = raw / "variants"
    combined = output / "variant-input"
    combined.mkdir()
    for mate in (1, 2):
        with (combined / f"R{mate}.fastq.gz").open("wb") as writer:
            for lane in ["L001", "L002", "L004", "L007", "L008"]:
                with (folder / f"tiny_n_{lane}_R{mate}_xxx.fastq.gz").open(
                    "rb"
                ) as reader:
                    shutil.copyfileobj(reader, writer)
    # Concatenated gzip members are valid gzip and preserve all five lanes.
    variant_out = output / "variants"
    run(
        [
            "bash",
            "workflows/variants.sh",
            folder / "reference.fa",
            combined / "R1.fastq.gz",
            combined / "R2.fastq.gz",
            "sarek-tiny-normal",
            variant_out,
            2,
        ],
        env={**os.environ, "THREADS": "2", "SKIP_QC": "0", "SKIP_MULTIQC": "0"},
    )
    mapped = int(
        subprocess.check_output(
            ["samtools", "view", "-c", "-F", "4", variant_out / "aligned.bam"],
            text=True,
        )
    )
    if mapped == 0:
        raise ValueError("External DNA fixture produced no mapped reads")
    records = subprocess.check_output(
        [
            "bcftools",
            "query",
            "-f",
            "%CHROM\t%POS\t%REF\t%ALT\t%FILTER\n",
            variant_out / "filtered.vcf.gz",
        ],
        text=True,
    ).splitlines()
    summary = {
        "dataset": "nf-core/sarek tiny normal, five lanes",
        "mapped_reads": mapped,
        "variant_records": len(records),
        "pass_records": sum(line.endswith("\tPASS") for line in records),
        "annotation": "not run: no compatible GFF3 supplied",
        "limitation": "External integration fixture; donor provenance and truth set not established; not a biological or clinical benchmark",
    }
    save_json(variant_out / "summary.json", summary)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--raw", type=Path, default=ROOT / "datasets/raw/examples")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    raw = args.raw.resolve()
    fetch("all", raw)
    shutil.copy2(raw / "verified-manifest.json", output / "input-manifest.json")
    scripts = (
        list((ROOT / "scripts").glob("*.py"))
        + list((ROOT / "workflows").glob("*.sh"))
        + list((ROOT / "src/biolab").glob("*.py"))
    )
    save_json(
        output / "run.json",
        {
            "git_commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
            ).strip(),
            "github_run_id": os.environ.get("GITHUB_RUN_ID"),
            "python": sys.version,
            "source_files_sha256": {
                p.relative_to(ROOT).as_posix(): hashlib.sha256(
                    p.read_bytes()
                ).hexdigest()
                for p in scripts
            },
        },
    )
    with (output / "python-environment.txt").open("w") as handle:
        run([sys.executable, "-m", "pip", "freeze"], stdout=handle)
    summary = {
        "variants": variant_example(raw, output),
        "rnaseq": rna_example(raw, output),
    }
    save_json(output / "validation.json", summary)
    print(json.dumps(summary, indent=2))
