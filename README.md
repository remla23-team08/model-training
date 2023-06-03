# model-training
Contains the ML training pipeline used for the main project of course CS4295: Release Engineering for Machine Learning Applications. This pipeline is of an ML model that evaluates restaurant reviews. The repository structure is based off the Cookiecutter template.

## Dependencies
All required packages can be found in `requirements.txt`. To install the required packages, run the following command:

```bash
pip install -r dep/requirements.txt
```

## Usage
In order to run the pipeline, ensure that you have `dvc` installed and run the following command:

```bash
dvc exp run
```

This will automatically download the dataset from an external source, pre-process the dataset, train the model and save the evaluation results in `reports/model_evaluation.json`. Tests will also automatically be ran. Linting via Pylint and DSLinter is also automatically run as part of the pipeline.

To view a graphical representation of the pipeline, run the following command:
``` bash
dvc dag
```
### Remote
A Google drive folder has been configured to be used as remote storage.

### Testing
In order to test the ML pipeline, several tests are performed which can be found in `tests/`. These are ran automatically as part of the pipeline. They can be manually ran using the following command:

```bash
pytest
```
### Metrics
The accuracy metric is stored in `reports/model_evaluation.json`. In order to see the experiment history, run the following command:

```bash
dvc exp show
```
Two experiments are listed, comparing the use of a 20% and 10% test split size. 
### Dataset
Project was created using the dataset provided by course instructors on [SURFdrive](https://surfdrive.surf.nl/files/index.php/s/207BTysNQFuVZPE?path=%2Fmaterial).

### Preprocessing
Any preprocessing steps can be found in `preprocessing.py`. These are executed automatically with the execution of the pipeline. Processed data (corpus) is stored in `data/processed/`.

### Storing the trained model
The trained model is stored in `data/models/`.


## Pylint & DSLinter
Pylint and DSLinter have been used and configured to ensure the code quality. All configuration options can be found in `.pylintrc`. This configuration file is based on [this example from the DSLinter documentation](https://github.com/SERG-Delft/dslinter/blob/main/docs/pylint-configuration-examples/pylintrc-for-ml-projects/.pylintrc). Besides this, there are a few custom changes, such as adding the variable names `X_train`, `X_test` etc. to the list of accepted variable names by Pylint, as these variable names are commonly used in ML applications. The `init_hook` variable in `.pylintrc` is also set to the path of this directory, in order to ensure that all imports within the code do not result in a warning from Pylint.

If you would like to manually verify the code quality, please run the following command:

```bash
pylint src
```

DSLinter is configured and will automatically run. This should return a perfect score of 10.00. A report summarising the findings can be found in `data/reports/`. 
