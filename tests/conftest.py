"""
Utilities (pytest fixtures) for the tests
"""

import os

import joblib
import pandas as pd
import pytest

from src.util import get_paths

root_path, dataset_path = get_paths()


@pytest.fixture(name="trained_model")
def trained_model_():
    """Loads trained model"""
    classifier_path = os.path.join(
        root_path, "..", "data/models/c2_Classifier_Sentiment_Model"
    )
    classifier = joblib.load(classifier_path)
    yield classifier


@pytest.fixture(name="dataset")
def dataset_():
    """Loads dataset"""
    d_set = pd.read_csv(
        dataset_path, delimiter="\t", quoting=3, dtype={"Review": object, "Liked": int}
    )[:]
    yield d_set


@pytest.fixture(name="corpus")
def corpus_():
    """Loads corpus"""
    crps_path = os.path.join(root_path, "..", "data/processed/corpus.joblib")
    crps = joblib.load(crps_path)
    yield crps


@pytest.fixture(name="count_vectoriser")
def count_vectoriser_():
    """Loads count vectoriser"""
    cv = joblib.load(
        os.path.join(root_path, "..", "data", "models", "c1_BoW_Sentiment_Model.pkl")
    )
    yield cv


@pytest.fixture(name="test_data")
def test_data():
    """Loads test data"""
    tst_data = joblib.load(
        os.path.join(root_path, "../data/processed/test_data.joblib")
    )
    yield tst_data


@pytest.fixture(name="X")
def X(corpus, count_vectoriser):
    """Loads full X features"""
    return count_vectoriser.transform(corpus).toarray()


@pytest.fixture(name="y")
def y(dataset):
    """Loads full y class labels"""
    return dataset.iloc[:, -1].values
