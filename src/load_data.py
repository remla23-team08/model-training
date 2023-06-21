# #! /usr/bin/env

"""
This script loads data from the dataset_path into a pandas dataset.
"""

import logging
import os
import tempfile
import zipfile

import requests

from util import get_paths

if __name__ == "__main__":
    # Specify the relative path to data tsv
    root_path, dataset_path = get_paths()

    # Import the data from external source
    logging.info("Importing external dataset..")

    # Define URL to download dataset from
    URL = r"https://drive.google.com/uc?export=download&id=1G7rLkSloPUzkK4zCzb9lLR0zSYygu8mK"
    temp_zip_path = tempfile.NamedTemporaryFile(delete=False)

    # Download dataset
    with temp_zip_path as f:
        response = requests.get(URL, timeout=10)
        f.write(response.content)
    temp_zip_path.close()

    # Define export path for dataset
    export_path = os.path.dirname(os.path.abspath(dataset_path))

    # Unzip at export path
    with zipfile.ZipFile(temp_zip_path.name, "r") as f:
        f.extractall(export_path)

    # Remove temporary zip file
    os.remove(temp_zip_path.name)

    # Print success to console
    logging.info("External dataset sucessfully imported!")
