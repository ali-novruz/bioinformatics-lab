import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from biolab.counts import combine_feature_counts
from biolab.provenance import verify_outputs
from biolab.registry import load_registry
from biolab.reporting import recorded_run
from biolab.sensitivity import (
    nested_expression_cv,
    permutation_pvalue,
    singleton_enrichment,
)

ROOT = Path(__file__).resolve().parents[1]


def count_inputs(tmp_path, second="g2\tI\t11\t20\t+\t10\t4\ng1\tI\t1\t10\t+\t10\t3\n"):
    header = "Geneid\tChr\tStart\tEnd\tStrand\tLength\tsample.bam\n"
    (tmp_path / "a.tsv").write_text(
        header + "g1\tI\t1\t10\t+\t10\t1\ng2\tI\t11\t20\t+\t10\t2\n"
    )
    (tmp_path / "b.tsv").write_text(header + second)
    samples = tmp_path / "samples.tsv"
    samples.write_text("sample_id\tcounts_path\n001\ta.tsv\n002\tb.tsv\n")
    return samples


def test_counts_align_by_gene_preserve_string_ids(tmp_path):
    result = combine_feature_counts(count_inputs(tmp_path))
    assert result.index.tolist() == ["g1", "g2"]
    assert result.columns.tolist() == ["001", "002"]
    assert result.to_numpy().tolist() == [[1, 3], [2, 4]]


@pytest.mark.parametrize(
    "change", ["coordinate", "fraction", "missing", "duplicate", "overflow"]
)
def test_counts_reject_incompatible_or_invalid_inputs(tmp_path, change):
    source = count_inputs(tmp_path)
    path = tmp_path / "b.tsv"
    text = path.read_text()
    replacements = {
        "coordinate": ("g1\tI\t1", "g1\tII\t1"),
        "fraction": ("\t3\n", "\t3.5\n"),
        "missing": ("\t3\n", "\t\n"),
        "duplicate": ("g2\t", "g1\t"),
        "overflow": ("\t3\n", "\t9223372036854775808\n"),
    }
    path.write_text(text.replace(*replacements[change]))
    with pytest.raises(ValueError):
        combine_feature_counts(source)


def test_singleton_exact_known_answer_and_resolution():
    result = singleton_enrichment(range(100), {"two": {0, 1}}, min_size=2)
    assert result.discoveries.sum() == 2
    assert np.isclose(result.min_padj.min(), 0.02)
    assert permutation_pvalue(0.9, [0.1] * 99) == 0.01
    assert permutation_pvalue(0.9, [0.9] * 99) == 1


def test_nested_cv_known_signal_and_partition_boundaries(monkeypatch):
    from sklearn.feature_selection import SelectKBest

    fitted_rows = []
    original_fit = SelectKBest.fit

    def track_fit(self, x, y):
        fitted_rows.append(set(x[:, -1].astype(int)))
        return original_fit(self, x, y)

    monkeypatch.setattr(SelectKBest, "fit", track_fit)
    rng = np.random.default_rng(7)
    y = np.repeat([0, 1], 20)
    x = rng.normal(size=(40, 8))
    x[:, 0] = y * 20 + rng.normal(0, 0.01, 40)
    x[:, -1] = np.arange(40)
    folds, pred = nested_expression_cv(
        x,
        y,
        outer_folds=4,
        inner_folds=3,
        grid={"select__k": [1, 2], "classifier__C": [0.1]},
    )
    assert pred.sample_index0.tolist() == list(range(40))
    assert (pred.truth == pred.prediction).all()
    # Two candidates x three inner folds + one refit per outer fold.
    assert len(fitted_rows) == 28
    for number, fold in enumerate(folds):
        assert not set(fold["train_indices0"]) & set(fold["validation_indices0"])
        assert 0 in fold["selected_feature_indices0"]
        for fitted in fitted_rows[number * 7 : (number + 1) * 7]:
            assert fitted <= set(fold["train_indices0"])
            assert not fitted & set(fold["validation_indices0"])


