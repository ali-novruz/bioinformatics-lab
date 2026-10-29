"""Evaluate PhiX174 ORF candidates against the curated GenBank CDS and a shuffle null.

The canonical ORF scan (find_orfs, 30 aa, both strands, circular) is unchanged.
This script adds what the scan alone cannot say:
- which candidates are real genes, matched on strand and stop codon (a "locus"),
  and whether the ATG chosen as start equals the curated start;
- how precision and recall move with the minimum-length threshold;
- whether long ORFs are expected by chance, using composition-preserving
  shuffles of the same genome;
- which curated genes overlap in different reading frames.

GenBank CDS are used only for evaluation, never to find candidates.
"""

import json
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Bio import SeqIO

from biolab.orfs import find_orfs
from biolab.reporting import finish_run, new_run, write_json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets/examples/orfs"
FASTA = DATA / "NC_001422.1.fasta"
GENBANK = DATA / "NC_001422.1.gb"
MIN_AA = 30
SHUFFLES = 200
SEED = 7
LONG_AA = 100
# Classical PhiX174 gene letters (Sanger et al. 1977) for the RefSeq locus tags.
LETTERS = {
    "phiX174p01": "A",
    "phiX174p02": "A*",
    "phiX174p03": "B",
    "phiX174p04": "K",
    "phiX174p05": "C",
    "phiX174p07": "D",
    "phiX174p08": "E",
    "phiX174p09": "J",
    "phiX174p06": "F",
    "phiX174p10": "G",
    "phiX174p11": "H",
}


def stop_key(strand, segments):
    """Strand plus the genome coordinate just past the stop codon."""
    return (strand, segments[-1][1] if strand == "+" else segments[-1][0])


def load():
    genome = SeqIO.read(FASTA, "fasta")
    record = SeqIO.read(GENBANK, "genbank")
    seq = str(genome.seq).upper()
    if str(record.seq).upper() != seq:
        raise ValueError("GenBank sequence differs from the analysed FASTA")
    genes = []
    for feature in record.features:
        if feature.type != "CDS":
            continue
        tag = feature.qualifiers["locus_tag"][0]
        if tag not in LETTERS:
            raise ValueError(f"Unexpected CDS {tag}")
        strand = "+" if feature.location.strand == 1 else "-"
        segments = [(int(p.start), int(p.end)) for p in feature.location.parts]
        if strand == "-":
            raise ValueError("PhiX174 RefSeq CDS are expected on the plus strand")
        genes.append(
            {
                "gene": LETTERS[tag],
                "locus_tag": tag,
                "product": feature.qualifiers["product"][0],
                "strand": strand,
                "segments0": segments,
                "start0": segments[0][0],
                "start_frame": segments[0][0] % 3,
                "length_aa": len(feature.qualifiers["translation"][0]),
                "wraps_origin": len(segments) > 1,
            }
        )
    if sorted(g["gene"] for g in genes) != sorted(LETTERS.values()):
        raise ValueError("GenBank CDS set does not match the 11 expected genes")
    return seq, genes


def loci_of(candidates):
    loci = {}
    for c in candidates:
        loci.setdefault(stop_key(c["strand"], c["segments0"]), []).append(c)
    return {
        k: max(v, key=lambda c: c["length_aa"]) | {"starts": len(v)}
        for k, v in loci.items()
    }


def codon_phase(segments, length):
    """Position within the codon (0, 1, 2) of every genome base a CDS covers; -1 elsewhere.

    Computed along the joined segments, so genes crossing the origin keep the
    correct phase even though 5386 is not divisible by 3.
    """
    phase = np.full(length, -1)
    offset = 0
    for a, b in segments:
        phase[a:b] = (offset + np.arange(b - a)) % 3
        offset += b - a
    return phase


def shuffle_null(seq, rng):
    rows = []
    letters = np.array(list(seq))
    for i in range(SHUFFLES):
        shuffled = "".join(rng.permutation(letters))
        loci = loci_of(find_orfs(shuffled, min_aa=MIN_AA, circular=True))
        sizes = [c["length_aa"] for c in loci.values()]
        rows.append(
            {
                "shuffle": i + 1,
                "loci": len(sizes),
                "longest_aa": max(sizes, default=0),
                "loci_ge_100aa": sum(s >= LONG_AA for s in sizes),
            }
        )
    return pd.DataFrame(rows)


