"""
Tests regarding features
"""

from src.evaluation import model_eval


def test_distribution(dataset):
    """Test review distribution"""
    positive_reviews = len(dataset[dataset['Liked'] == 1])
    negative_reviews = len(dataset[dataset['Liked'] == 0])

    if abs(1 - positive_reviews / negative_reviews) >= 0.3:
        raise AssertionError(
                "Distribution of positive and negative is not even:"
                f"Number of positive reviews: {positive_reviews},"
                f"Number of negative reviews: {negative_reviews}."
            )

def test_sentiment(trained_model, dataset, corpus, count_vectoriser):
    """Test sentitment using data slices"""
    # Create features from corpus, and then select filtered results (to keep feature length the same)
    X = count_vectoriser.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    # Create X and Y using filtered entries (happy)
    keywords = ["good", "glad", "happy", "satisfied"]
    filtered_index = [index for index, string in enumerate(corpus) if any(keyword in string for keyword in keywords)]
    X_good, y_good = X[filtered_index], y[filtered_index]

    base_score, _ = model_eval(trained_model, X, y)
    sliced_score, _ = model_eval(trained_model, X_good, y_good)

    if abs(base_score - sliced_score) > 0.05:
        raise AssertionError(
            f"Model score using data sliced on sentiment does not perform similarly to the base score. "
            f"Base score: {base_score}, "
            f"Sliced score: {sliced_score}. "
        )
