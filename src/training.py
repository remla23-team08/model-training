"""
File that trains the model based on preprocessed data from earlier stages
"""

import os

import joblib  # type: ignore
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer  # type: ignore
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.model_selection import train_test_split  # type: ignore


def train_model(X_t, y_t, state=0):
    """Trains model"""
    kernel = 1.0 * RBF(1.0)
    model = GaussianProcessClassifier(kernel=kernel, random_state=state).fit(X_t, y_t)
    return model


if __name__ == "__main__":
    # Specify the absolute path to corpus and dataset
    root_path = os.path.dirname(os.path.abspath(__file__))
    corpus_path = os.path.join(root_path, "..", "data/processed/corpus.joblib")
    dataset_path = os.path.join(
        root_path,
        "../data/external/a1_RestaurantReviews_HistoricDump.tsv",
    )

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
    classifier = train_model(X_train, y_train)

    # Store model and CV
    joblib.dump(
        classifier,
        os.path.join(root_path, "..", "data/models/c2_Classifier_Sentiment_Model"),
    )
    joblib.dump(
        count_vectoriser,
        os.path.join(root_path, "..", "data", "models", "c1_BoW_Sentiment_Model.pkl"),
    )

    # Store test data
    data = {"X_test": X_test, "y_test": y_test}

    joblib.dump(data, os.path.join(root_path, "..", "data/processed/test_data.joblib"))
