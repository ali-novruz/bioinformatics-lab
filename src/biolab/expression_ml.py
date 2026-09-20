"""High-dimensional gene-expression classification with training-only selection."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike
from sklearn.feature_selection import SelectKBest, VarianceThreshold, f_classif
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC


def load_khan(folder: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    xtrain = pd.read_csv(folder / "Khan_xtrain.csv")
    xtest = pd.read_csv(folder / "Khan_xtest.csv")
    ytrain = pd.read_csv(folder / "Khan_ytrain.csv")["x"]
    ytest = pd.read_csv(folder / "Khan_ytest.csv")["x"]
    if xtrain.shape != (63, 2308) or xtest.shape != (20, 2308):
        raise ValueError("Unexpected Khan ISLP dataset dimensions")
    if list(xtrain.columns) != list(xtest.columns) or xtrain.columns.has_duplicates:
        raise ValueError("Probe columns do not align")
    for x, y in [(xtrain, ytrain), (xtest, ytest)]:
        if len(x) != len(y) or set(y) != {1, 2, 3, 4}:
            raise ValueError("Invalid sample labels")
        if not np.isfinite(x.to_numpy()).all():
            raise ValueError("Finite processed microarray values required")
    return xtrain, xtest, ytrain, ytest


def expression_pipeline(k: int = 100, c: float = 1.0, seed: int = 42) -> Pipeline:
    return Pipeline(
        [
            ("variance", VarianceThreshold()),
            ("select", SelectKBest(f_classif, k=k)),
            ("scale", StandardScaler()),
            (
                "classifier",
                LinearSVC(
                    C=c,
                    class_weight="balanced",
                    dual="auto",
                    max_iter=20000,
                    random_state=seed,
                ),
            ),
        ]
    )


def fit_training_only(
    xtrain: pd.DataFrame, ytrain: ArrayLike, seed: int = 42
) -> GridSearchCV:
    if min(pd.Series(ytrain).value_counts()) < 5:
        raise ValueError(
            "Five-fold CV requires at least five training samples per class"
        )
    if xtrain.shape[1] < 500:
        raise ValueError("This predeclared experiment requires at least 500 probes")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    search = GridSearchCV(
        expression_pipeline(seed=seed),
        {"select__k": [25, 100, 500], "classifier__C": [0.01, 0.1, 1.0]},
        scoring="balanced_accuracy",
        cv=cv,
        refit=True,
        n_jobs=1,
        error_score="raise",
        return_train_score=True,
    )
    search.fit(xtrain, ytrain)
    return search
