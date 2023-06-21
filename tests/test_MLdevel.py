#! /usr/bin/env

"""
Tests regarding ML development
"""

import os

import joblib  # type: ignore
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split  # type: ignore

from src.evaluation import model_eval
from src.util import get_paths


@pytest.fixture(name="trained_model")
def load_trained_model():
    """Loads trained model"""
    classifier = joblib.load("data/models/c2_Classifier_Sentiment_Model")
    yield classifier


def test_nondeterminism_robustness(trained_model):
    """Test nondeterminism robustness"""
    # Specify the absolute path to corpus and dataset
    root_path, dataset_path = get_paths()
    corpus_path = os.path.join(root_path, "..", "data/processed/corpus.joblib")

    # Load data from file
    dataset = pd.read_csv(
        dataset_path, delimiter="\t", quoting=3, dtype={"Review": object, "Liked": int}
    )[:]
    corpus = joblib.load(corpus_path)
    dataset = pd.read_csv(
        dataset_path, delimiter="\t", quoting=3, dtype={"Review": object, "Liked": int}
    )[:]
    count_vectoriser = joblib.load(
        os.path.join(root_path, "..", "data", "models", "c1_BoW_Sentiment_Model.pkl")
    )

    # Create X and Y
    X = count_vectoriser.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    split = 0.1
    for state in [0, 1, 2]:
        # Create train-test split
        _, X_test, _, y_test = train_test_split(
            X, y, test_size=split, random_state=state
        )

        if state == 0:  # base score to compare to
            base_score, _ = model_eval(
                trained_model, X_test, y_test
            )  # score from 0 - 1
        else:  # comparitive score
            score, _ = model_eval(trained_model, X_test, y_test)
            if abs(base_score - score) > 0.2:
                raise AssertionError(
                    f"Model score is not robust to nondeterminism. "
                    f"Base score: {base_score}, "
                    f"score with seed {state}: {score}"
                )


if __name__ == "__main__":
    test_nondeterminism_robustness(
        joblib.load("data/models/c2_Classifier_Sentiment_Model")
    )
