import joblib
from src.load_data import load_data
from src.preprocessing import data_preprocessing
from src.classification import data_classification

# Define filepaths and load data
dataset_path = r"restaurant-sentiment/a1_RestaurantReviews_HistoricDump.tsv"
dataset = load_data(dataset_path)

# Perform preprocessing
X, y = data_preprocessing(dataset)

# Train and evaluate classifier, prints eval metrics
model = data_classification(X, y)

# Store model
joblib.dump(model, 'res/c2_Classifier_Sentiment_Model') 