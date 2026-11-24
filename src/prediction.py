
import joblib
import pandas as pd
import numpy as np

from pathlib import Path


# ==========================================
# PROJECT CONFIGURATION
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODEL_DIR = PROJECT_ROOT / "models"

MODEL_PATH = MODEL_DIR / "xgboost_attrition_model.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
FEATURES_PATH = MODEL_DIR / "feature_columns.pkl"


# ==========================================
# LOAD TRAINED MODEL AND ARTIFACTS
# ==========================================

def load_model_artifacts():

    required_files = [
        MODEL_PATH,
        SCALER_PATH,
        FEATURES_PATH
    ]

    for file_path in required_files:

        if not file_path.exists():

            raise FileNotFoundError(
                f"Required model artifact not found: {file_path}"
            )

    loaded_model = joblib.load(MODEL_PATH)
    loaded_scaler = joblib.load(SCALER_PATH)
    loaded_features = joblib.load(FEATURES_PATH)

    loaded_features = list(loaded_features)

    if not loaded_features:

        raise ValueError(
            "Training feature columns are empty."
        )

    if len(loaded_features) != len(set(loaded_features)):

        raise ValueError(
            "Duplicate feature columns detected."
        )

    if not hasattr(loaded_model, "predict_proba"):

        raise TypeError(
            "The trained model must support predict_proba()."
        )

    if not hasattr(loaded_scaler, "transform"):

        raise TypeError(
            "The saved scaler does not support transform()."
        )

    if hasattr(loaded_scaler, "n_features_in_"):

        if loaded_scaler.n_features_in_ != len(loaded_features):

            raise ValueError(
                "Scaler feature count does not match "
                "the saved training feature columns."
            )

    return (
        loaded_model,
        loaded_scaler,
        loaded_features
    )


# Load artifacts once when the module is imported.

try:

    model, scaler, feature_columns = load_model_artifacts()

    MODEL_LOADED = True

    print(
        "Employee Attrition XGBoost model loaded successfully."
    )

except Exception as e:

    model = None
    scaler = None
    feature_columns = []

    MODEL_LOADED = False

    MODEL_LOADING_ERROR = str(e)

    print(
        f"Model Loading Error: {MODEL_LOADING_ERROR}"
    )


# ==========================================
# VALIDATE EMPLOYEE INPUT
# ==========================================

def prepare_input(input_df):

    if not MODEL_LOADED:

        raise RuntimeError(
            f"Model could not be loaded: "
            f"{MODEL_LOADING_ERROR}"
        )

    if not isinstance(input_df, pd.DataFrame):

        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    if input_df.empty:

        raise ValueError(
            "Employee input cannot be empty."
        )

    # Align with exact training feature columns.

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    input_df = input_df.apply(
        pd.to_numeric,
        errors="raise"
    )

    if input_df.isnull().any().any():

        raise ValueError(
            "Missing values found in employee input."
        )

    if not np.isfinite(
        input_df.to_numpy(dtype=float)
    ).all():

        raise ValueError(
            "Input contains infinite or invalid values."
        )

    return input_df


# ==========================================
# EMPLOYEE ATTRITION PREDICTION
# ==========================================

def predict_attrition(input_df):

    """
    Predict employee attrition using the trained XGBoost model.

    Returns:
        prediction: 0 or 1
        probability: Attrition probability
        risk_score: Probability expressed as percentage
        risk_level: Low / Medium / High
    """

    input_df = prepare_input(input_df)

    # Apply the saved StandardScaler exactly once.

    scaled_data = scaler.transform(
        input_df
    )

    # Generate binary prediction.

    prediction = int(
        model.predict(scaled_data)[0]
    )

    # Obtain class probabilities.

    probabilities = model.predict_proba(
        scaled_data
    )[0]

    # Identify the probability corresponding to Attrition = 1.

    classes = list(model.classes_)

    if 1 not in classes:

        raise ValueError(
            "The trained model does not contain "
            "the positive attrition class (1)."
        )

    attrition_index = classes.index(1)

    probability = float(
        probabilities[attrition_index]
    )

    # Convert probability into percentage.

    risk_score = round(
        probability * 100,
        2
    )

    # ======================================
    # RISK CATEGORIZATION
    # As documented in the project report
    # ======================================

    if risk_score >= 70:

        risk_level = "High"

    elif risk_score >= 30:

        risk_level = "Medium"

    else:

        risk_level = "Low"

    return (
        prediction,
        probability,
        risk_score,
        risk_level
    )


