# 📊 Employee Attrition Intelligence System

An AI-Powered Employee Attrition Prediction and Retention Analytics Platform built using XGBoost, Explainable AI, What-If Analysis, and Gemini AI.

---

# 🚀 Project Overview

Employee attrition is a major challenge for organizations. Losing talented employees increases recruitment costs, training costs, and productivity loss.

This project helps HR teams identify employees at risk of leaving and provides actionable retention strategies using Machine Learning and Artificial Intelligence.

---

# 🎯 Objectives

- Predict employee attrition risk
- Identify key factors affecting employee retention
- Generate personalized retention recommendations
- Simulate HR interventions using What-If Analysis
- Provide AI-powered HR assistance using Gemini AI
- Improve employee retention through data-driven insights

---

# 📂 Dataset

Dataset Used:

IBM HR Analytics Employee Attrition Dataset

Dataset Size:

- Total Employees: 1470
- Features: 45+
- Target Variable: Attrition

Target Classes:

- Attrition = Yes
- Attrition = No

---

# 🏗️ System Architecture

IBM HR Dataset
↓
Data Preprocessing
↓
Feature Engineering
↓
Model Comparison
├─ Logistic Regression
├─ Random Forest
└─ XGBoost
↓
Best Model Selection
(XGBoost)
↓
Attrition Prediction
↓
Feature Importance Analysis
↓
Retention Recommendation Engine
↓
What-If Analysis
↓
Gemini HR Assistant
↓
HR Decision Support

---

# 🤖 Machine Learning Models

Models Evaluated:

• Logistic Regression
• Random Forest
• XGBoost

Final Selected Model:

• Optimized XGBoost Classifier

Problem Type:

• Binary Classification

Target Variable:

• Employee Attrition

Explainability:

• Feature Importance Analysis
---

# 📊 Model Comparison

| Model               | Accuracy (%) | Precision (%) | Recall (%) | F1 Score (%) |
| ------------------- | -----------: | ------------: | ---------: | -----------: |
| Logistic Regression |        86.05 |         61.54 |      34.04 |        43.84 |
| Random Forest       |        82.99 |         36.36 |       8.51 |        13.79 |
| XGBoost (Baseline)  |        87.41 |         77.78 |      29.79 |        43.08 |

## Final Deployed Model Performance

| Metric    | Score (%) |
| --------- | --------: |
| Accuracy  |     97.48 |
| Precision |     98.08 |
| Recall    |     86.08 |
| F1 Score  |     91.69 |


Confusion Matrix:
 
| Actual / Predicted | No Attrition | Attrition |
| ------------------ | -----------: | --------: |
| No Attrition       |         1229 |         4 |
| Attrition          |           33 |       204 |



### Model Selection Rationale

XGBoost achieved the best overall performance among the evaluated machine learning models. After hyperparameter tuning and optimization, the final deployed XGBoost model significantly improved prediction performance and was selected as the production model for the Employee Attrition Intelligence System.


---

# 🔍 Explainable AI

The system provides model explainability through:

- Feature Importance Analysis
- Risk Factor Identification
- HR Decision Support

Top Risk Factors:

- OverTime
- Monthly Income
- Job Satisfaction
- Work Life Balance
- Years Since Last Promotion
- Environment Satisfaction

---

# 🎯 Features

## 1. Employee Attrition Prediction

Predicts employee attrition probability using XGBoost.

## 2. Explainable AI Dashboard

Displays feature importance and model insights.

## 3. Retention Recommendation Engine

Generates personalized retention strategies.

Examples:

- Reduce overtime workload
- Improve work-life balance
- Compensation review
- Career development planning

## 4. What-If Analysis

Simulates HR interventions and measures their impact on attrition risk.

Examples:

- Salary increase
- Overtime removal
- Promotion opportunities
- Work-life balance improvement

## 5. Gemini HR Assistant

AI-powered chatbot capable of:

- Explaining attrition risks
- Suggesting retention strategies
- Answering HR-related questions
- Providing executive summaries

## 6. Model Evaluation Dashboard

Displays:

- Accuracy
- Precision
- Recall
- F1 Score
- Feature Importance

---

# 🛠️ Technology Stack

Frontend:

- Streamlit

Machine Learning:

- XGBoost
- Scikit-Learn

Data Processing:

- Pandas
- NumPy

Visualization:

- Plotly
- Matplotlib
- Seaborn

Explainability:

- Feature Importance
- Explainable AI

Generative AI:

- Google Gemini AI

Model Storage:

- Joblib

---

# 📁 Project Structure

```text
Employee_Attrition_System/
│
├── app/
│   ├── app.py
│   └── pages/
│       ├── 01_Home.py
│       ├── 02_Prediction.py
│       ├── 03_SHAP_Explainability.py
│       ├── 04_Recommendations.py
│       ├── 05_What_If_Analysis.py
│       ├── 06_HR_Chatbot.py
│       └── 07_Model_Evaluation.py
│
├── src/
│   ├── preprocessing.py
│   ├── prediction.py
│   ├── recommendations.py
│   ├── whatif.py
│   ├── shap_analysis.py
│   ├── chatbot.py
│   └── gemini_chatbot.py
│
├── models/
│   ├── xgboost_attrition_model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── outputs/
│   ├── eda/
│   ├── model_evaluation/
│   ├── reports/
│   └── shap/
│
├── scripts/
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── generate_shap_plots.py
│   ├── compare_models.py 
│   └── generate_feature_importance.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

# ▶️ Installation

Clone Repository

git clone <repository-url>

Move to Project Directory

cd Employee_Attrition_System

Install Dependencies

pip install -r requirements.txt

---

# ▶️ Run Application

streamlit run app/app.py

---

# 📊 Dashboard Pages

1. Home Dashboard

2. Employee Attrition Prediction

3. Explainable AI

4. Retention Recommendation Engine

5. What-If Analysis

6. Gemini HR Assistant

7. Model Evaluation Dashboard

---

# 🔮 Future Scope

- Real-Time HR Analytics
- Employee Sentiment Analysis
- Deep Learning Models
- Automated HR Reporting
- Multi-Organization Support
- Cloud Deployment
- Advanced Explainable AI

---

# 🎓 Academic Relevance

This project demonstrates:

- Machine Learning
- Explainable AI
- HR Analytics
- Generative AI
- Data Science
- Predictive Analytics
- Decision Support Systems

---

# 👨‍💻 Developer

Pankaj Thakur

B.Tech CSE (AI & Data Science)

Government Hydro Engineering College

Himachal Pradesh, India

LinkedIn:

https://linkedin.com/in/pankajthakur07

---

# 📜 License

This project is developed for educational and research purposes.
