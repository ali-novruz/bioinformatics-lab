"""Multiple testing and held-out AUROC uncertainty."""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import ArrayLike, NDArray
from sklearn.metrics import roc_auc_score


def benjamini_hochberg(pvalues: ArrayLike) -> NDArray[np.float64]:
    p = np.asarray(pvalues, dtype=float)
    if p.ndim != 1 or not np.isfinite(p).all() or ((p < 0) | (p > 1)).any():
        raise ValueError("Expected a finite one-dimensional array of p-values in [0,1]")
    if not len(p):
        return p.copy()
    order = np.argsort(p, kind="stable")
    adjusted = np.minimum.accumulate(
        (p[order] * len(p) / np.arange(1, len(p) + 1))[::-1]
    )[::-1]
    out = np.empty_like(p)
    out[order] = np.minimum(adjusted, 1)
    return out


def bootstrap_auc(
    y: ArrayLike,
    probability: ArrayLike,
    repeats: int = 1000,
    seed: int = 42,
    *,
    stratified: bool = True,
) -> dict[str, Any]:
    """Percentile CI for a fixed model; stratified draws preserve class counts.

    stratified=False reproduces the historical ordinary bootstrap conditioned
    on both classes being present. Neither method refits the model.
    """
    y = np.asarray(y)
    probability = np.asarray(probability)
    if (
        y.ndim != 1
        or y.shape != probability.shape
        or len(np.unique(y)) != 2
        or not np.isfinite(probability).all()
    ):
        raise ValueError("Binary labels and finite paired probabilities required")
    if repeats < 20:
        raise ValueError("At least 20 bootstrap replicates required")
    rng = np.random.default_rng(seed)
    values = []
    groups = [np.flatnonzero(y == label) for label in np.unique(y)]
    for _ in range(repeats):
        idx = (
            np.concatenate([rng.choice(g, size=len(g), replace=True) for g in groups])
            if stratified
            else rng.integers(0, len(y), len(y))
        )
        if len(np.unique(y[idx])) == 2:
            values.append(roc_auc_score(y[idx], probability[idx]))
    if not values:
        raise ValueError("No valid bootstrap samples")
    lo, hi = np.quantile(values, [0.025, 0.975])
    return {
        "low": float(lo),
        "high": float(hi),
        "valid_replicates": len(values),
        "requested_replicates": repeats,
        "method": "stratified percentile"
        if stratified
        else "ordinary percentile, conditioned on both classes",
        "scope": "fixed fitted model, held-out samples only",
    }
