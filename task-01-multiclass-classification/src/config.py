"""Shared settings for the classification pipeline."""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"
FIGURES_DIR = ROOT_DIR / "reports" / "figures"

# Iris dataset: 150 samples, 4 numeric features, 3 balanced classes
DATASET_FILE = RAW_DATA_DIR / "dataset.csv"
TARGET_COLUMN = "species"

TEST_SIZE = 0.2
RANDOM_STATE = 42
