"""
This file contains functions related to preprocessing of any data provided to the model
"""

import logging
import os

import joblib  # type: ignore
import pandas as pd
from libpython import preprocessing

from util import get_paths

if __name__ == "__main__":
    # Get relative paths
    root_path, dataset_path = get_paths()

    # Load data from file
    load_dataset = pd.read_csv(
        dataset_path, delimiter="\t", quoting=3, dtype={"Review": object, "Liked": int}
    )[:]

    # Preprocess and store processed corpus in joblib
    logging.info("Preprocessing the dataset...")

    preprocess_class = preprocessing.Preprocessing()
    save_corpus = preprocess_class.preprocess_dataset(load_dataset)
    corpus_path = os.path.join(root_path, "..", "data/processed/corpus.joblib")
    joblib.dump(save_corpus, corpus_path)
    logging.info("Processed dataset (corpus) is saved to: %s", corpus_path)
