import streamlit as st
import os

st.set_page_config(
    page_title="SHAP Explainability",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 SHAP Explainability Dashboard")

st.markdown("""
### Explainable Artificial Intelligence (XAI)

SHAP (SHapley Additive Explanations) helps understand why the XGBoost model predicts employee attrition risk.

It provides transparent explanations for each prediction and identifies the most influential employee attributes.
""")

st.markdown("---")

st.header("🧠 What SHAP Explains")

col1, col2 = st.columns(2)

with col1:

    st.info("""
    📈 Features Increasing Attrition Risk

    • Overtime

    • Low Monthly Income

    • Poor Work-Life Balance

    • Low Job Satisfaction

    • Long Time Since Promotion
    """)

with col2:

    st.success("""
    📉 Features Reducing Attrition Risk

    • High Job Satisfaction

    • Good Work-Life Balance

    • Higher Compensation

    • Positive Work Environment

    • Career Growth Opportunities
    """)

st.markdown("---")

st.header("📊 SHAP Visualizations")

st.markdown("""
The following visualizations were generated during model training and explain the model's behavior.
""")

# SHAP Summary Plot
if os.path.exists("outputs/shap/shap_summary.png"):

    st.subheader("1️⃣ SHAP Summary Plot")

    st.image(
        "outputs/shap/shap_summary.png",
        use_container_width=True
    )

    st.caption(
        "Shows overall feature importance across all employees."
    )

else:

    st.warning(
        "shap_summary.png not found in outputs/shap/"
    )

# SHAP Bar Plot
if os.path.exists("outputs/shap/shap_bar.png"):

    st.subheader("2️⃣ SHAP Feature Importance")

    st.image(
        "outputs/shap/shap_bar.png",
        use_container_width=True
    )

    st.caption(
        "Ranks features according to their impact on attrition prediction."
    )

else:

    st.warning(
        "shap_bar.png not found in outputs/shap/"
    )

# SHAP Waterfall Plot
if os.path.exists("outputs/shap/shap_waterfall.png"):

    st.subheader("3️⃣ SHAP Waterfall Plot")

    st.image(
        "outputs/shap/shap_waterfall.png",
        use_container_width=True
    )

    st.caption(
        "Explains an individual employee prediction."
    )

else:

    st.warning(
        "shap_waterfall.png not found in outputs/shap/"
    )

# SHAP Dependence Plot
if os.path.exists("outputs/shap/shap_dependence.png"):

    st.subheader("4️⃣ SHAP Dependence Plot")

    st.image(
        "outputs/shap/shap_dependence.png",
        use_container_width=True
    )

    st.caption(
        "Shows how a feature influences attrition risk."
    )

else:

    st.warning(
        "shap_dependence.png not found in outputs/shap/"
    )

st.markdown("---")

st.header("📋 Interpretation Guide")

st.markdown("""
### Red Values
Higher feature values that increase attrition risk.

### Blue Values
Lower feature values that reduce attrition risk.

### Positive SHAP Value
Feature pushes prediction toward employee attrition.

### Negative SHAP Value
Feature pushes prediction toward employee retention.
""")

st.markdown("---")

st.success("""
✅ SHAP Explainability enables transparent and trustworthy HR decision-making by explaining why employees are classified as high or low attrition risk.
""")