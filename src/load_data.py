import pandas as pd

def load_data(dataset_path):
    dataset = pd.read_csv(dataset_path, delimiter = '\t', quoting = 3)
    return dataset