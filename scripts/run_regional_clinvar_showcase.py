"""Read every ClinVar record of MEFV and HBB as evidence, not as a diagnosis.

Builds on the two-record regional triage with the full gene snapshots:
- which records belong to the gene (LOC regulatory elements ignored; large
  multi-gene CNVs and haplotypes set aside);
- how classifications and review strength differ between the two genes;
- where classified protein changes fall on UniProt domains, and whether
  pathogenic MEFV missense changes concentrate in B30.2/SPRY beyond what the
  sequencing focus on exon 10 already explains (label permutation null);
- where population frequency and classification pull in different directions.

No prevalence, carrier-risk or diagnostic claim is made.
"""

import json
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from biolab.clinvar import (
    assigned_gene,
    classification_group,
    protein_consequence,
    review_stars,
)
from biolab.reporting import finish_run, new_run, write_json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets/examples/regional"
SNAPSHOT = DATA / "clinvar-mefv-hbb-2026-11-24.tsv.gz"
UNIPROT = DATA / "uniprot-mefv-hbb-2026-11-24.json"
# Canonical RefSeq transcripts; any version of the same accession is accepted because
# HGVS c./p. positions are anchored to the coding start (older versions are counted).
TRANSCRIPT = {"MEFV": "NM_000243", "HBB": "NM_000518"}
CURRENT = {"MEFV": "NM_000243.3", "HBB": "NM_000518.5"}
SMALL = {
    "single nucleotide variant",
    "Deletion",
    "Duplication",
    "Insertion",
    "Indel",
    "Microsatellite",
}
PERMUTATIONS = 10000
SEED = 11
FREQ_TENSION = 0.005
GROUP_ORDER = ["P/LP", "Conflicting", "VUS", "B/LB", "Other"]
COLORS = {
    "P/LP": "#b8344f",
    "Conflicting": "#d9822b",
    "VUS": "#7c8696",
    "B/LB": "#2f6db5",
    "Other": "#c9ccd2",
}
# Teaching set: variants that clinical genetics courses commonly use for these genes.
# Matched on the canonical-transcript HGVS in the record title; ClinVar fields are reported as found.
TEACHING = {
    "MEFV": ["c.2080A>G", "c.2040G>C", "c.2082G>A", "c.2177T>C", "c.442G>C"],
    "HBB": ["c.20A>T", "c.79G>A", "c.118C>T", "c.93-21G>A", "c.92+1G>A", "c.92+6T>C"],
}


def load():
    table = pd.read_csv(SNAPSHOT, sep="\t", dtype=str, keep_default_na=False)
    if table["variation_id"].duplicated().any():
        raise ValueError("Duplicate ClinVar variation ids in snapshot")
    table["gene"] = table["genes"].map(assigned_gene)
    germline = table["review_status"] != ""
    table["in_scope"] = (
        (table["gene"] == table["gene_query"])
        & table["obj_type"].isin(SMALL)
        & germline
    )
    scoped = table[table["in_scope"]].copy()
    on_transcript = scoped.apply(
        lambda r: r["title"].startswith(TRANSCRIPT[r["gene"]] + "."), axis=1
    )
    scoped = scoped[on_transcript].copy()
    parsed = scoped["title"].map(protein_consequence)
    scoped["consequence"] = parsed.map(lambda p: p[0])
    scoped["position"] = parsed.map(lambda p: p[1]).astype("Int64")
    scoped["change"] = parsed.map(lambda p: p[2])
    scoped["group"] = scoped["classification"].map(classification_group)
    scoped["stars"] = scoped["review_status"].map(review_stars)
    scoped["af"] = pd.to_numeric(scoped["gnomad_af_max"].replace("", np.nan))
    older = scoped.apply(
        lambda r: not r["title"].startswith(CURRENT[r["gene"]]), axis=1
    )
    excluded = {
        "multi_gene_or_cnv": int((table["gene"] != table["gene_query"]).sum()),
        "haplotype_or_complex": int(
            (
                (table["gene"] == table["gene_query"]) & ~table["obj_type"].isin(SMALL)
            ).sum()
        ),
        "no_germline_classification": int(
            (
                (table["gene"] == table["gene_query"])
                & table["obj_type"].isin(SMALL)
                & ~germline
            ).sum()
        ),
        "genomic_or_other_description": int((~on_transcript).sum()),
    }
    excluded["kept_on_older_transcript_version"] = int(older.sum())
    return table, scoped, excluded


