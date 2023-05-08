import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def data_preprocessing(dataset):
    nltk.download('stopwords')
    ps = PorterStemmer()

    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    corpus=[]
    for i in range(0, len(dataset)):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)

    cv = CountVectorizer(max_features = 1420)

    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    # Saving BoW dictionary to later use in prediction
    bow_path = 'res/c1_BoW_Sentiment_Model.pkl'
    pickle.dump(cv, open(bow_path, "wb"))
    
    return X, y