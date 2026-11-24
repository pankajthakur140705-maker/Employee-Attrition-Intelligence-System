import streamlit as st
import pandas as pd
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Feature Importance",
    page_icon="📊",
    layout="wide"
)

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

IMAGE_PATH = PROJECT_ROOT / "outputs/evaluation/feature_importance.png"
CSV_PATH = PROJECT_ROOT / "outputs/evaluation/feature_importance.csv"

# Page title
st.title("📊 Feature Importance Dashboard")

st.markdown("""
### Explainable Machine Learning

Feature Importance helps us understand which employee attributes
have the greatest influence on the XGBoost model's predictions.

It ranks different employee characteristics according to their
contribution to the model's decision-making process.
""")

st.markdown("---")

# Feature importance overview
st.header("🧠 Understanding Feature Importance")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Features influencing attrition prediction**

    - Total Working Years
    - Stock Option Level
    - Overtime
    - Job Role
    - Years in Current Role
    - Age
    - Environment Satisfaction
    - Job Satisfaction
    """)

with col2:
    st.success("""
    **Why Feature Importance is useful**

    - Identifies influential employee attributes.
    - Helps HR understand model behaviour.
    - Supports data-driven HR decisions.
    - Highlights important retention factors.
    - Improves model interpretability.
    """)

st.markdown("---")

# Feature Importance visualization
st.header("📊 Feature Importance Visualization")

if IMAGE_PATH.exists():

    st.subheader("Top 15 Important Features")

    st.image(
        str(IMAGE_PATH),
        use_container_width=True
    )

    st.caption(
        "Features are ranked according to their importance "
        "in the trained XGBoost model."
    )

else:

    st.warning(
        "Feature importance image not found. "
        "Please run the feature importance generation script."
    )

st.markdown("---")

# Feature importance data
st.header("📋 Feature Importance Ranking")

if CSV_PATH.exists():

    importance_df = pd.read_csv(CSV_PATH)

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    # Display top 10 features
    st.subheader("Top 10 Influential Features")

    top_features = importance_df.head(10).copy()

    top_features["Importance"] = (
        top_features["Importance"] * 100
    ).round(2)

    top_features = top_features.rename(
        columns={
            "Feature": "Employee Attribute",
            "Importance": "Importance (%)"
        }
    )

    st.dataframe(
        top_features,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # Feature selection
    st.subheader("Explore Individual Features")

    selected_feature = st.selectbox(
        "Select an employee attribute:",
        importance_df["Feature"].tolist()
    )

    selected_value = importance_df.loc[
        importance_df["Feature"] == selected_feature,
        "Importance"
    ].iloc[0]

    st.metric(
        label=f"Importance of {selected_feature}",
        value=f"{selected_value * 100:.2f}%"
    )

else:

    st.warning(
        "Feature importance CSV not found."
    )

st.markdown("---")

# Interpretation guide
st.header("📖 Interpretation Guide")

st.markdown("""
### How to interpret Feature Importance?

**Higher Importance Score**

A feature with a higher score has a greater influence
on the model's predictions compared with other features.

**Lower Importance Score**

A feature with a lower score contributes less to the
model's overall prediction process.

**Zero Importance**

The model did not use that feature to make its
tree-based predictions.

**Important Note:**

Feature Importance indicates the relative influence of
features. It does not tell us whether a feature increases
or decreases employee attrition risk.
""")

st.markdown("---")

st.success("""
✅ Feature Importance Analysis helps HR managers identify
the employee attributes that the XGBoost model considers
most influential when predicting employee attrition.
""")