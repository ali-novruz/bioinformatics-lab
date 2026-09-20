"""Run the offline regional genetics evidence-triage lesson."""

import json
from pathlib import Path

import matplotlib.pyplot as plt

from biolab.clinical import prioritize_clinvar
from biolab.reporting import recorded_run

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "datasets/examples/regional/clinvar-2026-09-20.tsv"


def main() -> None:
    with recorded_run(
        ROOT, "regional-variants", [SOURCE], {"mode": "educational-triage"}
    ) as out:
        table, summary = prioritize_clinvar(SOURCE)
        table.to_csv(out / "prioritized_variants.csv", index=False)
        (out / "summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        figure, axis = plt.subplots(figsize=(7, 3.5))
        axis.bar(table["gene"], table["priority_score"], color=["#087F83", "#79DEC5"])
        axis.set(
            ylabel="Şəffaf evidence-triage balı",
            title="ClinVar nümunələri: klinik təsnifat deyil",
        )
        axis.spines[["top", "right"]].set_visible(False)
        figure.tight_layout()
        figure.savefig(out / "priorities.png", dpi=160)
        plt.close(figure)


if __name__ == "__main__":
    main()
