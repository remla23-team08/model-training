"""
Tests regarding ML development
"""

from sklearn.model_selection import train_test_split

from src.evaluation import model_eval
from src.training import train_model


def test_nondeterminism_robustness(trained_model, X, y):
    """Test nondeterminism robustness"""
    # Create train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.10, random_state=0
    )

    base_score, _ = model_eval(trained_model, X_test, y_test)  # score from 0 - 1

    for state in [1, 2]:  # Comparitive score
        new_model = train_model(X_train, y_train, state=state)
        score, _ = model_eval(new_model, X_test, y_test)
        if abs(base_score - score) > 0.2:
            raise AssertionError(
                f"Model score is not robust to nondeterminism. "
                f"Base score: {base_score}, "
                f"score with seed {state}: {score}"
            )