def test_failed_run_is_sealed_and_corruption_detected(tmp_path):
    external = tmp_path / "input.txt"
    external.write_text("input")
    root = tmp_path / "repo"
    root.mkdir()
    with pytest.raises(RuntimeError):
        with recorded_run(root, "failure", [external]) as out:
            (out / "partial.txt").write_text("partial")
            raise RuntimeError("expected failure")
    record = json.loads((out / "run.json").read_text())
    assert record["status"] == "failed" and record["elapsed_seconds"] >= 0
    assert record["inputs"][0]["external"]
    assert verify_outputs(out, record) == 1
    (out / "partial.txt").write_text("changed")
    with pytest.raises(ValueError, match="checksum"):
        verify_outputs(out, record)


def test_registry_rejects_duplicate_id(tmp_path):
    (tmp_path / "projects").mkdir()
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts/run.py").write_text("pass")
    (tmp_path / "docs.md").write_text("project")
    p = {
        "id": "valid",
        "title": "Valid",
        "script": "run.py",
        "args": [],
        "offline": True,
        "fetch": [],
        "docs": "docs.md",
    }
    (tmp_path / "projects/registry.json").write_text(json.dumps({"projects": [p, p]}))
    with pytest.raises(ValueError, match="duplicate"):
        load_registry(tmp_path)


def test_cli_unknown_project_and_list():
    listed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/lab.py"), "list"],
        capture_output=True,
        text=True,
    )
    assert listed.returncode == 0 and len(listed.stdout.splitlines()) == 13
    invalid = subprocess.run(
        [sys.executable, str(ROOT / "scripts/lab.py"), "run", "does-not-exist"],
        capture_output=True,
        text=True,
    )
    assert invalid.returncode == 2 and "Unknown project" in invalid.stderr


def test_custom_rna_plot_names_and_design(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location(
        "audit_run_projects", ROOT / "scripts/run_projects.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    from matplotlib.figure import Figure

    titles = []
    monkeypatch.setattr(
        Figure,
        "savefig",
        lambda self, *a, **kw: titles.extend(ax.get_title() for ax in self.axes),
    )
    norm = pd.DataFrame(
        [[1, 3, 5], [3, 7, 2], [7, 1, 9], [9, 2, 4]], index=["a", "b", "c", "d"]
    )
    meta = pd.DataFrame(
        {"condition": ["treated", "treated", "untreated", "untreated"]},
        index=norm.index,
    )
    res = pd.DataFrame({"padj": [0.01, 0.5, 1.0], "log2FoldChange": [2.0, -0.1, 0.0]})
    module.plot_expression(
        res, norm, meta, tmp_path, dataset="Yeast chrI", design="~ condition"
    )
    assert any("Yeast chrI: ~ condition" in title for title in titles)
    assert not any("Pasilla" in title for title in titles)


def test_suite_does_not_mark_a_missing_result_successful(tmp_path, monkeypatch):
    (tmp_path / "scripts").mkdir()
    (tmp_path / "projects").mkdir()
    (tmp_path / "scripts/no_result.py").write_text('print("no result")')
    (tmp_path / "docs.md").write_text("fixture")
    (tmp_path / "projects/registry.json").write_text(
        json.dumps(
            {
                "projects": [
                    {
                        "id": "empty",
                        "title": "Empty",
                        "script": "no_result.py",
                        "args": [],
                        "offline": True,
                        "fetch": [],
                        "docs": "docs.md",
                    }
                ]
            }
        )
    )
    spec = importlib.util.spec_from_file_location("audit_lab", ROOT / "scripts/lab.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(sys, "argv", ["lab.py", "run", "all", "--offline"])
    with pytest.raises(SystemExit) as error:
        module.main()
    assert error.value.code == 1
    report = json.loads(
        next((tmp_path / "results/runs").rglob("suite.json")).read_text()
    )
    assert report["status"] == "failed"
    assert "without recording a run" in report["projects"][0]["error"]


def test_research_graph_rejects_broken_relation(tmp_path):
    import shutil

    from biolab.health import check_health

    for folder in ["projects", "datasets/examples", "research"]:
        shutil.copytree(ROOT / folder, tmp_path / folder)
    shutil.copytree(ROOT / "scripts", tmp_path / "scripts")
    graph = {
        "nodes": [{"id": "a", "status": "protocol", "path": "projects/README.md"}],
        "edges": [{"from": "missing", "to": "a", "relation": "invalid"}],
    }
    (tmp_path / "research/graph.json").write_text(json.dumps(graph))
    with pytest.raises(ValueError, match="endpoints"):
        check_health(tmp_path)