def domains():
    raw = json.loads(UNIPROT.read_text(encoding="utf-8"))
    keep = {"Domain", "Zinc finger", "Coiled coil"}
    return {
        g: {
            "length": v["length"],
            "accession": v["accession"],
            "domains": [f for f in v["features"] if f["type"] in keep],
        }
        for g, v in raw.items()
    }


def hotspot(mefv, rng):
    """B30.2/SPRY (UniProt 580-775) share of P/LP missense versus two nulls."""
    start, end = 580, 775
    missense = mefv[
        (mefv["consequence"] == "missense")
        & mefv["group"].isin(["P/LP", "VUS", "B/LB"])
    ]
    inside = missense["position"].between(start, end).to_numpy()
    plp = (missense["group"] == "P/LP").to_numpy()
    observed = inside[plp].mean()
    null = np.array([inside[rng.permutation(plp)].mean() for _ in range(PERMUTATIONS)])
    p_label = (1 + (null >= observed).sum()) / (PERMUTATIONS + 1)
    length_share = (end - start + 1) / 781
    from scipy.stats import binomtest

    p_uniform = binomtest(
        int(inside[plp].sum()), int(plp.sum()), length_share, alternative="greater"
    ).pvalue
    return {
        "domain": "B30.2/SPRY 580-775",
        "plp_missense": int(plp.sum()),
        "plp_in_domain": int(inside[plp].sum()),
        "plp_share": round(float(observed), 4),
        "all_classified_missense": int(len(missense)),
        "all_missense_share": round(float(inside.mean()), 4),
        "domain_length_share": round(length_share, 4),
        "p_uniform_binomial": float(f"{p_uniform:.3g}"),
        "permutations": PERMUTATIONS,
        "null_mean_share": round(float(null.mean()), 4),
        "null_q95_share": round(float(np.quantile(null, 0.95)), 4),
        "p_label_permutation": round(float(p_label), 5),
    }, null


