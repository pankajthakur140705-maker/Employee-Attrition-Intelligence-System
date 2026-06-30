import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Intelligence System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Employee Attrition Intelligence System")

st.markdown("""
### AI-Powered Employee Retention Analytics Platform

This system combines Machine Learning, Explainable AI, What-If Analysis,
and Generative AI to predict employee attrition risk and provide actionable
HR decision support.
""")

st.markdown("---")

# Project Metrics

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        "97.48%"
    )

with col2:
    st.metric(
        "Precision",
        "98.08%"
    )

with col3:
    st.metric(
        "Recall",
        "86.08%"
    )

with col4:
    st.metric(
        "F1 Score",
        "91.69%"
    )

st.markdown("---")

st.header("🚀 Project Features")

col1, col2 = st.columns(2)

with col1:

    st.success(
        "📈 Employee Attrition Prediction"
    )

    st.success(
        "🔍 Explainable AI (Feature Importance)"
    )

    st.success(
        "🎯 Retention Recommendation Engine"
    )

with col2:

    st.success(
        "🔄 What-If Analysis"
    )

    st.success(
        "🤖 Gemini HR Assistant"
    )

    st.success(
        "📊 Model Evaluation Dashboard"
    )

st.markdown("---")

st.header("🧠 Machine Learning Pipeline")

st.info("""
Models Evaluated:

• Logistic Regression
• Random Forest
• XGBoost

Model Comparison Results:

• Logistic Regression Accuracy: 86.05%
• Random Forest Accuracy: 82.99%
• XGBoost Accuracy: 87.41%

Final Selected Model:

• Optimized XGBoost Classifier

Optimization Technique:

• Bayesian Optimization

Explainability:

• Feature Importance Analysis

Prediction Type:

• Binary Classification

Target Variable:

• Employee Attrition
""")

st.markdown("---")

st.header("📂 Dataset Information")

st.write("""
Dataset:

IBM HR Analytics Employee Attrition Dataset

Total Employees:

1470

Target Classes:

• Attrition = Yes
• Attrition = No

Features Used:

45+

Important Features:

• OverTime
• Monthly Income
• Job Satisfaction
• Work Life Balance
• Years Since Last Promotion
• Environment Satisfaction
""")

st.markdown("---")

st.header("🏗️ System Architecture")

st.code("""
IBM HR Analytics Dataset
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
       (XGBoost Chosen)
              ↓
       Risk Prediction
              ↓
 Feature Importance Analysis
              ↓
 Recommendation Engine
              ↓
     What-If Analysis
              ↓
     Gemini HR Assistant
              ↓
      HR Decision Support
""")

st.markdown("---")

st.header("🛠️ Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.write("""
• Python
• Pandas
• NumPy
• Scikit-Learn
""")

with tech2:
    st.write("""
• XGBoost
• Streamlit
• Plotly
• Matplotlib
""")

with tech3:
    st.write("""
• Gemini AI
• Joblib
• Explainable AI
• Feature Importance
""")

st.markdown("---")

st.header("📊 Model Performance Summary")

st.table({
    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy (%)": [
        86.05,
        82.99,
        87.41
    ]
})

st.markdown("---")

st.header("🎓 Project Outcome")

st.success("""
The system compares multiple machine learning models and selects the
best-performing XGBoost model for deployment.

It predicts employee attrition risk, provides explainable insights through
feature importance analysis, generates personalized retention recommendations,
supports What-If scenario simulation, and offers AI-powered HR assistance
using Gemini.

The deployed optimized XGBoost model achieved:

• Accuracy: 97.48%
• Precision: 98.08%
• Recall: 86.08%
• F1 Score: 91.69%
""")

st.markdown("---")

st.caption(
    "Developed by Pankaj Thakur | B.Tech CSE (AI & Data Science)"
)