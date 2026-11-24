import pandas as pd
import joblib
from pathlib import Path

# Project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Load trained model feature columns
FEATURE_PATH = PROJECT_ROOT / "models" / "feature_columns.pkl"

feature_columns = joblib.load(FEATURE_PATH)


def create_employee_record(employee_data):

    # Convert employee input into DataFrame
    df = pd.DataFrame([employee_data])

    # Encode categorical variables
    df = pd.get_dummies(
        df,
        columns=["OverTime", "JobRole"],
        dtype=int
    )

    # Match the exact training features
    df = df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    return df