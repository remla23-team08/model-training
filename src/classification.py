from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
import joblib

def prepare_dataset(X, y): 
    """
    Creates train/test split
    """    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
    return X_train, X_test, y_train, y_test


def model_eval(classifier, X_test, y_test):
    """
    Prints model evaluation metrics
    """
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm, accuracy_score(y_test, y_pred))

    return None


def data_classification(X, y):
    """
    Define, fit and evaluate GaussianNB classifier
    """
    # split dataset
    X_train, X_test, y_train, y_test = prepare_dataset(X, y)

    # define and fit classifier
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    
    return classifier