import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "datasets/annotations"


def test_khan_class_map_is_one_to_one_and_matches_published_counts():
    report = json.loads((FOLDER / "khan_annotation_verification.json").read_text())
    assert report["class_map"] == {"1": "BL", "2": "EWS", "3": "NB", "4": "RMS"}
    for split in ["train", "test"]:
        rows = report["splits"][split]["srbct_rows"]
        assert len(rows) == len(set(rows)) == report["splits"][split]["samples"]
        assert report["splits"][split]["min_sample_correlation"] >= 0.999


def test_khan_probe_annotation_follows_column_order():
    annotation = pd.read_csv(FOLDER / "khan_probe_annotation.csv")
    assert list(annotation["probe_column"]) == [f"V{i}" for i in range(1, 2309)]
    assert annotation["alignment_correlation"].min() >= 0.99
    markers = annotation.set_index("probe_column")["description"]
    assert markers["V1955"] == "fibroblast growth factor receptor 4"
    assert markers["V545"].startswith(
        "antigen identified by monoclonal antibodies 12E7"
    )


def test_showcase_results_name_the_single_test_error():
    summary = json.loads(
        (ROOT / "results/showcase/khan-classifier/summary.json").read_text()
    )
    assert summary["test_accuracy"] == 0.95
    assert summary["misclassified"] == [
        {"sample_id": "test_15", "truth": "EWS", "prediction": "RMS"}
    ]
    assert summary["leakage"]["leaky_mean"] > summary["leakage"]["inside_cv_mean"] + 0.2
