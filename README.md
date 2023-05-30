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


## Pylint & DSLinter
Pylint and DSLinter have been used and configured to ensure the code quality. All configuration options can be found in `.pylintrc`. This configuration file is based on [this example from the DSLinter documentation](https://github.com/SERG-Delft/dslinter/blob/main/docs/pylint-configuration-examples/pylintrc-for-ml-projects/.pylintrc). Besides this, there are a few custom changes, such as adding the variable names `X_train`, `X_test` etc. to the list of accepted variable names by Pylint, as these variable names are commonly used in ML applications. The `init_hook` variable in `.pylintrc` is also set to the path of this directory, in order to ensure that all imports within the code do not result in a warning from Pylint.

If you would like to manually verify the code quality, please run the following command:

```bash
pylint src
```

DSLinter is configured and will automatically run. This should return a perfect score of 10.00. A report summarising the findings can be found in the `data/reports` folder. 
