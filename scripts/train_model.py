
"""
Employee Attrition Intelligence System
Model Training and Evaluation Script

Dataset:
IBM HR Analytics Employee Attrition Dataset

Models:
1. Logistic Regression
2. Random Forest
3. XGBoost

Training configuration:
- 80:20 train-test split
- Stratified sampling
- Random state: 42
- One-hot encoding
- StandardScaler
"""

import joblib
import pandas as pd

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from xgboost import XGBClassifier


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

MODEL_DIR = PROJECT_ROOT / "models"

OUTPUT_DIR = (
    PROJECT_ROOT
    / "outputs"
    / "evaluation"
)

MODEL_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

print("\nLoading IBM HR Analytics dataset...")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}"
    )

df = pd.read_csv(DATA_PATH)

print("Dataset shape:", df.shape)

if "Attrition" not in df.columns:
    raise ValueError(
        "Target column 'Attrition' is missing."
    )

print("Total employee records:", len(df))


# --------------------------------------------------
# SELECT FEATURES
# --------------------------------------------------

features = [
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

missing_columns = [
    column
    for column in features
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required features: {missing_columns}"
    )

X = df[features].copy()

y = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})

if y.isna().any():
    raise ValueError(
        "Target column contains missing or unexpected values."
    )


# --------------------------------------------------
# ENCODE CATEGORICAL FEATURES
# --------------------------------------------------

print("\nEncoding categorical variables...")

X = pd.get_dummies(
    X,
    columns=["OverTime", "JobRole"],
    dtype=int
)

feature_columns = X.columns.tolist()

print("Number of encoded features:", len(feature_columns))


# --------------------------------------------------
# TRAIN-TEST SPLIT
# --------------------------------------------------

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# --------------------------------------------------
# FEATURE SCALING
# --------------------------------------------------

print("\nApplying StandardScaler...")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# DEFINE MODELS
# --------------------------------------------------

models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        eval_metric="logloss",
        random_state=42
    )
}


# --------------------------------------------------
# TRAIN AND EVALUATE MODELS
# --------------------------------------------------

print("\nTraining and evaluating models...")

evaluation_results = []
trained_models = {}

for model_name, model in models.items():

    print(f"\nTraining {model_name}...")

    model.fit(
        X_train_scaled,
        y_train
    )

    predictions = model.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    evaluation_results.append({
        "Model": model_name,
        "Accuracy (%)": round(accuracy * 100, 2),
        "Precision (%)": round(precision * 100, 2),
        "Recall (%)": round(recall * 100, 2),
        "F1 Score (%)": round(f1 * 100, 2)
    })

    trained_models[model_name] = model

    print(f"\n{model_name} Results")
    print("-" * 40)

    print(
        classification_report(
            y_test,
            predictions,
            target_names=["No Attrition", "Attrition"],
            zero_division=0
        )
    )


# --------------------------------------------------
# SAVE MODEL COMPARISON RESULTS
# --------------------------------------------------

results_df = pd.DataFrame(evaluation_results)

results_df = results_df.sort_values(
    by="Accuracy (%)",
    ascending=False
)

results_path = OUTPUT_DIR / "model_evaluation.csv"

results_df.to_csv(
    results_path,
    index=False
)

print("\nMODEL COMPARISON")
print("=" * 60)
print(results_df.to_string(index=False))


# --------------------------------------------------
# SAVE FINAL XGBOOST MODEL
# --------------------------------------------------

print("\nSaving final XGBoost model...")

final_model = trained_models["XGBoost"]

joblib.dump(
    final_model,
    MODEL_DIR / "xgboost_attrition_model.pkl"
)

joblib.dump(
    scaler,
    MODEL_DIR / "scaler.pkl"
)

joblib.dump(
    feature_columns,
    MODEL_DIR / "feature_columns.pkl"
)


# --------------------------------------------------
# XGBOOST CONFUSION MATRIX
# --------------------------------------------------

xgb_predictions = final_model.predict(
    X_test_scaled
)

cm = confusion_matrix(
    y_test,
    xgb_predictions,
    labels=[0, 1]
)

confusion_df = pd.DataFrame(
    cm,
    index=["Actual No Attrition", "Actual Attrition"],
    columns=["Predicted No Attrition", "Predicted Attrition"]
)

confusion_path = OUTPUT_DIR / "confusion_matrix.csv"

confusion_df.to_csv(confusion_path)

print("\nXGBOOST CONFUSION MATRIX")
print(confusion_df)


# --------------------------------------------------
# XGBOOST FEATURE IMPORTANCE
# --------------------------------------------------

print("\nGenerating XGBoost feature importance...")

importance_df = pd.DataFrame({
    "Feature": feature_columns,
    "Importance": final_model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
).reset_index(drop=True)

importance_path = OUTPUT_DIR / "feature_importance.csv"

importance_df.to_csv(
    importance_path,
    index=False
)

print("\nTOP 15 IMPORTANT FEATURES")
print(
    importance_df.head(15).to_string(index=False)
)


# --------------------------------------------------
# SAVE CLASSIFICATION REPORT
# --------------------------------------------------

report = classification_report(
    y_test,
    xgb_predictions,
    target_names=["No Attrition", "Attrition"],
    zero_division=0
)

report_path = OUTPUT_DIR / "xgboost_classification_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)


# --------------------------------------------------
# FINAL SUMMARY
# --------------------------------------------------

print("\n" + "=" * 60)
print("MODEL TRAINING COMPLETED")
print("=" * 60)

print("Final deployment model: XGBoost")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Encoded features:", len(feature_columns))

print("\nSaved model artifacts:")
print(" - models/xgboost_attrition_model.pkl")
print(" - models/scaler.pkl")
print(" - models/feature_columns.pkl")

print("\nSaved evaluation outputs:")
print(" - outputs/evaluation/model_evaluation.csv")
print(" - outputs/evaluation/confusion_matrix.csv")
print(" - outputs/evaluation/feature_importance.csv")
print(" - outputs/evaluation/xgboost_classification_report.txt")

print("\nTraining completed successfully!")
