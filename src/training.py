#! /usr/bin/env

"""
File that trains the model based on preprocessed data from earlier stages
"""

import os

import joblib  # type: ignore
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.naive_bayes import GaussianNB  # type: ignore

from util import get_paths

if __name__ == "__main__":
    # Specify the absolute path to corpus and dataset
    root_path, dataset_path = get_paths()
    corpus_path = os.path.join(root_path, "..", "data/processed/corpus.joblib")

    # Load data
    corpus = joblib.load(corpus_path)
    dataset = pd.read_csv(
        dataset_path, delimiter="\t", quoting=3, dtype={"Review": object, "Liked": int}
    )[:]

    # Use count vectoriser to transform dataset
    count_vectoriser = CountVectorizer(max_features=1420)

    # Train count vectoriser
    X = count_vectoriser.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    # Create train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.10, random_state=0
    )

    # define and fit classifier
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Store model and CV
    joblib.dump(
        classifier,
        os.path.join(root_path, "..", "data/models/c2_Classifier_Sentiment_Model"),
    )
    joblib.dump(
        count_vectoriser,
        os.path.join(root_path, "..", "data", "models", "c1_BoW_Sentiment_Model.pkl"),
    )