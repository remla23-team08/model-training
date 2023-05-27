import joblib
from load_data import load_data
from preprocessing import data_preprocessing
from classification import data_classification, model_eval

# Define filepaths and load data
dataset_path = r"restaurant-sentiment/a1_RestaurantReviews_HistoricDump.tsv"
dataset = load_data(dataset_path)

# Perform preprocessing
X, y = data_preprocessing(dataset)

# Train and evaluate classifier, prints eval metrics
model = data_classification(X, y)

model_eval(model, X, y)
# new_path = r"restaurant-sentiment/a2_RestaurantReviews_FreshDump.tsv"
# new_data = load_data(new_path)

# X_new, y_new = data_preprocessing(new_data)

# model_eval(model, X_new, y_new)

# Store model
joblib.dump(model, 'data/models/c2_Classifier_Sentiment_Model') 