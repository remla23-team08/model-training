# #! /usr/bin/env

"""
This script loads data from the dataset_path into a pandas dataset.
"""

import logging
import os
import urllib.request
import zipfile

from Util import Util

if __name__ == "__main__":
    # Specify the relative path to data tsv
    root_path, dataset_path = Util.get_paths()

    # Import the data from external source
    logging.info("Importing external dataset..")

    # Define URL to download dataset from
    URL = r"https://drive.google.com/uc?export=download&id=1G7rLkSloPUzkK4zCzb9lLR0zSYygu8mK"  # nosec B310
    zip_path, _ = urllib.request.urlretrieve(URL)

    # Define export path for dataset
    export_path = os.path.dirname(os.path.abspath(dataset_path))

    # Unzip at export path
    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(export_path)

    # Print success to console
    logging.info("External dataset sucessfully imported!")
