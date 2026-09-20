"""Controls for existing analyses; no reuse of the published test cohort."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike
from scipy.stats import hypergeom
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import GridSearchCV, StratifiedKFold

from .expression_ml import expression_pipeline


def singleton_enrichment(
    universe: Iterable[Any],
    gene_sets: Mapping[str, Iterable[Any]],
    alpha: float = 0.05,
    min_size: int = 2,
) -> pd.DataFrame:
    """Enumerate every size-one foreground, with the same term family and BH rule."""
    if not 0 < alpha < 1:
        raise ValueError("alpha must be between zero and one")
    universe = set(universe)
    if not universe:
        raise ValueError("Nonempty universe required")
    if min_size < 1:
        raise ValueError("min_size must be positive")
    members = [set(v) & universe for _, v in sorted(gene_sets.items())]
    members = [v for v in members if min_size <= len(v) < len(universe)]
    if not members:
        raise ValueError("No eligible terms")
    genes = sorted(universe)
    sizes = np.array([len(v) for v in members])
    rows = []
    for begin in range(0, len(genes), 1024):
        block = genes[begin : begin + 1024]
        overlap = np.array([[g in v for v in members] for g in block], dtype=int)
        pvalues = hypergeom.sf(overlap - 1, len(universe), sizes, 1)
        ordered = np.sort(pvalues, axis=1)
        adjusted = np.minimum.accumulate(
            (ordered * len(members) / np.arange(1, len(members) + 1))[:, ::-1], axis=1
        )[:, ::-1]
        adjusted = np.minimum(adjusted, 1)
        for i, gene in enumerate(block):
            rows.append(
                {
                    "gene_id": gene,
                    "min_pvalue": float(ordered[i, 0]),
                    "min_padj": float(adjusted[i, 0]),
                    "discoveries": int((adjusted[i] < alpha).sum()),
                    "tested_terms": len(members),
                }
            )
    return pd.DataFrame(rows)


def nested_expression_cv(
    x: ArrayLike,
    y: ArrayLike,
    *,
    seed: int = 42,
    outer_folds: int = 5,
    inner_folds: int = 3,
    grid: dict[str, list[Any]] | None = None,
) -> tuple[list[dict[str, Any]], pd.DataFrame]:
    """Return outer-fold scores and out-of-fold predictions with full inner selection."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y)
    if x.ndim != 2 or y.ndim != 1 or len(x) != len(y) or not np.isfinite(x).all():
        raise ValueError("Finite 2-D features and paired 1-D labels required")
    if (
        len(np.unique(y)) < 2
        or outer_folds < 2
        or inner_folds < 2
        or pd.Series(y).value_counts().min() < outer_folds
    ):
        raise ValueError("Enough samples per class for stratified outer CV required")
    grid = grid or {"select__k": [25, 100, 500], "classifier__C": [0.01, 0.1, 1.0]}
    splitter = StratifiedKFold(outer_folds, shuffle=True, random_state=seed)
    rows = []
    predictions = []
    for fold, (train, test) in enumerate(splitter.split(x, y), 1):
        if pd.Series(y[train]).value_counts().min() < inner_folds:
            raise ValueError("Too few training samples per class for inner CV")
        search = GridSearchCV(
            expression_pipeline(seed=seed),
            grid,
            scoring="balanced_accuracy",
            n_jobs=1,
            error_score="raise",
            cv=StratifiedKFold(inner_folds, shuffle=True, random_state=seed),
        )
        search.fit(x[train], y[train])
        predicted = search.predict(x[test])
        model = search.best_estimator_
        surviving = np.flatnonzero(model.named_steps["variance"].get_support())
        selected = surviving[model.named_steps["select"].get_support()]
        rows.append(
            {
                "fold": fold,
                "train_n": len(train),
                "validation_n": len(test),
                "inner_selected_score": float(search.best_score_),
                "balanced_accuracy": float(balanced_accuracy_score(y[test], predicted)),
                "parameters": search.best_params_,
                "selected_feature_indices0": selected.tolist(),
                "train_indices0": train.tolist(),
                "validation_indices0": test.tolist(),
            }
        )
        predictions.extend(
            {
                "sample_index0": int(i),
                "fold": fold,
                "truth": int(truth),
                "prediction": int(pred),
            }
            for i, truth, pred in zip(test, y[test], predicted, strict=True)
        )
    return rows, pd.DataFrame(predictions).sort_values("sample_index0")


def permutation_pvalue(observed: float, null_scores: ArrayLike) -> float:
    null = np.asarray(null_scores, dtype=float)
    if (
        null.ndim != 1
        or not len(null)
        or not np.isfinite(null).all()
        or not np.isfinite(observed)
    ):
        raise ValueError(
            "Finite observed score and nonempty finite null scores required"
        )
    # Include the observed arrangement; Monte Carlo p is never reported as zero.
    return float((1 + np.count_nonzero(null >= observed)) / (1 + len(null)))
