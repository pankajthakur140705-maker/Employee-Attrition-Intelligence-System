import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Intelligence System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Employee Attrition Intelligence System")

st.markdown("""
### AI-Powered Employee Retention Analytics Platform

This system combines Machine Learning, Explainable AI,
What-If Analysis, and Generative AI to predict employee
attrition risk and provide actionable HR decision support.
""")

st.markdown("---")

# Overview Metrics

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Dataset Size",
        "1470"
    )

with col2:
    st.metric(
        "Features",
        "45+"
    )

with col3:
    st.metric(
        "Models Compared",
        "3"
    )

with col4:
    st.metric(
        "Selected Model",
        "XGBoost"
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

st.header("🤖 Machine Learning Models")

st.table(
    {
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
    }
)

st.info("""
Final Selected Model:

XGBoost Classifier

Reason:
Highest predictive performance among all evaluated models.
""")

st.markdown("---")

st.header("📂 Dataset Information")

st.write("""
Dataset Used:

IBM HR Analytics Employee Attrition Dataset

Dataset Size:

• Total Employees: 1470

• Features: 45+

Target Variable:

• Attrition

Classes:

• Attrition = Yes
• Attrition = No
""")

st.markdown("---")

st.header("🏗️ System Architecture")

st.code("""
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
""")

st.markdown("---")

st.header("🔍 Top Attrition Risk Factors")

st.write("""
• OverTime

• Monthly Income

• Job Satisfaction

• Work Life Balance

• Years Since Last Promotion

• Environment Satisfaction
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
• Feature Importance
• Explainable AI
""")

st.markdown("---")

st.header("🎓 Project Outcome")

st.success("""
The Employee Attrition Intelligence System successfully
predicts employee attrition risk, explains key risk factors,
generates retention recommendations, performs What-If
analysis, and provides AI-powered HR assistance through
Google Gemini AI.
""")

st.markdown("---")

st.caption(
    "Developed by Pankaj Thakur | B.Tech CSE (AI & Data Science)"
)