# ==========================================
# FEATURE IMPORTANCE ANALYSIS
# ==========================================

def get_feature_importance():

    """
    Extract global feature importance from
    the trained XGBoost classifier.

    This is model-based feature importance,
    not SHAP or individual-level attribution.
    """

    if not MODEL_LOADED:

        raise RuntimeError(
            "XGBoost model is not loaded."
        )

    if not hasattr(model, "feature_importances_"):

        raise AttributeError(
            "The trained model does not expose "
            "feature_importances_."
        )

    importance_values = model.feature_importances_

    if len(importance_values) != len(feature_columns):

        raise ValueError(
            "Feature importance length does not match "
            "the training feature columns."
        )

    importance_df = pd.DataFrame({

        "Feature": feature_columns,

        "Importance": importance_values

    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    ).reset_index(drop=True)

    return importance_df


# ==========================================
# GET TOP INFLUENTIAL FEATURES
# ==========================================

def get_top_factors(input_df=None, top_n=5):

    """
    Return the most influential features according
    to the trained XGBoost model.

    These are global model-level importance rankings,
    not employee-specific causal explanations.
    """

    importance_df = get_feature_importance()

    importance_df = importance_df[
        importance_df["Importance"] > 0
    ]

    importance_df = importance_df.head(
        top_n
    )

    if importance_df.empty:

        return [
            "No significant feature importance available."
        ]

    feature_mapping = {

        "OverTime_Yes": "Overtime",

        "OverTime_No": "Overtime Status",

        "MonthlyIncome": "Monthly Income",

        "JobSatisfaction": "Job Satisfaction",

        "WorkLifeBalance": "Work-Life Balance",

        "YearsSinceLastPromotion": "Years Since Last Promotion",

        "EnvironmentSatisfaction": "Environment Satisfaction",

        "Age": "Employee Age",

        "DistanceFromHome": "Distance From Home",

        "JobRole_Sales Representative": "Sales Representative Role",

        "JobRole_Laboratory Technician": "Laboratory Technician Role",

        "JobRole_Research Scientist": "Research Scientist Role"

    }

    factors = []

    for feature in importance_df["Feature"]:

        readable_name = feature_mapping.get(
            feature,
            feature.replace("_", " ")
        )

        factors.append(
            readable_name
        )

    return factors


# ==========================================
# RISK COLOR
# ==========================================

def get_risk_color(risk_score):

    if risk_score >= 70:

        return "red"

    elif risk_score >= 30:

        return "orange"

    else:

        return "green"


# ==========================================
# GENERATE HR SUMMARY
# ==========================================

def generate_hr_summary(
    risk_score,
    risk_level,
    top_factors
):

    summary = f"""
EMPLOYEE ATTRITION RISK SUMMARY

Risk Score: {risk_score}%

Risk Level: {risk_level}

Important Model Features:
"""

    for index, factor in enumerate(
        top_factors,
        start=1
    ):

        summary += f"\n{index}. {factor}"

    summary += """

Note:
Feature importance indicates global model influence.
It does not establish causation or prove that an
individual employee will leave.
"""

    return summary


# ==========================================
# MODEL STATUS
# ==========================================

def get_model_status():

    return {

        "loaded": MODEL_LOADED,

        "model": "XGBoost",

        "features": len(feature_columns),

        "error": (
            None
            if MODEL_LOADED
            else MODEL_LOADING_ERROR
        )

    }
