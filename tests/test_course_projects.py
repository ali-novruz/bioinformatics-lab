import sqlite3

import numpy as np
import pytest
from sklearn.model_selection import StratifiedKFold, cross_validate

from biolab.expression_ml import expression_pipeline
from biolab.study_database import initialize


def test_feature_selection_and_scaling_stay_inside_training_folds():
    rng = np.random.default_rng(31)
    x = rng.normal(size=(40, 30))
    y = np.repeat([0, 1], 20)
    cv = list(StratifiedKFold(4, shuffle=True, random_state=7).split(x, y))
    results = cross_validate(
        expression_pipeline(k=5), x, y, cv=cv, return_estimator=True
    )
    for (train, test), fitted in zip(cv, results["estimator"], strict=True):
        assert fitted.named_steps["scale"].n_samples_seen_ == len(train)
        chosen = fitted.named_steps["select"].transform(
            fitted.named_steps["variance"].transform(x[train])
        )
        assert np.allclose(fitted.named_steps["scale"].mean_, chosen.mean(axis=0))
        assert len(fitted.predict(x[test])) == len(test)


@pytest.mark.parametrize(
    "bad_row",
    [("missing", "g1", 3), ("s1", "missing", 3), ("s1", "g1", -1), ("s1", "g1", 1.5)],
)
def test_sql_rejects_invalid_relationships_and_counts(bad_row):
    with sqlite3.connect(":memory:") as connection:
        initialize(connection)
        connection.execute("INSERT INTO sample VALUES ('s1','treated',1)")
        connection.execute("INSERT INTO gene VALUES ('g1')")
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute("INSERT INTO gene_count VALUES (?,?,?)", bad_row)


def test_sql_rejects_duplicate_sample_gene_counts():
    with sqlite3.connect(":memory:") as connection:
        initialize(connection)
        connection.execute("INSERT INTO sample VALUES ('s1','treated',1)")
        connection.execute("INSERT INTO gene VALUES ('g1')")
        connection.execute("INSERT INTO gene_count VALUES ('s1','g1',2)")
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute("INSERT INTO gene_count VALUES ('s1','g1',3)")
