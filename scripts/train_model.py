import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv(
    "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Features collected by the website
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

X = df[features].copy()

y = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})

# Encode categorical variables
X = pd.get_dummies(
    X,
    columns=["OverTime", "JobRole"],
    dtype=int
)

feature_columns = X.columns.tolist()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    eval_metric="logloss",
    random_state=42
)

model.fit(X_train, y_train)

# Evaluation
predictions = model.predict(X_test)

print(classification_report(y_test, predictions))

# Save model
os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/xgboost_attrition_model.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

joblib.dump(
    feature_columns,
    "models/feature_columns.pkl"
)

print("Model successfully trained!")
print("Number of features:", len(feature_columns))