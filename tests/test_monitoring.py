"""
Tests regarding monitoring
"""

import time

import psutil

from src.training import train_model


def test_training_time(X, y):
    """Test training time, if it exceeds 30 seconds fail."""
    start = time.time()
    _ = train_model(X, y)
    end = time.time()

    if abs(end - start) > 30:
        raise TimeoutError("Training time took more than 30 seconds.")


def test_ram_usage(X, y):
    """Test training ram usage"""
    _ = train_model(X, y)

    # Measure current RAM
    ram_usage = psutil.Process().memory_info().rss

    if ram_usage > 5e8:
        raise MemoryError(
            "Training took more than 500Mb of RAM." f"RAM usage: {(ram_usage/1e6):.2f}"
        )
