"""Live classroom demo: train, test and stress-test the Khan classifier in the browser.

Runs a local server (stdlib only) that streams every step to a visual page:
the 9 x 5 cross-validation grid fills fold by fold, the 20 held-out samples are
opened one at a time, and the shuffled-label leakage experiment runs live.
The protocol mirrors fit_training_only and run_khan_showcase.py exactly, so the
numbers on screen match the stored results.

    python scripts/khan_live_demo.py            # opens http://127.0.0.1:8765
"""

import json
import sys
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import numpy as np
import pandas as pd
from fetch_khan import fetch
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

from biolab.expression_ml import expression_pipeline, load_khan

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "projects/showcase/khan-gene-expression-classifier/live/index.html"
ANNOTATION = ROOT / "datasets/annotations"
PORT = 8765
SEED = 42
K_GRID = [25, 100, 500]
C_GRID = [0.01, 0.1, 1.0]
ORDER = ["BL", "EWS", "NB", "RMS"]
# Hand-checked symbols for the 2001 descriptions of the probes the model selects.
SYMBOLS = {
    "V1955": "FGFR4",
    "V545": "CD99",
    "V1389": "FCGRT",
    "V246": "CAV1",
    "V187": "IGF2",
    "V509": "IGF2",
    "V1003": "SGCA",
    "V1": "CTNNA1",
    "V174": "NF2",
    "V107": "GAS1",
    "V1319": "PTPN13",
    "V842": "CSDA",
    "V1708": "GYG2",
    "V851": "ALDH7A1",
    "V1954": "FVT1",
    "V1066": "PFN2",
    "V1427": "GSTA4",
    "V1645": "OLFM1",
}


