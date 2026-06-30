# 📘 Methodology

# Employee Attrition Intelligence System

---

# 1. Introduction

The Employee Attrition Intelligence System is an AI-powered HR analytics platform designed to predict employee attrition and provide actionable retention strategies.

The system combines:

- Machine Learning
- Explainable AI
- HR Analytics
- Generative AI (Gemini)

to assist HR professionals in identifying employees at risk of leaving an organization.

---

# 2. Dataset

## Dataset Used

IBM HR Analytics Employee Attrition Dataset

## Dataset Characteristics

| Attribute       | Value                 |
|-----------------|-----------------------|
| Employees       | 1470                  |
| Features        | 35+                   |
| Target Variable | Attrition             |
| Type            | Binary Classification |

Target Classes:

- Attrition = Yes
- Attrition = No

---

# 3. Data Preprocessing

Raw employee data cannot be directly used by machine learning algorithms.

The following preprocessing steps were performed:

### 3.1 Missing Value Handling

- Dataset inspected for null values
- No significant missing values found

### 3.2 Encoding

Categorical variables converted using:

- One-Hot Encoding

Examples:

- OverTime
- JobRole
- MaritalStatus
- Department

---

### 3.3 Feature Alignment

Features were aligned with trained model columns using:

```python
reindex(columns=feature_columns)
```

This ensures prediction inputs match training data.

---

### 3.4 Scaling

Numerical features were normalized using:

```text
StandardScaler
```

Features scaled:

- Age
- MonthlyIncome
- DistanceFromHome
- YearsSinceLastPromotion

---

# 4. Feature Engineering

The following employee attributes were selected as important predictors:

- Age
- Monthly Income
- Distance From Home
- OverTime
- Job Satisfaction
- Work Life Balance
- Environment Satisfaction
- Years Since Last Promotion
- Job Role

These features significantly influence employee retention behavior.

---

# 5. Machine Learning Model

## Selected Algorithm

XGBoost Classifier

### Why XGBoost?

- High predictive accuracy
- Handles structured HR data effectively
- Prevents overfitting
- Fast training and prediction
- Supports feature importance analysis

---

## Classification Objective

Predict:

```text
Employee Attrition
```

Output:

```text
0 = Employee Stays

1 = Employee Leaves
```

---

# 6. Model Training Process

Workflow:

Dataset
↓
Preprocessing
↓
Feature Engineering
↓
Train-Test Split
↓
XGBoost Training
↓
Evaluation
↓
Deployment

---

## Train-Test Split

```text
80% Training Data

20% Testing Data
```

---

# 7. Hyperparameter Optimization

Bayesian Optimization was used to improve model performance.

Optimized parameters:

- Learning Rate
- Max Depth
- Number of Estimators
- Subsample
- Column Sample Rate

Benefits:

- Improved accuracy
- Better generalization
- Reduced overfitting

---

# 8. Model Evaluation

Performance metrics used:

### Accuracy

Measures overall prediction correctness.

Formula:

Accuracy = Correct Predictions / Total Predictions

---

### Precision

Measures correctness of positive predictions.

Formula:

Precision = TP / (TP + FP)

---

### Recall

Measures ability to identify actual attrition cases.

Formula:

Recall = TP / (TP + FN)

---

### F1 Score

Balances Precision and Recall.

Formula:

F1 = 2 × (Precision × Recall) / (Precision + Recall)


---

# 9. Model Comparison

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 86.05%   |
| Random Forest       | 82.99%   |
| XGBoost             | 87.41%   |

---

# 10. Model Performance

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 97.48% |
| Precision | 98.08% |
| Recall    | 86.08% |
| F1 Score  | 91.69% |

Confusion Matrix:

```text
[[1229    4]
 [  33  204]]
```

---

# 11. Explainable AI

To improve transparency, feature importance analysis was implemented.

Top risk factors identified:

- OverTime
- Monthly Income
- Job Satisfaction
- Work Life Balance
- Years Since Last Promotion
- Environment Satisfaction

Benefits:

- Better HR decision-making
- Increased trust in predictions
- Improved interpretability

---

# 12. Retention Recommendation Engine

The system generates personalized HR recommendations.

Examples:

### High Overtime

Recommendation:

```text
Reduce overtime workload
```

### Low Salary

Recommendation:

```text
Review compensation package
```

### Promotion Delay

Recommendation:

```text
Discuss career growth opportunities
```

---

# 13. What-If Analysis

The What-If Analysis module allows HR teams to simulate interventions.

Examples:

- Increase salary
- Remove overtime
- Improve satisfaction
- Offer promotion

The model recalculates attrition risk for each scenario.

Benefits:

- Scenario planning
- Retention strategy testing
- Data-driven decision making

---

# 14. Gemini HR Assistant

Google Gemini AI was integrated to provide intelligent HR insights.

Capabilities:

- Explain attrition predictions
- Summarize employee risk
- Suggest retention actions
- Answer HR-related questions

Benefits:

- Natural language interaction
- Executive-level summaries
- Enhanced decision support

---

# 15. System Deployment

Frontend:

- Streamlit

Backend:

- Python

Model Storage:

- Joblib

Generative AI:

- Google Gemini

---

# 16. Conclusion

The proposed Employee Attrition Intelligence System successfully predicts employee attrition risk with high accuracy and provides actionable HR insights using machine learning, explainable AI, and generative AI.

The system can help organizations reduce attrition, improve employee retention, and support data-driven HR decision-making.
