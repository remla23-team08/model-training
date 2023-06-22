# model-training
Contains the ML training pipeline used for the main project of course CS4295: Release Engineering for Machine Learning Applications. This pipeline is of an ML model that evaluates restaurant reviews. The repository structure is based off the Cookiecutter template.

## :books: **Tabel of Contents**

- [model-training](#model-training)
  - [:books: **Tabel of Contents**](#books-tabel-of-contents)
  - [:scroll: **Pre-requisites**](#scroll-pre-requisites)
  - [:gear: **Poetry Setup**](#gear-poetry-setup)
    - [**Installation (Poetry)**](#installation-poetry)
    - [**Python Version**](#python-version)
    - [**Installing dependencies**](#installing-dependencies)
    - [**Adding a new dependency**](#adding-a-new-dependency)
    - [**The `pyproject.toml` Configuration**](#the-pyprojecttoml-configuration)
  - [:rocket: **Pipeline Usage**](#rocket-pipeline-usage)
    - [**Remote**](#remote)
    - [**Testing**](#testing)
    - [**Metrics**](#metrics)
    - [**Dataset**](#dataset)
    - [**Preprocessing**](#preprocessing)
    - [**Storing the trained model**](#storing-the-trained-model)
  - [:clipboard: **Linting**](#clipboard-linting)
  - [:art: **Formatting (isort \& black)**](#art-formatting-isort--black)
    - [**isort**](#isort)
    - [**black**](#black)

## :scroll: **Pre-requisites**

* Python >= `3.8.*` or <= `3.10.*`
  * Installation varies per python version and OS. Please refer to the [Python website](https://www.python.org/downloads/) for more details.
* Poetry
  * Refer to the [Installation (Poetry)](#installation-poetry) section for more details
* DVC 
  * See installation instructions [here](https://dvc.org/doc/install)

This project is using Poetry instead of Pip to manage dependencies. Poetry is a Python dependency management tool that simplifies the process of managing dependencies and packaging. Additionally, Poetry is also used to manage the virtual environment from which the project is run, thus not requiring the user to manually create a virtual environment. As such, make sure you have poetry installed before proceeding with the next sections. 

> **Note:** If you are not familiar with Poetry, you can find additional details about the setup by referring to the [Poetry Setup](#poetry-setup) section. If you have experience with it, you can skip this section by going directly to the [Pipeline Usage](#pipeline-usage) section.

## :gear: **Poetry Setup**

### **Installation (Poetry)**

To install Poetry, please follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) and follow the corresponding steps for your operating system.

### **Python Version**

Poetry for this project is configured to using any python version in the range of `3.8.*` to `3.10.*`. If you are using a different version of Python, you need to install a correct version and configure your poetry environment to use it. For example, to use `python3.8` you can run the following command:

```bash
poetry env use python3.8
```

> **Note**: The actual python value should be the path to the python executable (if not already on the `$PATH`). If already on the system, while on Linux-based systems, you can directly use `poetry env use $(which python3.8)` to use the correct path. If you installed the python binary in a different location, you must use the correct path to the executable.

### **Installing dependencies**

To install the project dependencies, please run the following command:

```bash
poetry install
```

This will install all dependencies listed in `pyproject.toml` and create a virtual environment for the project. As such, instead of using `pip` to install a specific dependency and then run that dependency in a virtual environment, Poetry will handle this for you.

### **Adding a new dependency**

To add a new dependency, please run the following command:

```bash
poetry add <dependency-name>
```

This will add the dependency to `pyproject.toml` and install it in the virtual environment.
However, if you would like to install a dependency for development purposes, please run the following command:

```bash
poetry add --dev <dependency-name>
```

In any case, dependency changes will also show up in the `poetry.lock` file. This file is used to ensure that all developers are using the same versions of the dependencies. Consequently, it is good practice and actually recommended that this file is committed to version control.

### **The `pyproject.toml` Configuration**

The `pyproject.toml` file is used to configure the project by managing dependencies and configuring poetry itself. It is also used to configure additional behaviours for linting and testing - essentially acting as a configuration file for the dependencies used in the project. For example, the `pyproject.toml` file in this project is used to configure the following:
* The Python version 
* The project name
* What profile `isort` should use
* What sources `bandit` should analyze
* etc.

## :rocket: **Pipeline Usage**

In order to run the pipeline, ensure that you have `dvc` installed and run the following command:

```bash
poetry run dvc exp run
```

Alternatively, you can also run the following command:
  
```bash
poetry run dvc repro
```

Both of these commands will automatically download the dataset from an external source, pre-process the dataset, train the model and save the evaluation results in `reports/model_evaluation.json`. Tests will also automatically be ran. Linting via Pylint and DSLinter is also automatically run as part of the pipeline.

> **Note**: The aforementioned commands will produce reports in the `reports/` folder. Some of these reports relate to the testing phase, namely the `tests-report.xml` and `coverage-report.xml`, whereas the rest relate to `mllint` and `pylint` scores. 

To view a graphical representation of the pipeline, run the following command:
``` bash
poetry run dvc dag
```

### **Remote**

A Google drive folder has been configured to be used as remote storage.

### **Testing**

In order to test the ML pipeline, several tests are performed which can be found in `tests/`. These are ran automatically as part of the pipeline. They can be manually ran using the following command:

```bash
poetry run pytest
```

The coverage report and test report are both found in the `reports/` folder.

### **Metrics**

The accuracy metric is stored in `reports/model_evaluation.json`. In order to see the experiment history, run the following command:

```bash
poetry run dvc exp show
```
Two experiments are listed, comparing the use of a 20% and 10% test split size.

### **Dataset**

Project was created using the dataset provided by course instructors on [SURFdrive](https://surfdrive.surf.nl/files/index.php/s/207BTysNQFuVZPE?path=%2Fmaterial).

### **Preprocessing**

Any preprocessing steps can be found in `preprocessing.py`. These are executed automatically with the execution of the pipeline. Processed data (corpus) is stored in `data/processed/`.

### **Storing the trained model**

The trained model is stored in `data/models/`.

## :clipboard: **Linting**
We are using the mllint tool to check for common mistakes in ML projects (formatting, tests, general good practice rules). The report that was used in the latest run of the pipeline can be found within `reports/mllint_report.md`.

> Note: The mllint tool combines multiple linters and uses rules for testing, configuration and other topics that are specific to ML projects. You can find the official source code for the tool [here](https://github.com/bvobart/mllint).

Pylint and DSLinter have been configured to ensure the code quality, and are run as part of mllint. All configuration options can be found in `.pylintrc`. This configuration file is based on [this example from the DSLinter documentation](https://github.com/SERG-Delft/dslinter/blob/main/docs/pylint-configuration-examples/pylintrc-for-ml-projects/.pylintrc). Besides this, there are a few custom changes, such as adding the variable names `X_train`, `X_test` etc. to the list of accepted variable names by Pylint, as these variable names are commonly used in ML applications. The `init_hook` variable in `.pylintrc` is also set to the path of this directory, in order to ensure that all imports within the code do not result in a warning from Pylint.

isort and black are used for the formatting. If you would like to manually verify the code quality, please run the following command:

```bash
poetry run mllint
```

This will run mllint, which includes several linters. DSLinter is configured and will automatically run. This should return a perfect score of 10.00. A report summarising the findings can be found in `reports/mllint_report.md`. 


## :art: **Formatting (isort & black)**

The project uses `isort` and `black` to format the code. `isort` is used to sort the imports in the code, while `black` is used to format the code itself. Both of these tools are configured in `pyproject.toml`.

### **isort**

If you would like to manually format the imports, please run the following command from within the root directory of the project:

```bash
poetry run isort .
```

This command will sort the imports in all files in the project. Naturally, you can also specify a specific file or directory to format. You can also check for any rule violations by running the following command:

```bash
poetry run isort --check-only .
``` 

> There are many more configuration options, therefore consider looking at the [isort documentation](https://pycqa.github.io/isort/) if you are interested in more information.

### **black**

If you would like to manually format the code, please run the following command from within the root directory of the project:

```bash
poetry run black .
```

Similarly, this command will format all files within the project - different files/directories can also be specified. Additionally, if you would only like to check any rule violations, please run the following command:

```bash
poetry run black --check .
```

> Again, there are many more configuration options, therefore consider looking at the [black readthedocs page](https://black.readthedocs.io/en/stable/) if you are interested in more information.

