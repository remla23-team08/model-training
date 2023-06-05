# #! /usr/bin/env

"""
This script loads data from the dataset_path into a pandas dataset.
"""

import os
import urllib.request
import zipfile


if __name__ == "__main__":
       # Specify the relative path to data tsv
    root_path = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(root_path, '..', '..', 'data', 'external', 'a1_RestaurantReviews_HistoricDump.tsv')

    # Import the data from external source
    print("Importing external dataset..")
    URL = r'https://drive.google.com/uc?export=download&id=1G7rLkSloPUzkK4zCzb9lLR0zSYygu8mK'
    zip_path, _ = urllib.request.urlretrieve(URL)

    # Define export path for dataset
    export_path = os.path.dirname(os.path.abspath(dataset_path))

    # Unzip at export path
    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(export_path)

    # Print success to console
    print("External dataset sucessfully imported!")