def main():
    started = time.perf_counter()
    seq, genes = load()
    length = len(seq)
    out = new_run(
        ROOT,
        "phix174-showcase",
        [FASTA, GENBANK],
        {
            "min_aa": MIN_AA,
            "shuffles": SHUFFLES,
            "seed": SEED,
            "match": "strand + stop codon",
        },
    )
    candidates = find_orfs(seq, min_aa=MIN_AA, circular=True)
    loci = loci_of(candidates)

    gene_rows = []
    for g in genes:
        key = stop_key(g["strand"], g["segments0"])
        locus = loci.get(key)
        exact = any(
            c["segments0"] == [tuple(s) for s in g["segments0"]]
            or [list(s) for s in c["segments0"]] == [list(s) for s in g["segments0"]]
            for c in candidates
            if stop_key(c["strand"], c["segments0"]) == key
        )
        gene_rows.append(
            g
            | {
                "locus_found": locus is not None,
                "exact_start_found": exact,
                "longest_candidate_aa": locus["length_aa"] if locus else None,
                "upstream_extension_aa": (locus["length_aa"] - g["length_aa"])
                if locus
                else None,
            }
        )
    gene_keys = {
        stop_key(g["strand"], g["segments0"]): g["gene"]
        for g in genes
        if g["gene"] != "A*"
    }
    locus_rows = []
    for key, c in sorted(loci.items(), key=lambda kv: -kv[1]["length_aa"]):
        locus_rows.append(
            {
                "strand": c["strand"],
                "segments0": c["segments0"],
                "longest_aa": c["length_aa"],
                "starts": c["starts"],
                "wraps_origin": c["wraps_origin"],
                "gene": gene_keys.get(key),
            }
        )
    loci_df = pd.DataFrame(locus_rows)

    curve = []
    for t in range(MIN_AA, 531, 5):
        kept = loci_df[loci_df["longest_aa"] >= t]
        hits = kept["gene"].notna().sum()
        curve.append(
            {
                "min_aa": t,
                "loci": int(len(kept)),
                "gene_loci": int(hits),
                "precision": round(hits / len(kept), 4) if len(kept) else None,
                "recall": round(hits / len(gene_keys), 4),
            }
        )

    null = shuffle_null(seq, np.random.default_rng(SEED))
    real_long = int((loci_df["longest_aa"] >= LONG_AA).sum())
    real_longest = int(loci_df["longest_aa"].max())
    p_long = (1 + int((null["loci_ge_100aa"] >= real_long).sum())) / (SHUFFLES + 1)
    p_longest = (1 + int((null["longest_aa"] >= real_longest).sum())) / (SHUFFLES + 1)

    overlaps = []
    phases = {g["gene"]: codon_phase(g["segments0"], length) for g in genes}
    named = [g for g in genes if g["gene"] != "A*"]
    for i, a in enumerate(named):
        for b in named[i + 1 :]:
            pa, pb = phases[a["gene"]], phases[b["gene"]]
            both = (pa >= 0) & (pb >= 0)
            if both.any():
                shift = np.unique((pa[both] - pb[both]) % 3)
                if len(shift) != 1:
                    raise ValueError(
                        f"Inconsistent frame shift for {a['gene']}-{b['gene']}"
                    )
                overlaps.append(
                    {
                        "genes": f"{a['gene']}–{b['gene']}",
                        "overlap_nt": int(both.sum()),
                        "frame_shift": int(shift[0]),
                        "same_frame": bool(shift[0] == 0),
                    }
                )
    coding = np.any([phases[g["gene"]] >= 0 for g in named], axis=0)

    pd.DataFrame(gene_rows).to_csv(
        out / "gene_recovery.csv", index=False, lineterminator="\n"
    )
    loci_df.to_csv(out / "orf_loci.csv", index=False, lineterminator="\n")
    pd.DataFrame(curve).to_csv(
        out / "threshold_curve.csv", index=False, lineterminator="\n"
    )
    null.to_csv(out / "shuffle_null.csv", index=False, lineterminator="\n")

    colors = {"+": "#2f6db5", "-": "#b8344f"}
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "polar"})
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    to_theta = lambda x: 2 * np.pi * x / length  # noqa: E731
    for g in named:
        for a, b in g["segments0"]:
            ax.barh(
                1.0 + 0.12 * g["start_frame"],
                to_theta(b - a),
                left=to_theta(a),
                height=0.1,
                color="#3a9a5b",
            )
        mid = g["segments0"][0][0]
        ax.text(
            to_theta(mid),
            1.45,
            g["gene"],
            ha="center",
            va="center",
            fontsize=11,
            weight="bold",
        )
    for r in locus_rows:
        for a, b in r["segments0"]:
            ax.barh(
                0.6 if r["strand"] == "+" else 0.4,
                to_theta(b - a),
                left=to_theta(a),
                height=0.08,
                color=colors[r["strand"]],
                alpha=0.9 if r["gene"] else 0.35,
            )
    ax.set_ylim(0, 1.55)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title("PhiX174: curated genes (outer, by frame) and ORF loci (inner, + / −)")
    fig.savefig(out / "genome_map.png", dpi=160, bbox_inches="tight")
    plt.close(fig)

    cdf = pd.DataFrame(curve)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(cdf["min_aa"], cdf["recall"], color="#3a9a5b", label="recall (gene loci)")
    ax.plot(cdf["min_aa"], cdf["precision"], color="#2f6db5", label="precision")
    ax.set_xlabel("minimum ORF length (aa)")
    ax.set_ylim(0, 1.05)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(out / "threshold_curve.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(
        null["loci_ge_100aa"],
        bins=range(0, max(null["loci_ge_100aa"].max(), real_long) + 2),
        color="#9aa1ab",
        align="left",
        label=f"{SHUFFLES} shuffled genomes",
    )
    ax.axvline(real_long, color="#3a9a5b", lw=3, label=f"real genome: {real_long}")
    ax.set_xlabel(f"ORF loci ≥ {LONG_AA} aa")
    ax.set_ylabel("shuffles")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(out / "shuffle_null.png", dpi=160)
    plt.close(fig)

    t30 = curve[0]
    best = max((c for c in curve if c["recall"] == 1.0), key=lambda c: c["precision"])
    summary = {
        "accession": "NC_001422.1",
        "length_nt": length,
        "gc_fraction": round((seq.count("G") + seq.count("C")) / length, 4),
        "curated_cds": len(genes),
        "curated_gene_loci": len(gene_keys),
        "candidates": len(candidates),
        "loci": len(loci),
        "loci_plus": int((loci_df["strand"] == "+").sum()),
        "loci_minus": int((loci_df["strand"] == "-").sum()),
        "gene_loci_recovered": int(loci_df["gene"].notna().sum()),
        "exact_starts_recovered": int(sum(r["exact_start_found"] for r in gene_rows)),
        "upstream_start_genes": [
            r["gene"] for r in gene_rows if r["upstream_extension_aa"]
        ],
        "precision_at_30aa": t30["precision"],
        "best_threshold_full_recall": best,
        "coding_fraction": round(float(coding.mean()), 4),
        "overlapping_pairs": len(overlaps),
        "overlapping_pairs_other_frame": sum(not o["same_frame"] for o in overlaps),
        "null": {
            "shuffles": SHUFFLES,
            "real_loci_ge_100aa": real_long,
            "null_mean_loci_ge_100aa": round(float(null["loci_ge_100aa"].mean()), 3),
            "null_max_loci_ge_100aa": int(null["loci_ge_100aa"].max()),
            "p_loci_ge_100aa": round(p_long, 4),
            "real_longest_aa": real_longest,
            "null_mean_longest_aa": round(float(null["longest_aa"].mean()), 1),
            "null_max_longest_aa": int(null["longest_aa"].max()),
            "p_longest": round(p_longest, 4),
        },
        "limitations": [
            "Matching uses strand and stop codon; the scan reports every in-frame ATG, so start choice is evaluated separately.",
            "Mononucleotide shuffles keep composition but not codon or dinucleotide structure.",
            "One small, gene-dense phage genome; precision here does not transfer to larger genomes.",
            "Curated CDS are the reference; non-ATG starts or unannotated genes would count as errors.",
        ],
    }
    write_json(out / "summary.json", summary)
    write_json(
        out / "presentation_data.json",
        {
            "sequence": seq,
            "genes": gene_rows,
            "loci": locus_rows,
            "curve": curve,
            "null": null.to_dict("records"),
            "overlaps": overlaps,
            "summary": summary,
        },
    )
    finish_run(
        out, status="passed", elapsed_seconds=round(time.perf_counter() - started, 2)
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(out)


if __name__ == "__main__":
    main()
