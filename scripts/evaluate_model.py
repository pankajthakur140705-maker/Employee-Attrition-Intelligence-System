import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

DATA_PATH = "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"

MODEL_PATH = "models/xgboost_attrition_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURES_PATH = "models/feature_columns.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_columns = joblib.load(FEATURES_PATH)

df = pd.read_csv(DATA_PATH)

df["Attrition"] = df["Attrition"].map(
    {
        "Yes": 1,
        "No": 0
    }
)

y = df["Attrition"]

X = df.drop(
    columns=["Attrition"]
)

X = pd.get_dummies(X)

X = X.reindex(
    columns=feature_columns,
    fill_value=0
)

X_scaled = scaler.transform(X)

predictions = model.predict(X_scaled)

print("\nAccuracy:")
print(
    accuracy_score(
        y,
        predictions
    )
)

print("\nPrecision:")
print(
    precision_score(
        y,
        predictions
    )
)

print("\nRecall:")
print(
    recall_score(
        y,
        predictions
    )
)

print("\nF1 Score:")
print(
    f1_score(
        y,
        predictions
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y,
        predictions
    )
)

print("\nClassification Report:")
print(
    classification_report(
        y,
        predictions
    )
)