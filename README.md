# model-training
Contains the ML training pipeline used for the main project of course CS4295: Release Engineering for Machine Learning Applications. This pipeline is of an ML model that evaluates restaurant reviews.

## Dependencies
All required packages can be found in dep/requirements.txt. To install the required packages, run the following command:

```bash
pip install -r dep/requirements.txt
```

## Dataset
Project was created using the dataset provided by course instructors on [SURFdrive](https://surfdrive.surf.nl/files/index.php/s/207BTysNQFuVZPE?path=%2Fmaterial)

To use this repository, please download the archive at the link above, unzip the archive and place the `restaurant-sentiment/` folder in the main `model-training` folder.

## Usage
To manually generate a new ML model, execute `main.py`. 

### Preprocessing
Any preprocessing steps can be found in `preprocessing.py`. These are executed automatically with the execution of `main.py`.


### Storing the trained model
The trained model is stored in the `res/` folder.
