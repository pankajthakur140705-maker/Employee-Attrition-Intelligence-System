
import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Employee Attrition Intelligence System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# APPLICATION HEADER
# ==========================================

st.title("📊 Employee Attrition Intelligence System")

st.subheader(
    "An AI-Powered Framework for Employee Retention Prediction"
)

st.markdown("""
Predict employee attrition, understand the factors influencing
employee turnover, and support HR decision-making through
Machine Learning, Feature Importance, and Generative AI.
""")

st.divider()


# ==========================================
# PROJECT OVERVIEW
# ==========================================

st.header("🏢 Project Overview")

st.markdown("""
The **Employee Attrition Intelligence System** is an integrated
HR analytics and decision-support platform developed using
Machine Learning and Artificial Intelligence.

The system helps HR professionals:

- Predict employee attrition probability.
- Identify important factors influencing employee turnover.
- Generate personalized employee retention recommendations.
- Simulate retention interventions using What-If Analysis.
- Interact with a Gemini-powered HR Assistant.
""")

st.divider()


# ==========================================
# PROJECT STATISTICS
# ==========================================

st.header("📈 Project at a Glance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Employee Records",
        value="1,470",
        help="IBM HR Analytics Employee Attrition Dataset"
    )

with col2:
    st.metric(
        label="Train-Test Split",
        value="80 : 20",
        help="Stratified train-test partition"
    )

with col3:
    st.metric(
        label="ML Models Evaluated",
        value="3",
        help="Logistic Regression, Random Forest and XGBoost"
    )

with col4:
    st.metric(
        label="Final Model",
        value="XGBoost",
        help="Selected model for deployment"
    )

st.divider()


# ==========================================
# CORE SYSTEM MODULES
# ==========================================

st.header("⚙️ System Modules")

st.markdown(
    "The dashboard integrates five major decision-support modules."
)

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.subheader("🎯 1. Attrition Prediction")

        st.write("""
        Predict employee attrition status and estimate
        the probability of an employee leaving the organization
        using the trained XGBoost classifier.
        """)

    with st.container(border=True):

        st.subheader("📊 2. Feature Importance")

        st.write("""
        Analyze the influential employee attributes identified
        by the XGBoost model, including overtime, monthly income,
        job satisfaction, work-life balance and promotion history.
        """)

    with st.container(border=True):

        st.subheader("💡 3. Retention Recommendation Engine")

        st.write("""
        Generate personalized, rule-based retention strategies
        based on employee characteristics and identified
        attrition risk factors.
        """)

with col2:

    with st.container(border=True):

        st.subheader("🔄 4. What-If Analysis")

        st.write("""
        Simulate potential interventions by modifying salary,
        overtime, job satisfaction and work-life balance.
        Compare the resulting attrition probabilities.
        """)

    with st.container(border=True):

        st.subheader("🤖 5. Gemini HR Assistant")

        st.write("""
        Interact with Google Gemini to obtain natural-language
        explanations, employee risk summaries, HR insights
        and retention strategy suggestions.
        """)

st.divider()


# ==========================================
# MACHINE LEARNING METHODOLOGY
# ==========================================

st.header("🧠 Machine Learning Methodology")

st.markdown("""
The project evaluates three supervised machine learning
classification algorithms using the IBM HR Analytics dataset.
""")

models = {
    "Logistic Regression": "Baseline classification model",
    "Random Forest": "Ensemble learning using decision trees",
    "XGBoost": "Gradient boosting classifier selected for deployment"
}

for model, description in models.items():

    st.markdown(f"**{model}** — {description}")

st.info(
    "XGBoost was selected as the final deployment model "
    "after comparative evaluation."
)

st.divider()


# ==========================================
# DOCUMENTED MODEL PERFORMANCE
# ==========================================

st.header("📉 Model Evaluation Results")

st.caption(
    "Reported experimental results from the internship project."
)

import pandas as pd

performance_data = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],

    "Accuracy": [
        "86.05%",
        "82.99%",
        "87.41%"
    ],

    "Precision": [
        "61.54%",
        "36.36%",
        "77.78%"
    ],

    "Recall": [
        "34.04%",
        "8.51%",
        "29.79%"
    ],

    "F1-Score": [
        "43.84%",
        "13.79%",
        "43.08%"
    ]

})

st.dataframe(
    performance_data,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Evaluation metrics are the documented experimental results "
    "and are not live measurements from individual predictions."
)

st.divider()


# ==========================================
# EMPLOYEE RISK CATEGORIZATION
# ==========================================

st.header("🚦 Employee Risk Categorization")

st.markdown("""
The system categorizes employees according to their predicted
attrition probability.
""")

risk_col1, risk_col2, risk_col3 = st.columns(3)

with risk_col1:

    st.success("🟢 LOW RISK")

    st.subheader("Below 30%")

    st.write("Regular monitoring and employee engagement.")

with risk_col2:

    st.warning("🟠 MEDIUM RISK")

    st.subheader("30% to below 70%")

    st.write("Targeted retention strategies and intervention.")

with risk_col3:

    st.error("🔴 HIGH RISK")

    st.subheader("70% or above")

    st.write("Immediate HR intervention and detailed analysis.")

st.divider()


# ==========================================
# TECHNOLOGY STACK
# ==========================================

st.header("💻 Technology Stack")

tech_col1, tech_col2 = st.columns(2)

with tech_col1:

    st.markdown("""
    **Programming and Data Processing**

    - Python
    - Pandas
    - NumPy
    - Scikit-learn

    **Machine Learning**

    - Logistic Regression
    - Random Forest
    - XGBoost
    """)

with tech_col2:

    st.markdown("""
    **Artificial Intelligence**

    - XGBoost Feature Importance
    - Google Gemini AI

    **Application Development**

    - Streamlit Dashboard
    - Matplotlib

    **Dataset**

    - IBM HR Analytics Employee Attrition Dataset
    """)

st.divider()


# ==========================================
# PROJECT OBJECTIVE
# ==========================================

st.header("🎯 Project Objective")

st.markdown("""
The primary objective is to develop an integrated employee
attrition intelligence framework that transforms machine
learning predictions into interpretable insights and
actionable HR retention strategies.

The system aims to support proactive workforce management,
improve employee retention planning, and assist HR
professionals in making data-driven decisions.
""")

st.divider()


# ==========================================
# NAVIGATION GUIDANCE
# ==========================================

st.header("🧭 Dashboard Navigation")

st.markdown("""
Use the **left sidebar** to navigate between the available
application pages:

1. Home
2. Prediction
3. Feature Importance
4. Recommendations
5. What-If Analysis
6. HR Chatbot
7. Model Evaluation
""")

st.success(
    "✅ Employee Attrition Intelligence System Loaded Successfully. "
    "Select a module from the sidebar to begin."
)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Employee Attrition Intelligence System | "
    "Developed by Pankaj Thakur | "
    "B.Tech CSE (AI & Data Science)"
)
