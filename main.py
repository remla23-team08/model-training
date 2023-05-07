from IPython.display import clear_output
import os.path
from src.load_data import save_mfcc
from src.visualisation import visualise
from src.classification import main_classification

# Define filepaths
dataset_path = r"Data/genres_original"
json_path = r"res/data.json"

# Create data.json containing mfcc features if it does not already exist
if not os.path.isfile(json_path):
    save_mfcc(dataset_path,json_path,num_segments=10)
    clear_output()

# Visualise .wav file of any song
vis = False # Toggle
songpath = r"Data/genres_original/blues/blues.0000"
if vis:
    visualise(dataset_path, json_path, songpath)

# Define and train classifier
model = main_classification(json_path, show_history=True)

# Save trained model
model.save(r"res/model.h5")