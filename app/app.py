import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Intelligence System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Employee Attrition Intelligence System")

st.markdown("""
# Welcome

An AI-Powered HR Analytics Platform for:

✅ Employee Attrition Prediction

✅ SHAP Explainability

✅ Retention Recommendation Engine

✅ What-If Analysis

✅ Gemini HR Assistant

---

### Navigation

Use the left sidebar to access:

- Home
- Prediction
- SHAP Explainability
- Recommendations
- What-If Analysis
- HR Chatbot

---

### Technology Stack

- XGBoost Classifier
- SHAP Explainability
- Streamlit Dashboard
- Google Gemini AI
- IBM HR Analytics Dataset
- Python Machine Learning

---

### Objective

Predict employee attrition, explain model decisions,
recommend retention actions, and assist HR teams with AI-powered insights.
""")

st.success(
    "✅ System Loaded Successfully. Select a module from the sidebar."
)