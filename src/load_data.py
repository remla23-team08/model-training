#! /usr/bin/env

"""
This script loads data from the dataset_path into a pandas dataset.
"""

import pandas as pd

def load_data(dataset_path):
    """Function loading data from dataset_path into pandas dataset"""
    dataset = pd.read_csv(dataset_path, delimiter = '\t', quoting = 3)
    return dataset