class Lab:
    """Holds the data and whatever the audience has run so far."""

    def __init__(self):
        xtrain, xtest, ytrain, ytest = load_khan(fetch())
        verification = json.loads(
            (ANNOTATION / "khan_annotation_verification.json").read_text()
        )
        names = {int(k): v for k, v in verification["class_map"].items()}
        self.annotation = pd.read_csv(ANNOTATION / "khan_probe_annotation.csv")
        if list(self.annotation["probe_column"]) != list(xtrain.columns):
            raise ValueError("Annotation does not follow the probe column order")
        self.xtrain, self.xtest = xtrain, xtest
        self.ytrain, self.ytest = ytrain.map(names), ytest.map(names)
        self.model = None
        self.params = None
        self.lock = threading.Lock()

    def summary(self):
        return {
            "train": list(self.xtrain.shape),
            "test": list(self.xtest.shape),
            "train_counts": self.ytrain.value_counts().reindex(ORDER).tolist(),
            "test_counts": self.ytest.value_counts().reindex(ORDER).tolist(),
            "classes": ORDER,
            "trained": self.model is not None,
        }

    def train(self, emit):
        """Grid search with the same folds, grid order and tie-break as GridSearchCV."""
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
        folds = list(cv.split(self.xtrain, self.ytrain))
        results = []
        for c in C_GRID:
            for k in K_GRID:
                scores = []
                for f, (tr, va) in enumerate(folds):
                    t0 = time.perf_counter()
                    pipe = expression_pipeline(k=k, c=c, seed=SEED)
                    pipe.fit(self.xtrain.iloc[tr], self.ytrain.iloc[tr])
                    score = balanced_accuracy_score(
                        self.ytrain.iloc[va], pipe.predict(self.xtrain.iloc[va])
                    )
                    scores.append(score)
                    emit(
                        "fold",
                        {
                            "k": k,
                            "C": c,
                            "fold": f,
                            "score": round(score, 4),
                            "ms": round((time.perf_counter() - t0) * 1000),
                        },
                    )
                    time.sleep(0.07)
                results.append(
                    {"k": k, "C": c, "mean": round(float(np.mean(scores)), 4)}
                )
                emit("cell", results[-1])
        best = max(results, key=lambda r: r["mean"])  # first maximum, as GridSearchCV
        self.params = best
        self.model = expression_pipeline(k=best["k"], c=best["C"], seed=SEED)
        self.model.fit(self.xtrain, self.ytrain)
        emit("best", {**best, "ties": sum(r["mean"] == best["mean"] for r in results)})
        emit("genes", self.genes())
        emit("pca", self.pca())

    def selected(self):
        kept = self.model.named_steps["variance"].get_support(indices=True)
        sel = self.model.named_steps["select"]
        idx = kept[sel.get_support(indices=True)]
        return idx, sel.scores_[sel.get_support(indices=True)]

    def genes(self):
        idx, scores = self.selected()
        block = self.xtrain.iloc[:, idx]
        means = block.groupby(self.ytrain.to_numpy()).mean()
        rows = []
        for j, f in zip(idx, scores, strict=True):
            probe = self.xtrain.columns[j]
            desc = self.annotation.loc[j, "description"]
            rows.append(
                {
                    "probe": probe,
                    "symbol": SYMBOLS.get(
                        probe,
                        f"EST {probe}" if desc == "ESTs" else desc.split(",")[0][:28],
                    ),
                    "description": desc,
                    "f": round(float(f), 1),
                    "high": means[probe].idxmax(),
                    "means": {c: round(float(means.loc[c, probe]), 3) for c in ORDER},
                }
            )
        rows.sort(key=lambda r: (ORDER.index(r["high"]), -r["f"]))
        order = np.argsort(self.ytrain.to_numpy(), kind="stable")
        cols = [r["probe"] for r in rows]
        z = self.xtrain[cols].iloc[order]
        z = ((z - z.mean()) / z.std()).T.round(2)
        return {
            "genes": rows,
            "samples": self.ytrain.iloc[order].tolist(),
            "z": z.to_numpy().tolist(),
        }

    def pca(self):
        out = {}
        idx, _ = self.selected()
        for label, cols in [("all", slice(None)), ("selected", idx)]:
            scaler = StandardScaler().fit(self.xtrain.iloc[:, cols])
            p = PCA(2, random_state=SEED).fit(
                scaler.transform(self.xtrain.iloc[:, cols])
            )
            tr = p.transform(scaler.transform(self.xtrain.iloc[:, cols]))
            te = p.transform(scaler.transform(self.xtest.iloc[:, cols]))
            out[label] = {
                "explained": p.explained_variance_ratio_.round(4).tolist(),
                "train": [
                    [*map(float, xy.round(3)), c]
                    for xy, c in zip(tr, self.ytrain, strict=True)
                ],
                "test": [
                    [*map(float, xy.round(3)), c]
                    for xy, c in zip(te, self.ytest, strict=True)
                ],
            }
        return out

    def test(self, emit):
        if self.model is None:
            raise RuntimeError("Train the model before opening the test set")
        scores = self.model.decision_function(self.xtest)
        classes = list(self.model.classes_)
        preds = self.model.predict(self.xtest)
        for i, (truth, pred) in enumerate(zip(self.ytest, preds, strict=True)):
            emit(
                "sample",
                {
                    "i": i,
                    "id": f"test_{i + 1:02d}",
                    "truth": truth,
                    "pred": pred,
                    "scores": {
                        c: round(float(s), 4)
                        for c, s in zip(classes, scores[i], strict=True)
                    },
                },
            )
            time.sleep(0.22)
        cm = pd.crosstab(self.ytest, pd.Series(preds, index=self.ytest.index)).reindex(
            index=ORDER, columns=ORDER, fill_value=0
        )
        emit(
            "metrics",
            {
                "correct": int((preds == self.ytest.to_numpy()).sum()),
                "accuracy": round(float((preds == self.ytest.to_numpy()).mean()), 4),
                "balanced": round(float(balanced_accuracy_score(self.ytest, preds)), 4),
                "macro_f1": round(
                    float(f1_score(self.ytest, preds, average="macro")), 4
                ),
                "confusion": cm.to_numpy().tolist(),
            },
        )

    def leak(self, emit, n):
        """Same seed and permutation sequence as run_khan_showcase.py (its shuffles 1..n)."""
        k = self.params["k"] if self.params else 25
        c = self.params["C"] if self.params else 0.01
        rng = np.random.default_rng(SEED)
        cv = StratifiedKFold(5, shuffle=True, random_state=SEED)
        y0 = self.ytrain.to_numpy()
        for i in range(1, n + 1):
            y = rng.permutation(y0)
            leaky_x = SelectKBest(f_classif, k=k).fit_transform(self.xtrain, y)
            leaky = make_pipeline(
                StandardScaler(),
                LinearSVC(C=c, class_weight="balanced", dual="auto", max_iter=20000),
            )
            emit(
                "shuffle",
                {
                    "i": i,
                    "leaky": round(
                        float(
                            cross_val_score(
                                leaky, leaky_x, y, cv=cv, scoring="balanced_accuracy"
                            ).mean()
                        ),
                        4,
                    ),
                    "inside": round(
                        float(
                            cross_val_score(
                                expression_pipeline(k=k, c=c, seed=SEED),
                                self.xtrain,
                                y,
                                cv=cv,
                                scoring="balanced_accuracy",
                            ).mean()
                        ),
                        4,
                    ),
                    "labels": y[:63].tolist(),
                },
            )


LAB = None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def send_body(self, body, ctype):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def stream(self, job):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()

        def emit(event, payload):
            self.wfile.write(
                f"event: {event}\ndata: {json.dumps(payload)}\n\n".encode()
            )
            self.wfile.flush()

        if not LAB.lock.acquire(blocking=False):
            emit("fail", {"message": "Başqa bir addım hələ işləyir."})
            return
        try:
            job(emit)
            emit("done", {})
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception as exc:  # report to the page, then keep serving
            emit("fail", {"message": f"{type(exc).__name__}: {exc}"})
            raise
        finally:
            LAB.lock.release()

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/":
            self.send_body(PAGE.read_text(encoding="utf-8"), "text/html; charset=utf-8")
        elif url.path == "/api/summary":
            self.send_body(json.dumps(LAB.summary()), "application/json")
        elif url.path == "/api/train":
            self.stream(LAB.train)
        elif url.path == "/api/test":
            self.stream(LAB.test)
        elif url.path == "/api/leak":
            n = int(parse_qs(url.query).get("n", ["20"])[0])
            if not 1 <= n <= 100:
                self.send_error(400, "n must be between 1 and 100")
                return
            self.stream(lambda emit: LAB.leak(emit, n))
        else:
            self.send_error(404)


def main():
    global LAB
    print("Khan datası yüklənir...")
    LAB = Lab()
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}"
    print(f"Canlı demo hazırdır: {url}  (dayandırmaq üçün Ctrl+C)")
    if "--no-browser" not in sys.argv:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


if __name__ == "__main__":
    main()
