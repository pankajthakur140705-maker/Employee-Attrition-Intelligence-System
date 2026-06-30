# 🏗️ Project Architecture

# Employee Attrition Intelligence System

---

# 1. System Overview

The Employee Attrition Intelligence System is an AI-powered HR analytics platform designed to predict employee attrition risk and provide intelligent retention recommendations.

The system integrates:

- Machine Learning Model Comparison
- Logistic Regression
- Random Forest
- XGBoost
- Explainable AI
- Recommendation Engine
- What-If Analysis
- Google Gemini AI
- Streamlit Dashboard

---

# 2. High-Level Architecture

```text
                IBM HR Analytics Dataset
                           │
                           ▼
                Data Preprocessing Layer
                           │
                           ▼
                 Feature Engineering
                           │
                           ▼
                  Model Comparison
          ┌──────────┬──────────┬──────────┐
          │          │          │
          ▼          ▼          ▼
    Logistic      Random    XGBoost
   Regression     Forest
          └──────────┴──────────┴──────────┘
                           │
                           ▼
               Best Model Selection
                     (XGBoost)
                           │
                           ▼
                  Prediction Engine
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
  Risk Assessment   Explainability   Evaluation Module
         │                 │                 │
         ▼                 ▼                 ▼
 Recommendations   Feature Importance   Performance Metrics
         │
         ▼
     What-If Analysis
         │
         ▼
   Gemini HR Assistant
         │
         ▼
    HR Decision Support
```

---

# 3. System Components

## 3.1 Data Layer

### Input Dataset

IBM HR Analytics Employee Attrition Dataset

Contains:

- Employee Demographics
- Compensation Information
- Satisfaction Scores
- Promotion History
- Overtime Information
- Job Roles

Output:

```text
Structured Employee Data
```

---

## 3.2 Preprocessing Layer

### Responsibilities

- Data Cleaning
- One-Hot Encoding
- Feature Alignment
- Feature Scaling

Implementation:

```python
create_employee_record()
```

File:

```text
src/preprocessing.py
```

Output:

```text
Preprocessed Feature Matrix
```

---

## 3.3 Machine Learning Layer

### Models Evaluated

1. Logistic Regression
2. Random Forest
3. XGBoost

### Model Comparison Results

| Model | Accuracy (%) |
|---------|---------:|
| Logistic Regression | 86.05 |
| Random Forest | 82.99 |
| XGBoost | 87.41 |

### Final Selected Model

```text
XGBoost Classifier
```

### Responsibilities

- Model Training
- Attrition Prediction
- Probability Estimation
- Risk Classification

Implementation:

```python
predict_attrition()
```

File:

```text
src/prediction.py
```

Outputs:

- Prediction
- Probability
- Risk Score
- Risk Level
- Top Risk Factors

---

## 3.4 Explainability Layer

### Purpose

Provide transparency and interpretability for model predictions.

### Techniques Used

- Feature Importance Analysis
- Risk Factor Identification
- Business Interpretation

Outputs:

- Important Features
- Business Insights
- HR Recommendations

Files:

```text
src/shap_analysis.py
scripts/generate_feature_importance.py
```

---

## 3.5 Recommendation Engine

### Purpose

Generate personalized retention strategies based on employee risk factors.

Examples:

- Reduce overtime
- Improve work-life balance
- Compensation review
- Promotion planning
- Career growth discussion

Implementation:

```python
generate_recommendations()
```

File:

```text
src/recommendations.py
```

Output:

```text
Retention Action Plan
```

---

## 3.6 What-If Analysis Engine

### Purpose

Simulate HR interventions and evaluate their impact on attrition risk.

### Example Scenarios

Scenario 1

```text
Increase Salary
```

Scenario 2

```text
Remove Overtime
```

Scenario 3

```text
Improve Job Satisfaction
```

Outputs:

- New Risk Score
- Risk Comparison
- Suggested Actions

File:

```text
src/whatif.py
```

---

## 3.7 Gemini HR Assistant

### Purpose

Provide AI-powered HR insights and decision support.

### Technology

Google Gemini AI

### Capabilities

- Explain attrition predictions
- Answer HR questions
- Generate executive summaries
- Suggest retention strategies
- Interpret employee risk

File:

```text
src/gemini_chatbot.py
```

Workflow:

```text
User Question
      │
      ▼
 Gemini Prompt
      │
      ▼
 Gemini Model
      │
      ▼
 HR Response
```

---

# 4. Dashboard Architecture

Built using:

```text
Streamlit
```

Dashboard Pages:

```text
01_Home.py

02_Prediction.py

03_SHAP_Explainability.py

04_Recommendations.py

05_What_If_Analysis.py

06_HR_Chatbot.py

07_Model_Evaluation.py
```

---

# 5. Data Flow Diagram

```text
Employee Input
      │
      ▼
Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Model Comparison
(Logistic Regression,
Random Forest,
XGBoost)
      │
      ▼
Best Model Selection
(XGBoost)
      │
      ▼
Risk Prediction
      │
      ├────────► Recommendation Engine
      │
      ├────────► What-If Analysis
      │
      ├────────► Feature Importance
      │
      │
      └────────► Gemini Assistant
                     │
                     ▼
              HR Decision Support
```

---

# 6. Project Folder Architecture

```text
Employee_Attrition_System/
│
├── app/
│
├── src/
│
├── models/
│
├── data/
│
├── outputs/
│
├── scripts/
│
├── docs/
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

---

# 7. Security Considerations

### Sensitive Information

- Gemini API Key

### Protection Method

```text
.env file
```

Excluded using:

```text
.gitignore
```

### Security Best Practices

- Do not expose API keys publicly
- Keep .env excluded from GitHub
- Store credentials separately from source code

---

# 8. Deployment Architecture

```text
Local Machine
      │
      ▼
Python Environment
      │
      ▼
Streamlit Application
      │
      ├── XGBoost Model
      ├── Feature Importance
      ├── Recommendation Engine
      ├── What-If Analysis
      ├── Gemini AI
      └── Model Comparison Results
```

---

# 9. Future Architecture Enhancements

Future improvements may include:

- SHAP-Based Explainability
- Real-Time HR Dashboard
- Employee Sentiment Analysis
- Deep Learning Models
- Cloud Deployment
- Multi-Organization Support
- Automated Reporting
- Ensemble Learning Models

---

# 10. Conclusion

The proposed architecture integrates model comparison, optimized XGBoost prediction, explainable AI through feature importance analysis, recommendation generation, What-If Analysis, and Gemini-powered HR assistance into a unified Employee Attrition Intelligence System.

Among the evaluated machine learning algorithms, XGBoost achieved the highest predictive performance and was selected as the final deployment model.

The architecture supports data-driven HR decision-making and provides actionable employee retention insights through a modern AI-powered analytics platform.