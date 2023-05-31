#! /usr/bin/env

"""
Evaluate the model and return results
"""

from sklearn.metrics import confusion_matrix, accuracy_score


def model_eval(classifier, X_test, y_test):
    """
    Returns model evaluation metrics
    """
    y_pred = classifier.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    acc_score = accuracy_score(y_test, y_pred)
    return conf_matrix, acc_score
