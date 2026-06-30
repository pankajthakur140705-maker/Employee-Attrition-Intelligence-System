# 📘 Methodology

# Employee Attrition Intelligence System

---

# 1. Introduction

The Employee Attrition Intelligence System is designed to predict employee attrition risk and assist Human Resource (HR) teams in making proactive retention decisions.

The methodology combines:

- Data Preprocessing
- Feature Engineering
- Machine Learning
- Explainable AI
- Recommendation Generation
- What-If Analysis
- Generative AI

---

# 2. Dataset Description

Dataset Used:

IBM HR Analytics Employee Attrition Dataset

Dataset Characteristics:

- Total Records: 1470
- Features: 45+
- Target Variable: Attrition

Target Classes:

| Attrition Value | Meaning                 |
|-----------------|-------------------------|
| Yes             | Employee likely to leave|
| No              | Employee likely to stay |

---

# 3. Data Preprocessing

The raw dataset undergoes preprocessing before model training.

Steps:

### 3.1 Data Cleaning

- Missing value inspection
- Data validation
- Duplicate checking

### 3.2 Target Variable Encoding

Attrition values are converted:

```python
Yes → 1
No → 0
```

### 3.3 Feature Encoding

Categorical features are transformed using:

```text
One-Hot Encoding
```

Examples:

```text
Gender
Department
BusinessTravel
JobRole
OverTime
```

### 3.4 Feature Alignment

Input features are aligned with trained model columns using:

```python
reindex()
```

### 3.5 Feature Scaling

Numerical attributes are normalized using:

```text
StandardScaler
```

---

# 4. Feature Engineering

The processed dataset contains employee attributes including:

- Age
- Monthly Income
- Distance From Home
- Job Satisfaction
- Environment Satisfaction
- Work Life Balance
- Years Since Last Promotion
- OverTime

These features are transformed into model-ready numerical inputs.

---

# 5. Machine Learning Methodology

Three machine learning algorithms were evaluated.

## Models Evaluated

### Logistic Regression

Used as a baseline classification model.

Advantages:

- Fast training
- Easy interpretation

---

### Random Forest

Ensemble learning algorithm based on decision trees.

Advantages:

- Handles nonlinear relationships
- Robust to overfitting

---

### XGBoost

Gradient Boosting based ensemble algorithm.

Advantages:

- High predictive performance
- Efficient handling of structured data
- Feature importance generation

---

# 6. Model Comparison

The following models were trained and evaluated.

| Model | Accuracy (%) | Precision (%) | Recall (%) | F1 Score (%) |
|---------|---------:|---------:|---------:|---------:|
| Logistic Regression | 86.05 | 61.54 | 34.04 | 43.84 |
| Random Forest | 82.99 | 36.36 | 8.51 | 13.79 |
| XGBoost | 87.41 | 77.78 | 29.79 | 43.08 |

---

# 7. Model Selection

Based on experimental results, XGBoost achieved the highest predictive performance among the evaluated algorithms.

Therefore:

```text
Selected Model = XGBoost
```

Reasons:

- Highest accuracy
- Better precision
- Strong performance on structured HR data
- Built-in feature importance capability

---

# 8. Prediction Pipeline

The prediction workflow follows:

```text
Employee Input
      ↓
Preprocessing
      ↓
Feature Encoding
      ↓
Feature Scaling
      ↓
XGBoost Prediction
      ↓
Probability Score
      ↓
Risk Classification
```

Outputs:

- Prediction
- Probability
- Risk Score
- Risk Level

---

# 9. Explainable AI Methodology

To improve model transparency, explainability techniques are used.

Methods:

### Feature Importance Analysis

Provides:

- Important predictors
- Business interpretation
- HR insights

Top Factors:

- OverTime
- Monthly Income
- Job Satisfaction
- Work Life Balance
- Years Since Last Promotion
- Environment Satisfaction

---

# 10. Recommendation Engine

A rule-based recommendation system generates retention strategies.

Examples:

| Risk Factor | Recommendation |
|------------|---------------|
| Overtime | Reduce workload |
| Low Income | Compensation review |
| Low Satisfaction | Improve engagement |
| Promotion Delay | Career growth planning |

Purpose:

```text
Prediction → Action
```

---

# 11. What-If Analysis

The What-If Analysis module allows HR teams to simulate interventions.

Example Scenarios:

### Scenario 1

```text
Increase Salary
```

### Scenario 2

```text
Remove Overtime
```

### Scenario 3

```text
Improve Job Satisfaction
```

Outputs:

- Updated risk score
- Risk comparison
- Suggested intervention impact

---

# 12. Gemini HR Assistant

Google Gemini AI is integrated to provide conversational HR assistance.

Capabilities:

- Explain predictions
- Answer HR questions
- Suggest retention strategies
- Generate employee summaries

Workflow:

```text
User Query
      ↓
Prompt Engineering
      ↓
Gemini AI
      ↓
HR Response
```

---

# 13. Dashboard Implementation

The complete system is implemented using Streamlit.

Dashboard Modules:

1. Home
2. Prediction
3. Explainability
4. Recommendations
5. What-If Analysis
6. Gemini HR Assistant
7. Model Evaluation

---

# 14. System Output

The final system provides:

- Attrition Prediction
- Risk Classification
- Feature Importance
- Retention Recommendations
- What-If Analysis Results
- AI-Powered HR Assistance

---

# 15. Conclusion

The proposed methodology combines machine learning, explainable AI, recommendation systems, scenario simulation, and generative AI into a unified Employee Attrition Intelligence System.

Among the evaluated models, XGBoost achieved the best predictive performance and was selected as the final deployment model for supporting HR decision-making and employee retention strategies.