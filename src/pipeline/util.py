#! /usr/bin/env

"""
This file contains utility functions for the pipeline (for reusability).
"""

import os


def get_paths():
    """Get the root path and dataset path."""
    root_path = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(
        root_path,
        "..",
        "..",
        "data",
        "external",
        "a1_RestaurantReviews_HistoricDump.tsv",
    )
    return root_path, dataset_path
