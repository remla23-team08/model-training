#! /usr/bin/env

"""
Tests regarding ML development
"""

import joblib
import pytest

from src.pipeline.evaluation import model_eval


@pytest.fixture()
def trained_model():
    """ Loads trained model """
    classifier = joblib.load('data/models/c2_Classifier_Sentiment_Model')
    yield classifier


def test_nondeterminism_robustness(trained_model):
    """ Test nondeterminism robustness"""
    base_score, _ = model_eval(trained_model)# score from 0 - 1
    for seed in [1, 2]:
        score, _ = model_eval(trained_model, state=seed)
        assert abs(base_score - score) <= 0.03

if __name__ == "__main__":
    test_nondeterminism_robustness(joblib.load('data/models/c2_Classifier_Sentiment_Model'))