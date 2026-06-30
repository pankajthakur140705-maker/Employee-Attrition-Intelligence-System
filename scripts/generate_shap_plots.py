import os
import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"

MODEL_PATH = "models/xgboost_attrition_model.pkl"
FEATURES_PATH = "models/feature_columns.pkl"

OUTPUT_DIR = "outputs/shap"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

model = joblib.load(
    MODEL_PATH
)

feature_columns = joblib.load(
    FEATURES_PATH
)

df = pd.read_csv(
    DATA_PATH
)

df = df.drop(
    columns=["Attrition"]
)

df = pd.get_dummies(df)

df = df.reindex(
    columns=feature_columns,
    fill_value=0
)

explainer = shap.Explainer(
    model,
    df
)

shap_values = explainer(df)
plt.figure()

shap.plots.beeswarm(
    shap_values,
    show=False
)

plt.savefig(
    f"{OUTPUT_DIR}/shap_summary.png",
    bbox_inches="tight"
)

plt.close()

plt.figure()

shap.plots.bar(
    shap_values,
    show=False
)

plt.savefig(
    f"{OUTPUT_DIR}/shap_bar.png",
    bbox_inches="tight"
)

plt.close()

print(
    "SHAP plots saved successfully."
)