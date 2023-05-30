#! /usr/bin/env

"""
Functions related to training of model and classification
"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def prepare_dataset(X, y):
    """
    Creates train/test split
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
    return X_train, X_test, y_train, y_test


def data_classification(X, y):
    """
    Define, fit and evaluate GaussianNB classifier
    """
    # split dataset
    X_train, X_test, y_train, y_test = prepare_dataset(X, y)

    # define and fit classifier
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    return classifier, X_test, y_test
