
import sys
from pathlib import Path

import streamlit as st
import pandas as pd

# --------------------------------------------------
# PROJECT IMPORTS
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.prediction import get_feature_importance


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Model Evaluation",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("📊 Model Evaluation Dashboard")

st.markdown(
    """
    ### Employee Attrition Model Performance

    This dashboard presents the comparative evaluation of
    Logistic Regression, Random Forest, and XGBoost models
    trained using the IBM HR Analytics Employee Attrition Dataset.
    """
)

st.divider()


# --------------------------------------------------
# DOCUMENTED MODEL RESULTS
# --------------------------------------------------

evaluation_data = {
    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy (%)": [
        86.05,
        82.99,
        87.41
    ],
    "Precision (%)": [
        61.54,
        36.36,
        77.78
    ],
    "Recall (%)": [
        34.04,
        8.51,
        29.79
    ],
    "F1 Score (%)": [
        43.84,
        13.79,
        43.08
    ]
}

evaluation_df = pd.DataFrame(evaluation_data)


# --------------------------------------------------
# FINAL MODEL PERFORMANCE
# --------------------------------------------------

st.header("🏆 Final Model: XGBoost")

xgboost = evaluation_df[
    evaluation_df["Model"] == "XGBoost"
].iloc[0]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        f"{xgboost['Accuracy (%)']:.2f}%"
    )

with col2:
    st.metric(
        "Precision",
        f"{xgboost['Precision (%)']:.2f}%"
    )

with col3:
    st.metric(
        "Recall",
        f"{xgboost['Recall (%)']:.2f}%"
    )

with col4:
    st.metric(
        "F1 Score",
        f"{xgboost['F1 Score (%)']:.2f}%"
    )

st.caption(
    "These are the documented experimental results from the internship report."
)

st.divider()


# --------------------------------------------------
# MODEL COMPARISON
# --------------------------------------------------

st.header("📈 Model Performance Comparison")

st.dataframe(
    evaluation_df,
    use_container_width=True,
    hide_index=True
)

st.subheader("Accuracy Comparison")

accuracy_chart = evaluation_df.set_index("Model")[
    "Accuracy (%)"
]

st.bar_chart(
    accuracy_chart,
    horizontal=True
)

st.subheader("Precision, Recall and F1 Comparison")

comparison_chart = evaluation_df.set_index("Model")[
    ["Precision (%)", "Recall (%)", "F1 Score (%)"]
]

st.bar_chart(
    comparison_chart
)

st.divider()


# --------------------------------------------------
# MODEL EVALUATION INTERPRETATION
# --------------------------------------------------

st.header("🧠 Evaluation Insights")

st.markdown(
    """
    **Logistic Regression**

    Achieved 86.05% accuracy and 43.84% F1 score.
    It provides a baseline for comparison with the other models.

    **Random Forest**

    Achieved 82.99% accuracy and 13.79% F1 score.
    Its documented recall was 8.51%.

    **XGBoost**

    Achieved the highest documented accuracy of 87.41%
    and precision of 77.78% among the three evaluated models.
    It was selected as the final deployment model.
    """
)

st.warning(
    """
    The XGBoost model's documented recall is 29.79%.
    Accuracy alone does not indicate how effectively the model
    identifies employees who will leave. HR users should consider
    precision, recall and F1 score when interpreting its performance.
    """
)

st.divider()


# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------

st.header("📊 XGBoost Feature Importance")

st.markdown(
    """
    Feature importance provides a global view of the employee
    attributes considered influential by the trained XGBoost model.
    """
)

try:

    importance_df = get_feature_importance()

    if (
        importance_df is not None
        and not importance_df.empty
        and {"Feature", "Importance"}.issubset(
            importance_df.columns
        )
    ):

        importance_df = importance_df.copy()

        importance_df = importance_df.sort_values(
            by="Importance",
            ascending=False
        )

        top_features = importance_df.head(15).set_index(
            "Feature"
        )["Importance"]

        st.bar_chart(
            top_features,
            horizontal=True
        )

        st.caption(
            "Feature importance extracted from the trained XGBoost model."
        )

    else:

        st.info(
            "Feature importance data is not currently available."
        )

except Exception as error:

    st.warning(
        f"Unable to load feature importance: {error}"
    )


st.divider()


# --------------------------------------------------
# DATASET AND METHODOLOGY
# --------------------------------------------------

st.header("📚 Dataset and Evaluation Methodology")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Dataset Information")

    st.markdown(
        """
        - **Dataset:** IBM HR Analytics Employee Attrition Dataset
        - **Total Records:** 1,470
        - **Target Variable:** Attrition
        - **Yes:** 1
        - **No:** 0
        """
    )

with col2:

    st.subheader("Training Methodology")

    st.markdown(
        """
        - **Training/Test Split:** 80:20
        - **Stratification:** Applied
        - **Random State:** 42
        - **Models Evaluated:** Three
        - **Final Model:** XGBoost
        """
    )

st.divider()


# --------------------------------------------------
# EVALUATION METRICS EXPLANATION
# --------------------------------------------------

st.header("📖 Understanding Evaluation Metrics")

with st.expander("Accuracy"):
    st.write(
        "The proportion of all predictions that the model classified correctly."
    )

with st.expander("Precision"):
    st.write(
        "Among employees predicted to leave, the proportion who actually left."
    )

with st.expander("Recall"):
    st.write(
        "Among employees who actually left, the proportion correctly identified by the model."
    )

with st.expander("F1 Score"):
    st.write(
        "The harmonic mean of precision and recall, balancing both metrics."
    )


# --------------------------------------------------
# FINAL SUMMARY
# --------------------------------------------------

st.divider()

st.success(
    """
    XGBoost was selected as the final deployment model after
    comparing Logistic Regression, Random Forest, and XGBoost.

    It achieved 87.41% accuracy and 77.78% precision in the
    documented experimental evaluation.
    """
)

st.caption(
    "Source: Internship project report — Employee Attrition Intelligence System Using Machine Learning."
)
