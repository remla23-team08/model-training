"""
Evaluate the model and return results
"""

import json
import logging
import os

import joblib  # type: ignore
from sklearn.metrics import accuracy_score, confusion_matrix  # type: ignore


def model_eval(classifier, X_test, y_test, save_score=False, root=None):
    """
    Returns model evaluation metrics for given model and dataset
    """

    y_pred = classifier.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    acc_score = accuracy_score(y_test, y_pred)

    if save_score:
        # Save results to reports/model_evaluation.json
        metric_json = {"Accuracy": acc_score, "Confusion Matrix": str(conf_matrix)}
        with open(
            os.path.join(root, "..", "reports/model_evaluation.json"),
            "w",
            encoding="UTF-8",
        ) as f:
            json.dump(metric_json, f)

        logging.info("Evaluation results saved to evaluation_results.json")

    return acc_score, conf_matrix


if __name__ == "__main__":
    # Specify the absolute path to root
    root_path = os.path.dirname(os.path.abspath(__file__))

    # Load X_test and y_test from the joblib file
    data = joblib.load(os.path.join(root_path, "..", "data/processed/test_data.joblib"))
    X_test_loaded = data["X_test"]
    y_test_loaded = data["y_test"]

    # Load model
    model = joblib.load(
        os.path.join(
            root_path,
            "..",
            "data",
            "models",
            "c2_Classifier_Sentiment_Model",
        )
    )

    model_eval(
        model, X_test_loaded, y_test_loaded, save_score=True, root=root_path
    )  # save score to file
