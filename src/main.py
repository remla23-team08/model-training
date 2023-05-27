#! /usr/bin/env

"""
Main execution script to manually execute the processing pipeline
"""

import os
import joblib
from load_data import load_data
from preprocessing import data_preprocessing
from classification import data_classification
from evaluation import model_eval

# Get the parent directory
parent_dir = os.path.dirname(os.getcwd())

# Path to dataset
DATASET_PATH = r"restaurant-sentiment/a1_RestaurantReviews_HistoricDump.tsv"
global_path = os.path.join(parent_dir, DATASET_PATH)

if __name__ == "__main__":
    # Define filepaths and load data
    dataset = load_data(global_path)

    # Perform preprocessing
    X, y = data_preprocessing(dataset)

    # Train and evaluate classifier, prints eval metrics
    model, X_test, y_test = data_classification(X, y)

    model_eval(model, X_test, y_test)
    # new_path = r"restaurant-sentiment/a2_RestaurantReviews_FreshDump.tsv"
    # new_data = load_data(new_path)

    # X_new, y_new = data_preprocessing(new_data)

    # model_eval(model, X_new, y_new)

    # Store model
    joblib.dump(model, os.path.join(parent_dir, 'data/models/c2_Classifier_Sentiment_Model'))
