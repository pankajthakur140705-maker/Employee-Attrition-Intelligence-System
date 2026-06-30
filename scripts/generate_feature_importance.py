import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

MODEL_PATH = "models/xgboost_attrition_model.pkl"
FEATURES_PATH = "models/feature_columns.pkl"

OUTPUT_DIR = "outputs/evaluation"

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

importance = model.feature_importances_

importance_df = pd.DataFrame(
    {
        "Feature": feature_columns,
        "Importance": importance
    }
)

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

importance_df.to_csv(
    f"{OUTPUT_DIR}/feature_importance.csv",
    index=False
)

plt.figure(
    figsize=(12, 8)
)

top_features = importance_df.head(15)

plt.barh(
    top_features["Feature"],
    top_features["Importance"]
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIR}/feature_importance.png"
)

plt.close()

print(
    "Feature importance generated successfully."
)