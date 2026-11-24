
import sys
from pathlib import Path

import streamlit as st

# Ensure project root is available for imports
PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.recommendations import generate_recommendations


st.set_page_config(
    page_title="Retention Recommendation Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Retention Recommendation Engine")

st.markdown(
    """
    Generate rule-based employee retention recommendations using
    important HR indicators from the Employee Attrition Intelligence System.
    """
)

st.divider()

st.subheader("👤 Employee Information")

col1, col2 = st.columns(2)

with col1:
    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"],
        help="Whether the employee regularly works overtime."
    )

    monthly_income = st.number_input(
        "Monthly Income (₹)",
        min_value=0,
        max_value=1000000,
        value=10000,
        step=500
    )

    job_satisfaction = st.slider(
        "Job Satisfaction",
        min_value=1,
        max_value=4,
        value=3
    )

with col2:
    work_life_balance = st.slider(
        "Work-Life Balance",
        min_value=1,
        max_value=4,
        value=3
    )

    years_since_promotion = st.slider(
        "Years Since Last Promotion",
        min_value=0,
        max_value=40,
        value=2
    )

st.divider()

st.subheader("🏢 Organizational Salary Information")

organizational_average_income = st.number_input(
    "Organizational Average Monthly Income (₹)",
    min_value=0,
    max_value=1000000,
    value=0,
    step=500,
    help=(
        "Enter the actual organizational average monthly income. "
        "Leave as 0 if this information is unavailable."
    )
)

st.caption(
    "Salary-based recommendations are generated only when a valid "
    "organizational average is provided."
)

if st.button(
    "🚀 Generate Recommendations",
    use_container_width=True,
    type="primary"
):

    employee = {
        "OverTime": overtime,
        "MonthlyIncome": monthly_income,
        "JobSatisfaction": job_satisfaction,
        "WorkLifeBalance": work_life_balance,
        "YearsSinceLastPromotion": years_since_promotion
    }

    average_income = (
        organizational_average_income
        if organizational_average_income > 0
        else None
    )

    recommendations = generate_recommendations(
        employee,
        organizational_average_income=average_income
    )

    st.session_state["retention_recommendations"] = recommendations
    st.session_state["retention_employee"] = employee
    st.session_state["retention_average_income"] = average_income


# Display results after generation
if "retention_recommendations" in st.session_state:

    employee = st.session_state["retention_employee"]
    recommendations = st.session_state["retention_recommendations"]
    average_income = st.session_state["retention_average_income"]

    st.divider()

    st.subheader("📋 Employee Profile")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Monthly Income",
            f"₹{employee['MonthlyIncome']:,}"
        )

    with col2:
        st.metric(
            "Job Satisfaction",
            f"{employee['JobSatisfaction']}/4"
        )

    with col3:
        st.metric(
            "Work-Life Balance",
            f"{employee['WorkLifeBalance']}/4"
        )

    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            "OverTime",
            employee["OverTime"]
        )

    with col5:
        st.metric(
            "Years Since Promotion",
            employee["YearsSinceLastPromotion"]
        )

    if average_income is not None:
        st.caption(
            f"Organizational average monthly income: ₹{average_income:,}"
        )

    st.divider()

    st.subheader("💡 Recommended Retention Actions")

    if (
        len(recommendations) == 1
        and recommendations[0].startswith(
            "No retention concerns were identified"
        )
    ):
        st.success(recommendations[0])

    else:
        for index, recommendation in enumerate(
            recommendations,
            start=1
        ):
            st.info(
                f"**{index}.** {recommendation}"
            )

    st.divider()

    st.subheader("🧠 HR Summary")

    if len(recommendations) > 1 or not recommendations[0].startswith(
        "No retention concerns were identified"
    ):
        st.warning(
            f"{len(recommendations)} retention recommendation(s) "
            "were generated based on the employee's profile."
        )
    else:
        st.success(
            "No concerns were identified by the configured "
            "recommendation rules."
        )

    st.caption(
        """
        Note: These recommendations are generated using predefined,
        rule-based HR conditions. They are not an independent machine
        learning prediction or a quantified attrition-risk score.
        """
    )

    st.divider()

    if st.button("🔄 Reset Recommendations"):
        st.session_state.pop("retention_recommendations", None)
        st.session_state.pop("retention_employee", None)
        st.session_state.pop("retention_average_income", None)
        st.rerun()
