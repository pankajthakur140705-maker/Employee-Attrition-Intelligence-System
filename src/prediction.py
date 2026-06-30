import joblib
import pandas as pd
import numpy as np

MODEL_PATH = "models/xgboost_attrition_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURES_PATH = "models/feature_columns.pkl"

try:

    model = joblib.load(
        MODEL_PATH
    )

    scaler = joblib.load(
        SCALER_PATH
    )

    feature_columns = joblib.load(
        FEATURES_PATH
    )

except Exception as e:

    print(
        f"Model Loading Error: {e}"
    )

    model = None
    scaler = None
    feature_columns = []


def predict_attrition(input_df):

    if model is None:

        raise Exception(
            "Model not loaded."
        )

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    scaled_data = scaler.transform(
        input_df
    )

    prediction = model.predict(
        scaled_data
    )[0]

    probability = model.predict_proba(
        scaled_data
    )[0][1]

    risk_score = round(
        probability * 100,
        2
    )

    if risk_score >= 70:

        risk_level = "High"

    elif risk_score >= 40:

        risk_level = "Medium"

    else:

        risk_level = "Low"

    return (
        prediction,
        probability,
        risk_score,
        risk_level
    )


def get_top_factors(input_df):

    factors = []

    try:

        row = input_df.iloc[0]

        if (
            "OverTime" in input_df.columns
            and str(
                row["OverTime"]
            ) == "Yes"
        ):
            factors.append(
                "Excessive Overtime"
            )

        if (
            "MonthlyIncome"
            in input_df.columns
            and row["MonthlyIncome"]
            < 5000
        ):
            factors.append(
                "Low Monthly Income"
            )

        if (
            "JobSatisfaction"
            in input_df.columns
            and row["JobSatisfaction"]
            <= 2
        ):
            factors.append(
                "Low Job Satisfaction"
            )

        if (
            "WorkLifeBalance"
            in input_df.columns
            and row["WorkLifeBalance"]
            <= 2
        ):
            factors.append(
                "Poor Work-Life Balance"
            )

        if (
            "YearsSinceLastPromotion"
            in input_df.columns
            and row[
                "YearsSinceLastPromotion"
            ] >= 5
        ):
            factors.append(
                "Promotion Delay"
            )

        if (
            "EnvironmentSatisfaction"
            in input_df.columns
            and row[
                "EnvironmentSatisfaction"
            ] <= 2
        ):
            factors.append(
                "Poor Work Environment"
            )

        if (
            "DistanceFromHome"
            in input_df.columns
            and row[
                "DistanceFromHome"
            ] >= 20
        ):
            factors.append(
                "Long Commute Distance"
            )

        if (
            "Age"
            in input_df.columns
            and row["Age"] < 25
        ):
            factors.append(
                "Young Employee Risk"
            )

        if (
            "JobRole"
            in input_df.columns
        ):

            high_risk_roles = [
                "Sales Representative",
                "Laboratory Technician"
            ]

            if (
                str(
                    row["JobRole"]
                )
                in high_risk_roles
            ):
                factors.append(
                    f"High Risk Role ({row['JobRole']})"
                )

        if len(factors) == 0:

            factors.append(
                "No Significant Risk Factors"
            )

        return factors[:5]

    except Exception:

        return [
            "Unable to determine risk factors"
        ]


def get_risk_color(risk_score):

    if risk_score >= 70:
        return "red"

    elif risk_score >= 40:
        return "orange"

    else:
        return "green"


def generate_hr_summary(
    risk_score,
    risk_level,
    top_factors
):

    summary = f"""
Risk Level: {risk_level}

Risk Score: {risk_score}%

Top Risk Factors:
"""

    for factor in top_factors:

        summary += f"\n• {factor}"

    return summary