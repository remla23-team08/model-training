#! /usr/bin/env

"""
Tests regarding placeholders
"""


import joblib  # type: ignore
import pytest


@pytest.fixture(name="trained_model")
def load_trained_model():
    """Loads trained model"""
    classifier = joblib.load("data/models/c2_Classifier_Sentiment_Model")
    yield classifier


def test_placeholder():
    """Test nondeterminism robustness"""


if __name__ == "__main__":
    test_placeholder()
