# model-training
Contains the ML training pipeline used for the main project of course CS4295: Release Engineering for Machine Learning Applications. This pipeline is of an ML model that automatically categorises music. It is based on the project "Music Genre Classification" by user dapy15 as found here: 
https://www.kaggle.com/code/dapy15/music-genre-classification/notebook.  


## Dependencies
All required packages can be found in dep/requirements.txt. To install the required packages, run the following command:

`$ pip install -r dep/requirements.txt`

## Dataset
Pipeline was created and tested using dataset sourced from the following link:
https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

To use this repository, please download the archive at the link above, unzip the archive and place the Data/ folder in the main model-training folder.

## Usage
Once the Data/ folder has been placed in the repository, execute `main.py` to train the model on the dataset. `main.py` will generate a .json file containing the contents of the Data/ folder for easier access. If data.json already exists, this step will be skipped. 

### Visualisation
Any .wav file in the Data/ folder can be visualised, by means of plotting its waveform. This is done by changing the vis variable in `main.py`to True and changing the songpath to any .wav file. 

### Preprocessing
Any preprocessing steps can be found in `preprocessing.py`. These are executed automatically with the execution of `main.py`.

### Compiling and evaluation of the model
This pipeline uses a convolutional neural network based in keras. In `main.py`, the function main_classification has a parameter called "show_history". If True, a plot will be generated showing the training loss over time. The model is trained for 50 iterations. 

The model is evaluated using accuracy and F1 scores. The custom F1 evaluation metric can be found in `eval_functions.py`.

### Storing the trained model
The model is stored as a .h5 file inside the res/ folder, which can be easily opened with keras to make future predictions. 