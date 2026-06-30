import joblib
import shap
import pandas as pd

MODEL_PATH = "models/xgboost_attrition_model.pkl"

try:

    model = joblib.load(
        MODEL_PATH
    )

    explainer = shap.TreeExplainer(
        model
    )

except Exception as e:

    print(
        f"SHAP Initialization Error: {e}"
    )

    model = None
    explainer = None


def get_explainer():

    return explainer


def get_shap_values(input_df):

    if explainer is None:

        raise Exception(
            "SHAP Explainer not initialized."
        )

    shap_values = explainer.shap_values(
        input_df
    )

    return shap_values


def get_feature_importance(input_df):

    if explainer is None:

        return pd.DataFrame(
            {
                "Feature": [],
                "Importance": []
            }
        )

    shap_values = explainer.shap_values(
        input_df
    )

    importance_df = pd.DataFrame(
        {
            "Feature": input_df.columns,
            "Importance": abs(
                shap_values
            ).mean(axis=0)
        }
    )

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    return importance_df


def get_top_shap_features(
    input_df,
    top_n=5
):

    importance_df = get_feature_importance(
        input_df
    )

    return (
        importance_df
        .head(top_n)["Feature"]
        .tolist()
    )


def explain_employee(
    input_df
):

    if explainer is None:

        return {
            "status": "error",
            "message": "SHAP Explainer not available."
        }

    shap_values = explainer.shap_values(
        input_df
    )

    feature_importance = pd.DataFrame(
        {
            "Feature": input_df.columns,
            "SHAP_Value": shap_values[0]
        }
    )

    feature_importance[
        "Abs_SHAP"
    ] = abs(
        feature_importance[
            "SHAP_Value"
        ]
    )

    feature_importance = (
        feature_importance
        .sort_values(
            by="Abs_SHAP",
            ascending=False
        )
    )

    return {
        "status": "success",
        "top_features":
            feature_importance
            .head(5)
            .to_dict(
                orient="records"
            )
    }