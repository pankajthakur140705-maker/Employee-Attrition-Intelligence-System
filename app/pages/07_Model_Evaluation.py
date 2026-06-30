import streamlit as st

st.title("📊 Model Evaluation Dashboard")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy", "97.48%")
    st.metric("Precision", "98.08%")

with col2:
    st.metric("Recall", "86.08%")
    st.metric("F1 Score", "91.69%")

st.markdown("---")

st.subheader("Confusion Matrix")

st.code("""
[[1229    4]
 [  33  204]]
""")

st.markdown("---")

import os

st.subheader("📈 Feature Importance")

image_path = "outputs/evaluation/feature_importance.png"

if os.path.exists(image_path):

    st.image(
        image_path,
        caption="Top Feature Importance from XGBoost Model",
        use_container_width=True
    )

else:

    st.error(
        f"Feature Importance image not found:\n{image_path}"
    )

st.markdown("---")

st.subheader("Model Summary")

st.success("""
Model: XGBoost Classifier

Dataset: IBM HR Analytics Employee Attrition Dataset

Accuracy: 97.48%

Precision: 98.08%

Recall: 86.08%

F1 Score: 91.69%

The model demonstrates strong predictive performance and can effectively identify employees at risk of attrition.
""")