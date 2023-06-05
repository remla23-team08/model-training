#! /usr/bin/env

"""
This file contains functions related to preprocessing of any data provided to the model
"""

import os
import re

import joblib
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


class Preprocessing:
    """Class to easily preprocess datasets"""

    def __init__(self):
        """Initialize preprocess class"""
        nltk.download("stopwords")
        self.porter_stem = PorterStemmer()
        self.all_stopwords = stopwords.words("english")
        self.all_stopwords.remove("not")

        self.dataset = None
        self.count_vectorizer = None

    def preprocess_dataset(self, dataset):
        """Loop over entire dataset to preprocess"""
        corpus = []
        for i in range(0, len(dataset)):
            corpus.append(self.preprocess_review(dataset["Review"][i]))
        return corpus

    def preprocess_review(self, review):
        """Processing a single review"""
        review = re.sub("[^a-zA-Z]", " ", review)
        review = review.lower()
        review = review.split()
        review = [
            self.porter_stem.stem(word)
            for word in review
            if not word in set(self.all_stopwords)
        ]
        review = " ".join(review)
        return review


if __name__ == "__main__":
    # Specify the relative path to data tsv
    root_path = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(
        root_path,
        "..",
        "..",
        "data",
        "external",
        "a1_RestaurantReviews_HistoricDump.tsv",
    )

    # Load data from file
    load_dataset = pd.read_csv(
        dataset_path, delimiter="\t", quoting=3, dtype={"Review": object, "Liked": int}
    )[:]

    # Preprocess and store processed corpus in joblib
    print("Preprocessing the dataset...")
    preprocess_class = Preprocessing()
    save_corpus = preprocess_class.preprocess_dataset(load_dataset)
    corpus_path = os.path.join(root_path, "..", "..", "data/processed/corpus.joblib")
    joblib.dump(save_corpus, corpus_path)
    print(f"Processed dataset (corpus) is saved to: {corpus_path}")
