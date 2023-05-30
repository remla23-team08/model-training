#! /usr/bin/env

"""
Functions related to model evaluation
"""

from sklearn.metrics import confusion_matrix, accuracy_score


def model_eval(classifier, X_test, y_test):
    """
    Prints model evaluation metrics
    """
    y_pred = classifier.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix, accuracy_score(y_test, y_pred))
