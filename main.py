from IPython.display import clear_output
import os.path
from src.load_data import save_mfcc, load_mfcc
from src.visualisation import visualise
from src.preprocessing import preprocessing
# Define filepaths
dataset_path = r"Data/genres_original"
json_path = r"res/data.json"

# Load data into json file 
if os.path.isfile(json_path):
    # If the file exists, load mfcc json
    X, y = load_mfcc(json_path)
else: # If not, create data.json with mfcc features
    save_mfcc(dataset_path,json_path,num_segments=10)
    clear_output()
    X, y = load_mfcc(json_path)

# Visualise .wav file of any song
vis = False
if vis:
    songpath = r"Data/genres_original/blues/blues.0000"
    visualise(dataset_path, json_path, songpath)

# Preprocessing
