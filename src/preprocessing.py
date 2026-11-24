
"""
Employee Attrition Intelligence System
Employee Data Preprocessing Module

Preprocessing must remain consistent with scripts/train_model.py.

Training features:
- Age
- MonthlyIncome
- DistanceFromHome
- OverTime
- JobRole
- JobSatisfaction
- WorkLifeBalance
- YearsSinceLastPromotion
- EnvironmentSatisfaction
"""

import joblib
import pandas as pd

from pathlib import Path


# --------------------------------------------------
# PROJECT CONFIGURATION
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODEL_DIR = PROJECT_ROOT / "models"

FEATURE_PATH = MODEL_DIR / "feature_columns.pkl"


# --------------------------------------------------
# REQUIRED EMPLOYEE INPUT FIELDS
# --------------------------------------------------

REQUIRED_INPUT_FIELDS = [
    "Age",
    "MonthlyIncome",
    "DistanceFromHome",
    "OverTime",
    "JobRole",
    "JobSatisfaction",
    "WorkLifeBalance",
    "YearsSinceLastPromotion",
    "EnvironmentSatisfaction"
]

CATEGORICAL_COLUMNS = [
    "OverTime",
    "JobRole"
]


# --------------------------------------------------
# LOAD TRAINING FEATURE COLUMNS
# --------------------------------------------------

def load_feature_columns():

    if not FEATURE_PATH.exists():
        raise FileNotFoundError(
            f"Feature columns file not found: {FEATURE_PATH}"
        )

    columns = joblib.load(FEATURE_PATH)

    if not isinstance(columns, (list, tuple, pd.Index)):
        raise TypeError(
            "feature_columns.pkl must contain a list, tuple "
            "or pandas Index of training feature names."
        )

    columns = list(columns)

    if not columns:
        raise ValueError(
            "Training feature columns are empty."
        )

    if len(columns) != len(set(columns)):
        raise ValueError(
            "Duplicate feature names found in feature_columns.pkl."
        )

    return columns


feature_columns = load_feature_columns()


# --------------------------------------------------
# VALIDATE EMPLOYEE INPUT
# --------------------------------------------------

def validate_employee_data(employee_data):

    if not isinstance(employee_data, dict):
        raise TypeError(
            "Employee data must be provided as a dictionary."
        )

    if not employee_data:
        raise ValueError(
            "Employee data cannot be empty."
        )

    missing_fields = [
        field
        for field in REQUIRED_INPUT_FIELDS
        if field not in employee_data
    ]

    if missing_fields:
        raise ValueError(
            f"Missing required employee fields: {missing_fields}"
        )

    for field in REQUIRED_INPUT_FIELDS:

        value = employee_data[field]

        if value is None:
            raise ValueError(
                f"Employee field '{field}' cannot be empty."
            )

        if isinstance(value, str) and not value.strip():
            raise ValueError(
                f"Employee field '{field}' cannot be empty."
            )

    # Validate categorical values against training columns.
    overtime_values = {
        column.replace("OverTime_", "", 1)
        for column in feature_columns
        if column.startswith("OverTime_")
    }

    job_role_values = {
        column.replace("JobRole_", "", 1)
        for column in feature_columns
        if column.startswith("JobRole_")
    }

    if employee_data["OverTime"] not in overtime_values:
        raise ValueError(
            "Invalid OverTime value. Expected one of: "
            f"{sorted(overtime_values)}"
        )

    if employee_data["JobRole"] not in job_role_values:
        raise ValueError(
            "Invalid JobRole value. Expected one of: "
            f"{sorted(job_role_values)}"
        )


# --------------------------------------------------
# EMPLOYEE DATA PREPROCESSING
# --------------------------------------------------

def create_employee_record(employee_data):

    """
    Convert employee information into a model-ready DataFrame.

    Processing:
    1. Validate required employee fields.
    2. Convert dictionary into DataFrame.
    3. One-hot encode categorical variables.
    4. Align columns with saved training feature columns.
    5. Fill absent one-hot columns with zero.
    6. Validate final numeric data.

    Scaling is handled separately in prediction.py.
    """

    validate_employee_data(employee_data)

    # Create DataFrame
    df = pd.DataFrame([employee_data])

    # One-hot encode categorical features
    df = pd.get_dummies(
        df,
        columns=CATEGORICAL_COLUMNS,
        dtype=int
    )

    # Convert all values to numeric
    for column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="raise"
        )

    # Align with exact training feature order
    df = df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Validate missing values
    if df.isnull().any().any():
        raise ValueError(
            "Missing values detected after preprocessing."
        )

    # Validate numeric types
    if not all(
        pd.api.types.is_numeric_dtype(dtype)
        for dtype in df.dtypes
    ):
        raise TypeError(
            "All model features must be numeric."
        )

    # Validate finite values
    if not (
        df.select_dtypes(include="number")
        .map(lambda value: pd.notna(value) and abs(value) != float("inf"))
        .all()
        .all()
    ):
        raise ValueError(
            "Invalid or infinite numeric values detected."
        )

    return df


# --------------------------------------------------
# FEATURE INFORMATION
# --------------------------------------------------

def get_feature_count():

    return len(feature_columns)


def get_feature_names():

    return feature_columns.copy()
