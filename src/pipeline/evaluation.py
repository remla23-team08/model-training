#! /usr/bin/env

"""
Evaluate the model and return results
"""

import json
import logging
import os

import joblib  # type: ignore
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore

from preprocessing import Preprocessing


def model_eval(
    classifier,
    set_path="data/external/a1_RestaurantReviews_HistoricDump.tsv",
    split=0.1,
    state=0,
):
    """
    Returns model evaluation metrics for given model and dataset
    """

    # Specify the absolute path to corpus and dataset
    root_path = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(root_path, "..", "..", set_path)

    # Load data from file
    dataset = pd.read_csv(
        dataset_path, delimiter="\t", quoting=3, dtype={"Review": object, "Liked": int}
    )[:]

    # Preprocess dataset
    preprocess_class = Preprocessing()
    corpus = preprocess_class.preprocess_dataset(dataset)

    # Load CV
    count_vectoriser = joblib.load(
        os.path.join(
            root_path, "..", "..", "data", "models", "c1_BoW_Sentiment_Model.pkl"
        )
    )

    # Create X and Y
    X = count_vectoriser.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    # Create train-test split
    _, X_test, _, y_test = train_test_split(X, y, test_size=split, random_state=state)

    y_pred = classifier.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    acc_score = accuracy_score(y_test, y_pred)

    # Save results to reports/model_evaluation.json
    metric_json = {"Accuracy": acc_score, "Confusion Matrix": str(conf_matrix)}
    with open(
        os.path.join(root_path, "..", "..", "reports/model_evaluation.json"),
        "w",
        encoding="UTF-8",
    ) as f:
        json.dump(metric_json, f)

    logging.info("Evaluation results saved to evaluation_results.json")

    return acc_score, conf_matrix


if __name__ == "__main__":
    model = joblib.load(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "..",
            "data",
            "models",
            "c2_Classifier_Sentiment_Model",
        )
    )
    model_eval(model)
