"""Run a predeclared four-class microarray experiment using the supplied split."""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fetch_khan import fetch
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score

from biolab.expression_ml import fit_training_only, load_khan
from biolab.reporting import new_run, write_json

ROOT = Path(__file__).resolve().parents[1]


def main():
    folder = fetch()
    xtrain, xtest, ytrain, ytest = load_khan(folder)
    out = new_run(
        ROOT,
        "gene-expression-ml",
        sorted(folder.glob("*.csv")),
        {
            "seed": 42,
            "k_grid": [25, 100, 500],
            "C_grid": [0.01, 0.1, 1.0],
            "selection": "training-only five-fold balanced accuracy",
            "split": "ISLP published 63 training / 20 test samples",
        },
    )
    search = fit_training_only(xtrain, ytrain)
    model = search.best_estimator_
    prediction = model.predict(xtest)
    dummy = DummyClassifier(strategy="most_frequent").fit(xtrain, ytrain)
    dummy_cv = cross_val_score(
        DummyClassifier(strategy="most_frequent"),
        xtrain,
        ytrain,
        scoring="balanced_accuracy",
        cv=StratifiedKFold(5, shuffle=True, random_state=42),
    )
    summary = {
        "dataset": "Khan et al. (2001), ISLP four-class microarray subset",
        "data_type": "real processed gene-expression microarray values; not raw counts",
        "features": 2308,
        "train_samples": 63,
        "test_samples": 20,
        "train_class_counts": {
            str(k): int(v) for k, v in ytrain.value_counts().sort_index().items()
        },
        "test_class_counts": {
            str(k): int(v) for k, v in ytest.value_counts().sort_index().items()
        },
        "selected_parameters": search.best_params_,
        "selected_cv_balanced_accuracy": float(search.best_score_),
        "dummy_cv_balanced_accuracy": float(dummy_cv.mean()),
        "test_accuracy": float(accuracy_score(ytest, prediction)),
        "test_balanced_accuracy": float(balanced_accuracy_score(ytest, prediction)),
        "test_macro_f1": float(f1_score(ytest, prediction, average="macro")),
        "dummy_test_balanced_accuracy": float(
            balanced_accuracy_score(ytest, dummy.predict(xtest))
        ),
        "class_order": [1, 2, 3, 4],
        "confusion_matrix": confusion_matrix(
            ytest, prediction, labels=[1, 2, 3, 4]
        ).tolist(),
        "limitations": [
            "Twenty held-out tissue samples from a historical benchmark; not early-detection or screening evidence.",
            "Source values were processed before distribution; upstream preprocessing independence cannot be established here.",
            "V1..V2308 are dataset column identifiers, not verified gene symbols.",
            "Cross-validation score is used for model selection and is not an unbiased generalization estimate.",
            "Published test split is not a prospective or external-cohort validation.",
        ],
    }
    # Interval is conditional on the trained model and this small fixed test cohort.
    rng = np.random.default_rng(42)
    correct = np.asarray(ytest) == prediction
    bootstrap = [
        float(rng.choice(correct, len(correct), replace=True).mean())
        for _ in range(2000)
    ]
    summary["test_accuracy_bootstrap_95_conditional"] = np.quantile(
        bootstrap, [0.025, 0.975]
    ).tolist()
    write_json(out / "summary.json", summary)
    pd.DataFrame(search.cv_results_).to_csv(out / "cv_results.csv", index=False)
    pd.DataFrame(
        {
            "sample_id": [f"test_{i + 1:02}" for i in range(len(ytest))],
            "truth": ytest,
            "prediction": prediction,
        }
    ).to_csv(out / "predictions.csv", index=False)
    report = classification_report(
        ytest, prediction, labels=[1, 2, 3, 4], output_dict=True, zero_division=0
    )
    write_json(out / "classification_report.json", report)
    surviving = xtrain.columns[model.named_steps["variance"].get_support()]
    selector = model.named_steps["select"]
    selected = surviving[selector.get_support()]
    pd.DataFrame(
        {
            "probe_column": selected,
            "training_anova_score": selector.scores_[selector.get_support()],
        }
    ).to_csv(out / "selected_probes.csv", index=False)
    fig, ax = plt.subplots(figsize=(6, 5))
    ConfusionMatrixDisplay.from_predictions(
        ytest, prediction, labels=[1, 2, 3, 4], cmap="Blues", ax=ax, colorbar=False
    )
    ax.set_title("Khan microarray: published test split (n=20)")
    fig.tight_layout()
    fig.savefig(out / "confusion_matrix.png", dpi=150)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(
        ["Dummy CV", "Selected SVM CV", "SVM test"],
        [
            summary["dummy_cv_balanced_accuracy"],
            summary["selected_cv_balanced_accuracy"],
            summary["test_balanced_accuracy"],
        ],
        color=["#a1abb2", "#2c7c88", "#ac5a44"],
    )
    ax.set(
        ylim=(0, 1.08),
        ylabel="Balanced accuracy",
        title="Training selection and held-out evaluation",
    )
    fig.tight_layout()
    fig.savefig(out / "comparison.png", dpi=150)
    plt.close(fig)
    print(out)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
