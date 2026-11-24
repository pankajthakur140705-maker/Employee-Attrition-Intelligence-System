
import sys
from pathlib import Path

import streamlit as st
import pandas as pd

# Ensure project root is available for imports
PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.prediction import (
    get_feature_importance,
    get_model_status
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Feature Importance",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("📊 Feature Importance Dashboard")

st.markdown(
    """
    ### XGBoost Model Interpretability

    This dashboard presents the global feature importance
    extracted from the trained XGBoost model.

    It ranks employee attributes according to their relative
    importance within the model.
    """
)

st.divider()


# --------------------------------------------------
# MODEL STATUS
# --------------------------------------------------

st.header("🧠 Model Information")

try:
    model_status = get_model_status()

    if model_status.get("loaded", False):
        st.success("XGBoost model loaded successfully.")
    else:
        st.error("XGBoost model is not available.")

        if model_status.get("error"):
            st.error(str(model_status["error"]))

        st.stop()

except Exception as error:
    st.error(f"Unable to check model status: {error}")
    st.stop()


# --------------------------------------------------
# LOAD FEATURE IMPORTANCE
# --------------------------------------------------

try:
    importance_df = get_feature_importance()

    if importance_df is None or importance_df.empty:
        st.warning("Feature importance data is not available.")
        st.stop()

    required_columns = {"Feature", "Importance"}

    if not required_columns.issubset(importance_df.columns):
        st.error(
            "Feature importance data must contain "
            "'Feature' and 'Importance' columns."
        )
        st.stop()

    importance_df = importance_df[
        ["Feature", "Importance"]
    ].copy()

    importance_df["Importance"] = pd.to_numeric(
        importance_df["Importance"],
        errors="coerce"
    )

    importance_df = importance_df.dropna(
        subset=["Importance"]
    )

    importance_df = importance_df[
        importance_df["Importance"] >= 0
    ]

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    ).reset_index(drop=True)

    if importance_df.empty:
        st.warning("No valid feature importance values were found.")
        st.stop()

    total_importance = importance_df["Importance"].sum()

    if total_importance <= 0:
        st.warning(
            "The model returned zero feature importance values."
        )
        st.stop()

    # Convert importance values into relative percentages
    importance_df["Importance (%)"] = (
        importance_df["Importance"] / total_importance
    ) * 100

except Exception as error:
    st.error(
        f"Unable to load feature importance: {error}"
    )
    st.stop()


# --------------------------------------------------
# FEATURE IMPORTANCE OVERVIEW
# --------------------------------------------------

st.header("📈 Feature Importance Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Features",
        len(importance_df)
    )

with col2:
    top_feature = importance_df.iloc[0]["Feature"]

    st.metric(
        "Most Important Feature",
        str(top_feature)
    )

with col3:
    top_importance = importance_df.iloc[0]["Importance (%)"]

    st.metric(
        "Top Feature Importance",
        f"{top_importance:.2f}%"
    )


st.divider()


# --------------------------------------------------
# TOP 15 FEATURE IMPORTANCE CHART
# --------------------------------------------------

st.header("📊 Feature Importance Visualization")

st.subheader("Top 15 Important Features")

top_15 = importance_df.head(15).copy()

chart_data = top_15.set_index("Feature")[
    "Importance (%)"
]

st.bar_chart(
    chart_data,
    horizontal=True
)

st.caption(
    "The chart displays the 15 highest-ranked features "
    "based on the trained XGBoost model's feature importance."
)


st.divider()


# --------------------------------------------------
# FEATURE IMPORTANCE TABLE
# --------------------------------------------------

st.header("📋 Feature Importance Ranking")

display_df = importance_df.copy()

display_df.insert(
    0,
    "Rank",
    range(1, len(display_df) + 1)
)

display_df["Importance (%)"] = (
    display_df["Importance (%)"].round(2)
)

display_df = display_df[
    ["Rank", "Feature", "Importance (%)"]
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


# --------------------------------------------------
# INDIVIDUAL FEATURE EXPLORATION
# --------------------------------------------------

st.header("🔍 Explore Individual Features")

selected_feature = st.selectbox(
    "Select an employee attribute:",
    importance_df["Feature"].tolist()
)

selected_row = importance_df.loc[
    importance_df["Feature"] == selected_feature
].iloc[0]

selected_importance = selected_row["Importance (%)"]

st.metric(
    label=f"Importance of {selected_feature}",
    value=f"{selected_importance:.2f}%"
)


st.divider()


# --------------------------------------------------
# INTERPRETATION GUIDE
# --------------------------------------------------

st.header("📖 Interpretation Guide")

st.markdown(
    """
    **Higher Feature Importance**

    A higher score means that the feature has greater relative
    importance in the trained model compared with other features.

    **Lower Feature Importance**

    A lower score indicates that the feature has less relative
    importance in the model.

    **Zero Feature Importance**

    A zero score means that the model's reported importance
    for that feature is zero.

    **Important Limitation**

    Feature importance does not explain whether a feature
    increases or decreases attrition probability.

    It also does not establish a causal relationship between
    an employee attribute and attrition.
    """
)


st.divider()


# --------------------------------------------------
# FINAL NOTE
# --------------------------------------------------

st.success(
    """
    Feature Importance provides a global view of the employee
    attributes used by the XGBoost model. HR managers can use
    these insights to better understand model behaviour and
    support data-driven retention decisions.
    """
)

st.caption(
    "Source: Feature importance extracted from the deployed XGBoost model."
)
