# 🏗️ Project Architecture

# Employee Attrition Intelligence System

---

# 1. System Overview

The Employee Attrition Intelligence System is an AI-powered HR analytics platform designed to predict employee attrition and provide intelligent retention recommendations.

The system integrates:

- Machine Learning Model Comparison
- Logistic Regression
- Random Forest
- XGBoost
- Explainable AI
- What-If Analysis
- Recommendation Engine
- Google Gemini AI
- Streamlit Dashboard

---

# 2. High-Level Architecture
```text

`                IBM HR Analytics Dataset
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
      Logistic     Random      XGBoost
     Regression    Forest
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
 Recommendations   Feature Importance   Metrics
         │
         ▼
     What-If Analysis
         │
         ▼
   Gemini HR Assistant
         │
         ▼
    HR Decision Support

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

Responsible for:

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

---

## 3.3 Machine Learning Layer

### Model

### Models Evaluated

1. Logistic Regression
2. Random Forest
3. XGBoost

### Model Comparison Results

| Model               | Accuracy (%) |
|---------------------|--------------|
| Logistic Regression | 86.05        |
| Random Forest       | 82.99        |
| XGBoost             | 87.41        |

### Final Selected Model

Optimized XGBoost Classifier

Responsibilities:

- Train model
- Predict attrition
- Calculate probability scores

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

Purpose:

Provide transparency for predictions.

Techniques:

- Feature Importance Analysis
- Risk Factor Identification

Outputs:

- Top Features
- Business Insights
- HR Interpretation

Files:

```text
src/shap_analysis.py
scripts/generate_feature_importance.py
```

---

## 3.5 Recommendation Engine

Purpose:

Generate personalized retention strategies.

Examples:

- Reduce overtime
- Improve work-life balance
- Salary review
- Promotion discussion

Implementation:

```python
generate_recommendations()
```

File:

```text
src/recommendations.py
```

---

## 3.6 What-If Analysis Engine

Purpose:

Simulate HR interventions and measure impact.

Examples:

Scenario 1:

```text
Increase Salary
```

Scenario 2:

```text
Remove Overtime
```

Scenario 3:

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

Purpose:

Provide AI-powered HR insights.

Technology:

Google Gemini AI

Capabilities:

- Explain predictions
- Generate summaries
- Suggest retention actions
- Answer HR questions

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
```text

Built using:

01_Home.py

02_Prediction.py

03_Explainability.py

04_Recommendations.py

05_What_If_Analysis.py

06_HR_Chatbot.py

07_Model_Evaluation.py


---

# 5. Data Flow Diagram

```text
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
      ▼
Risk Score
      │
      ├────────► Recommendation Engine
      │
      ├────────► What-If Analysis
      │
      ├────────► Feature Importance
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
│   ├── app.py
│   └── pages/
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

Sensitive information:

- Gemini API Key

Protection:

```text
.env file
```

Excluded using:

```text
.gitignore
```

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
      ├── Optimized XGBoost Model
      ├── Model Comparison Results
      ├── Feature Importance
      ├── Recommendation Engine
      ├── What-If Analysis
      └── Gemini AI
```

---

# 9. Future Architecture Enhancements

Future improvements may include:

- Real-Time HR Dashboard
- Employee Sentiment Analysis
- Deep Learning Models
- Cloud Deployment
- Multi-Company Support
- Automated Reporting
- Advanced Explainable AI
- SHAP-Based Explainability
- Ensemble Learning Models
- Real-Time Employee Monitoring

---

# 10. Conclusion

The proposed architecture integrates model comparison, optimized XGBoost prediction, explainable AI through feature importance analysis, recommendation generation, What-If Analysis, and Gemini-powered HR assistance into a unified Employee Attrition Intelligence System. The platform supports data-driven HR decision-making and achieved a final deployed model accuracy of 97.48%.