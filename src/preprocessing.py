#! /usr/bin/env

"""
This file contains functions related to preprocessing of any data provided to the model
"""

import os
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

def data_preprocessing(dataset):
    """
    Main preprocessing steps for ML data
    """
    nltk.download('stopwords')
    porter_stem = PorterStemmer()

    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    corpus=[]
    for i in range(0, len(dataset)):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower()
        review = review.split()
        review = [porter_stem.stem(word) for word in review if not word in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)

    # Use count vectoriser to transform dataset
    count_vectoriser = CountVectorizer(max_features = 1420)
    X = count_vectoriser.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    # Get the parent directory
    parent_dir = os.path.dirname(os.getcwd())

    # Saving BoW dictionary to later use in prediction
    bow_path = os.path.join(parent_dir, r'data/models/c1_BoW_Sentiment_Model.pkl')
    with open(bow_path, "wb") as file:
        pickle.dump(count_vectoriser, file)

    return X, y
