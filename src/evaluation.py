#! /usr/bin/env

"""
Evaluate the model and return results
"""

import os
import json
import logging

import joblib  # type: ignore
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore


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
    # Specify the absolute path to corpus and dataset
    root_path = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(
        root_path, "..", "data", "external", "a1_RestaurantReviews_HistoricDump.tsv"
    )
    corpus_path = os.path.join(root_path, "..", "data/processed/corpus.joblib")

    # Load the data, corpus and CV
    count_vectoriser = joblib.load(
        os.path.join(root_path, "..", "data", "models", "c1_BoW_Sentiment_Model.pkl")
    )
    corpus = joblib.load(corpus_path)
    dataset = pd.read_csv(
        dataset_path, delimiter="\t", quoting=3, dtype={"Review": object, "Liked": int}
    )[:]

    # Create X and Y
    X = count_vectoriser.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    _, X_test_main, _, y_test_main = train_test_split(
        X, y, test_size=0.1, random_state=0
    )

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
        model, X_test_main, y_test_main, save_score=True, root=root_path
    )  # save score to file
