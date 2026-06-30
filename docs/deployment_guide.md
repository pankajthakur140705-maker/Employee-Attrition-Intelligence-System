# 🚀 Deployment Guide

# Employee Attrition Intelligence System

This guide explains how to set up and run the Employee Attrition Intelligence System on a local machine.

---

# 1. Prerequisites

Install the following software:

- Python 3.10+
- VS Code
- Git (Optional)

Verify installation:

```bash
python --version
```

---

# 2. Clone Project

```bash
git clone <repository-url>
```

Move to project directory:

```bash
cd Employee_Attrition_System
```

---

# 3. Install Dependencies

Install all required libraries:

```bash
pip install -r requirements.txt
```

Required packages:

- streamlit
- pandas
- numpy
- scikit-learn
- xgboost
- shap
- matplotlib
- plotly
- google-generativeai
- python-dotenv
- joblib

---

# 4. Configure Gemini API

Create a file named:

```text
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get API Key from:

https://aistudio.google.com

---

# 5. Project Structure

```text
Employee_Attrition_System/
│
├── app/
├── src/
├── models/
├── data/
├── outputs/
├── scripts/
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

---

# 6. Run Streamlit Dashboard

Execute:

```bash
streamlit run app/app.py
```

The dashboard will open automatically in your browser.

Default URL:

```text
http://localhost:8501
```

---

# 7. Dashboard Modules

## Home Dashboard

Provides project overview and architecture.

---

## Attrition Prediction

Predicts employee attrition risk using the trained XGBoost model.

---

## Explainable AI

Displays feature importance and model interpretation.

---

## Recommendation Engine

Generates retention strategies based on employee risk factors.

---

## What-If Analysis

Simulates HR interventions and evaluates impact on attrition risk.

---

## Gemini HR Assistant

Provides AI-generated HR insights and recommendations.

---

## Model Evaluation Dashboard

Displays:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Feature Importance

---

# 8. Model Performance

| Metric | Score |
|----------|----------|
| Accuracy | 97.48% |
| Precision | 98.08% |
| Recall | 86.08% |
| F1 Score | 91.69% |

---

# 9. Generate Evaluation Outputs

Run:

```bash
python scripts/evaluate_model.py
```

Generate feature importance:

```bash
python scripts/generate_feature_importance.py
```

---

# 10. Troubleshooting

### Module Not Found

Install missing package:

```bash
pip install package_name
```

---

### Gemini Not Working

Verify:

```env
GEMINI_API_KEY
```

exists in `.env`.

---

### Model Not Found

Verify:

```text
models/
├── xgboost_attrition_model.pkl
├── scaler.pkl
└── feature_columns.pkl
```

exist.

---

### Dataset Not Found

Verify:

```text
data/
└── WA_Fn-UseC_-HR-Employee-Attrition.csv
```

exists.

---

# 11. Future Deployment

The system can be deployed using:

- Streamlit Cloud
- Render
- Railway
- AWS
- Azure
- Google Cloud

---

# Developer

Pankaj Thakur

B.Tech CSE (AI & Data Science)

Government Hydro Engineering College

Himachal Pradesh, India