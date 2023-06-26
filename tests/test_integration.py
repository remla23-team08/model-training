"""
Tests regarding integration
"""


import numpy as np
from sklearn.gaussian_process import GaussianProcessClassifier
import pandas as pd

from src.evaluation import model_eval


def test_load_data(dataset):
    """Test whether the load data stage has completed successfully"""
    if not isinstance(dataset, pd.DataFrame):
        raise AssertionError("load_data has not returned a valid dataset/dataframe.")

def test_preprocessing(dataset, corpus):
    """Test whether the preprocessing stage has completed succesfully"""
    if not isinstance(corpus, list):
        raise AssertionError("preprocessing has not created a valid corpus")
    
    if len(corpus) != dataset.shape[0]:
        raise AssertionError("Preprocessed corpus and dataset are not the same length")

def test_training(trained_model, test_data):
    """Check whether training stage was completed successfully."""
    if not isinstance(trained_model, GaussianProcessClassifier):
        raise AssertionError("Trained model is not a valid classifier")

    X_test_loaded, y_test_loaded = test_data["X_test"], test_data["y_test"]
    accuracy, _ = model_eval(trained_model, X_test_loaded, y_test_loaded)

    if accuracy < 0.5:
        raise AssertionError(f"Trained model's accuracy is too low (worse than random). "
                              f"Recorded model accuracy = {accuracy:.2f}")

def test_evaluation(trained_model, test_data):
    """Check whether evaluation stage is completed successfully."""
    X_test_loaded, y_test_loaded = test_data["X_test"], test_data["y_test"]
    accuracy, confusion_matrix = model_eval(trained_model, X_test_loaded, y_test_loaded)

    if not isinstance(accuracy, float):
        raise AssertionError("Evaluation accuracy is not a valid float")
    if not 0.0 <= accuracy <= 1.0:
        raise AssertionError("Evaluation accuracy is not between 0 and 1."
                             f"Accuracy: {accuracy:.2f}.")
    
    if not isinstance(confusion_matrix, np.ndarray) or confusion_matrix.shape != (2, 2):
        raise AssertionError("Confusion matrix is not a valid 2x2 ndarray.")
   