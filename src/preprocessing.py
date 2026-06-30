import pandas as pd
import joblib

FEATURES_PATH = "models/feature_columns.pkl"

try:

    feature_columns = joblib.load(
        FEATURES_PATH
    )

except Exception as e:

    print(
        f"Feature Loading Error: {e}"
    )

    feature_columns = []


def create_employee_record(
    employee_data
):

    defaults = {

        "Age": 30,

        "MonthlyIncome": 10000,

        "DistanceFromHome": 5,

        "OverTime": "No",

        "JobRole": "Research Scientist",

        "JobSatisfaction": 3,

        "WorkLifeBalance": 3,

        "YearsSinceLastPromotion": 2,

        "EnvironmentSatisfaction": 3
    }

    for key, value in defaults.items():

        if key not in employee_data:

            employee_data[key] = value

    df = pd.DataFrame(
        [employee_data]
    )

    categorical_columns = [

        "OverTime",

        "JobRole"
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_columns
    )

    if len(feature_columns) > 0:

        df = df.reindex(
            columns=feature_columns,
            fill_value=0
        )

    return df


def validate_employee_data(
    employee_data
):

    errors = []

    if employee_data.get(
        "Age",
        30
    ) < 18:

        errors.append(
            "Age must be at least 18."
        )

    if employee_data.get(
        "MonthlyIncome",
        10000
    ) <= 0:

        errors.append(
            "Monthly Income must be positive."
        )

    if employee_data.get(
        "DistanceFromHome",
        5
    ) < 0:

        errors.append(
            "Distance From Home cannot be negative."
        )

    return errors


def employee_summary(
    employee_data
):

    summary = pd.DataFrame(
        employee_data.items(),
        columns=[
            "Feature",
            "Value"
        ]
    )

    return summary