def main():
    started = time.perf_counter()
    table, scoped, excluded = load()
    dom = domains()
    out = new_run(
        ROOT,
        "regional-clinvar-showcase",
        [SNAPSHOT, UNIPROT],
        {"permutations": PERMUTATIONS, "seed": SEED, "frequency_tension": FREQ_TENSION},
    )
    rng = np.random.default_rng(SEED)

    composition = (
        scoped.groupby(["gene", "group"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=GROUP_ORDER, fill_value=0)
    )
    stars = scoped.groupby(["gene", "stars"]).size().unstack(fill_value=0)
    plp = scoped[scoped["group"] == "P/LP"]
    strength = {
        g: {
            "plp": int(len(d)),
            "plp_2plus_stars": int((d["stars"] >= 2).sum()),
            "plp_expert_panel": int((d["stars"] >= 3).sum()),
        }
        for g, d in plp.groupby("gene")
    }
    consequences = scoped.groupby(["gene", "consequence"]).size().unstack(fill_value=0)

    hot, null = hotspot(scoped[scoped["gene"] == "MEFV"], rng)

    tension = scoped[(scoped["group"] == "P/LP") & (scoped["af"] > FREQ_TENSION)]
    common_conflicts = scoped[(scoped["group"] == "Conflicting")].nlargest(5, "af")
    teaching_rows = []
    for gene, terms in TEACHING.items():
        for term in terms:
            hit = scoped[
                (scoped["gene"] == gene)
                & scoped["title"].str.contains(f":{term}", regex=False)
                & ~scoped["title"].str.contains(f":{term}[0-9]", regex=True)
            ]
            if len(hit) != 1:
                raise ValueError(
                    f"{gene} {term}: expected one record, found {len(hit)}"
                )
            r = hit.iloc[0]
            teaching_rows.append(
                {
                    "gene": gene,
                    "hgvs_c": term,
                    "change": r["change"] or term,
                    "variation_id": r["variation_id"],
                    "classification": r["classification"],
                    "group": r["group"],
                    "stars": int(r["stars"]),
                    "review_status": r["review_status"],
                    "gnomad_af_max": None if pd.isna(r["af"]) else float(r["af"]),
                    "traits": r["traits"],
                }
            )
    teaching = pd.DataFrame(teaching_rows)

    cols = [
        "variation_id",
        "gene",
        "change",
        "consequence",
        "position",
        "classification",
        "group",
        "review_status",
        "stars",
        "af",
        "traits",
    ]
    scoped[cols].to_csv(out / "records_in_scope.csv", index=False, lineterminator="\n")
    composition.to_csv(out / "composition.csv", lineterminator="\n")
    teaching.to_csv(out / "teaching_variants.csv", index=False, lineterminator="\n")
    tension[cols].to_csv(
        out / "frequency_tension.csv", index=False, lineterminator="\n"
    )
    pd.DataFrame({"plp_share_in_b302": null}).to_csv(
        out / "hotspot_null.csv", index=False, lineterminator="\n"
    )

    # Lollipop maps.
    fig, axes = plt.subplots(
        2, 1, figsize=(12, 6.5), gridspec_kw={"height_ratios": [1.3, 1]}
    )
    for ax, gene in zip(axes, ["MEFV", "HBB"], strict=True):
        d = scoped[
            (scoped["gene"] == gene)
            & scoped["position"].notna()
            & (scoped["consequence"] != "synonymous")
        ]
        length = dom[gene]["length"]
        ax.add_patch(plt.Rectangle((1, -0.25), length, 0.5, color="#e6e8ec"))
        for f in dom[gene]["domains"]:
            ax.add_patch(
                plt.Rectangle(
                    (f["start"], -0.3), f["end"] - f["start"] + 1, 0.6, color="#9aa1ab"
                )
            )
            ax.text(
                (f["start"] + f["end"]) / 2,
                0,
                f["description"] or f["type"],
                ha="center",
                va="center",
                fontsize=8,
            )
        for group in reversed(GROUP_ORDER):
            g = d[d["group"] == group]
            counts = g.groupby("position").size()
            ax.vlines(
                counts.index,
                0.35,
                0.35 + np.log1p(counts.values),
                color=COLORS[group],
                lw=0.6,
                alpha=0.6,
            )
            ax.scatter(
                counts.index,
                0.35 + np.log1p(counts.values),
                s=10,
                color=COLORS[group],
                label=group,
                zorder=3,
            )
        ax.set_xlim(0, length + 5)
        ax.set_yticks([])
        ax.set_title(
            f"{gene} ({dom[gene]['accession']}, {length} aa): ClinVar protein changes by classification"
        )
    axes[0].legend(frameon=False, ncol=5, fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(out / "lollipop.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(null, bins=40, color="#9aa1ab")
    ax.axvline(
        hot["plp_share"],
        color="#b8344f",
        lw=3,
        label=f"P/LP observed {hot['plp_share']:.2f}",
    )
    ax.axvline(
        hot["domain_length_share"],
        color="black",
        ls="--",
        lw=1,
        label=f"domain length share {hot['domain_length_share']:.2f}",
    )
    ax.set_xlabel("share of P/LP missense inside B30.2/SPRY (label permutation null)")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(out / "hotspot_null.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.2))
    for i, group in enumerate(GROUP_ORDER[:4]):
        vals = scoped[(scoped["group"] == group) & scoped["af"].notna()]["af"]
        ax.scatter(
            np.log10(vals.clip(lower=1e-6)),
            np.full(len(vals), i) + rng.uniform(-0.25, 0.25, len(vals)),
            s=8,
            color=COLORS[group],
            alpha=0.6,
        )
    ax.axvline(np.log10(FREQ_TENSION), color="black", ls="--", lw=1)
    ax.set_yticks(range(4), GROUP_ORDER[:4])
    ax.set_xlabel("log10 highest gnomAD allele frequency shown by ClinVar")
    fig.tight_layout()
    fig.savefig(out / "frequency_by_class.png", dpi=160)
    plt.close(fig)

    summary = {
        "snapshot": SNAPSHOT.name,
        "records_total": int(len(table)),
        "records_by_query": table["gene_query"].value_counts().to_dict(),
        "excluded": excluded,
        "in_scope": scoped["gene"].value_counts().to_dict(),
        "composition": {g: row.to_dict() for g, row in composition.iterrows()},
        "review_stars": {
            g: {int(k): int(v) for k, v in row.items()} for g, row in stars.iterrows()
        },
        "plp_strength": strength,
        "consequences": {
            g: {k: int(v) for k, v in row.items() if v}
            for g, row in consequences.iterrows()
        },
        "hotspot_mefv": hot,
        "frequency_tension": {
            "threshold": FREQ_TENSION,
            "plp_above": [
                {
                    "gene": r.gene,
                    "change": r.change or r.variation_id,
                    "af": float(r.af),
                    "stars": int(r.stars),
                }
                for r in tension.itertuples()
            ],
            "most_common_conflicting": [
                {"gene": r.gene, "change": r.change, "af": float(r.af)}
                for r in common_conflicts.itertuples()
                if not pd.isna(r.af)
            ],
        },
        "teaching_variants": teaching_rows,
        "clinical_use": False,
        "regional_prevalence_claim": False,
        "limitations": [
            "ClinVar aggregates submitter assertions; classifications change weekly and are not ACMG calls made here.",
            "gnomAD values are the highest frequency ClinVar displays for the record, without ancestry breakdown.",
            "Submission is ascertainment-biased (exon 10 of MEFV is sequenced most); the permutation null addresses only part of it.",
            "Teaching variants are reported as found in ClinVar; no prevalence, carrier risk or diagnosis is implied.",
        ],
    }
    write_json(out / "summary.json", summary)

    lolli = {}
    for gene in ["MEFV", "HBB"]:
        d = scoped[
            (scoped["gene"] == gene)
            & scoped["position"].notna()
            & (scoped["consequence"] != "synonymous")
        ]
        lolli[gene] = [
            {
                "pos": int(r.position),
                "change": r.change,
                "group": r.group,
                "stars": int(r.stars),
                "consequence": r.consequence,
                "af": None if pd.isna(r.af) else float(r.af),
                "id": r.variation_id,
            }
            for r in d.itertuples()
        ]
    write_json(
        out / "presentation_data.json",
        {
            "domains": dom,
            "lollipop": lolli,
            "af_by_group": {
                g: scoped[(scoped["group"] == g) & scoped["af"].notna()]["af"]
                .round(6)
                .tolist()
                for g in GROUP_ORDER[:4]
            },
            "hotspot_null": np.round(null[:2000], 4).tolist(),
            "summary": summary,
        },
    )
    finish_run(
        out, status="passed", elapsed_seconds=round(time.perf_counter() - started, 2)
    )
    print(
        json.dumps(
            {
                k: summary[k]
                for k in [
                    "in_scope",
                    "excluded",
                    "composition",
                    "plp_strength",
                    "hotspot_mefv",
                    "frequency_tension",
                ]
            },
            indent=1,
            ensure_ascii=False,
        )
    )
    print(out)


if __name__ == "__main__":
    main()
