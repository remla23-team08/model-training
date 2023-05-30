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

# Get the root path of the current script
root_path = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to data.csv
dataset_path = os.path.join(root_path, '..', 'restaurant-sentiment', 'a1_RestaurantReviews_HistoricDump.tsv')

if __name__ == "__main__":
    # Define filepaths and load data
    dataset = load_data(dataset_path)

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
    joblib.dump(model, os.path.join(root_path, '..', 'data/models/c2_Classifier_Sentiment_Model'))
