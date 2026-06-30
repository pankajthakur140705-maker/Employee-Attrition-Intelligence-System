import streamlit as st
from src.recommendations import generate_recommendations

st.set_page_config(
    page_title="Retention Recommendation Engine",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Retention Recommendation Engine")

st.markdown("""
Generate personalized employee retention strategies based on key HR risk indicators.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=100000,
        value=10000
    )

    years_since_promotion = st.slider(
        "Years Since Last Promotion",
        0,
        15,
        2
    )

with col2:

    job_satisfaction = st.slider(
        "Job Satisfaction",
        1,
        4,
        3
    )

    environment_satisfaction = st.slider(
        "Environment Satisfaction",
        1,
        4,
        3
    )

if st.button("🚀 Generate Recommendations", use_container_width=True):

    employee = {
        "OverTime": overtime,
        "MonthlyIncome": monthly_income,
        "JobSatisfaction": job_satisfaction,
        "EnvironmentSatisfaction": environment_satisfaction,
        "YearsSinceLastPromotion": years_since_promotion
    }

    recommendations = generate_recommendations(employee)

    st.markdown("---")

    st.subheader("📋 Employee Risk Profile")

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.metric(
            "Monthly Income",
            f"₹{monthly_income:,}"
        )

    with col_b:
        st.metric(
            "Job Satisfaction",
            f"{job_satisfaction}/4"
        )

    with col_c:
        st.metric(
            "Promotion Gap",
            f"{years_since_promotion} Years"
        )

    st.markdown("---")

    st.subheader("💡 Recommended Retention Actions")

    if len(recommendations) == 0:

        st.success(
            """
            Employee appears stable.

            No immediate retention intervention required.
            """
        )

    else:

        for idx, rec in enumerate(
            recommendations,
            start=1
        ):
            st.success(
                f"{idx}. {rec}"
            )

    st.markdown("---")

    st.subheader("🧠 HR Action Summary")

    risk_count = 0

    if overtime == "Yes":
        risk_count += 1
        st.warning(
            "⚠️ Overtime is increasing attrition risk."
        )

    if monthly_income < 5000:
        risk_count += 1
        st.warning(
            "⚠️ Compensation review recommended."
        )

    if job_satisfaction <= 2:
        risk_count += 1
        st.warning(
            "⚠️ Employee engagement initiatives required."
        )

    if environment_satisfaction <= 2:
        risk_count += 1
        st.warning(
            "⚠️ Workplace environment improvement recommended."
        )

    if years_since_promotion >= 5:
        risk_count += 1
        st.warning(
            "⚠️ Career growth discussion recommended."
        )

    st.markdown("---")

    st.subheader("📊 Overall Retention Status")

    if risk_count >= 4:

        st.error(
            "🔴 High Retention Risk - Immediate HR intervention required."
        )

    elif risk_count >= 2:

        st.warning(
            "🟠 Moderate Retention Risk - Monitor employee closely."
        )

    else:

        st.success(
            "🟢 Low Retention Risk - Employee profile appears healthy."
        )

    st.markdown("---")

    st.subheader("🎯 Recommended HR Strategy")

    if risk_count >= 4:

        st.info(
            """
            Priority Actions:

            • Salary Review

            • Reduce Overtime

            • Promotion Discussion

            • Employee Engagement Program

            • Manager Feedback Session
            """
        )

    elif risk_count >= 2:

        st.info(
            """
            Suggested Actions:

            • Regular Check-ins

            • Recognition Programs

            • Career Development Discussions
            """
        )

    else:

        st.info(
            """
            Maintain Current Strategy:

            • Employee Recognition

            • Learning Opportunities

            • Positive Work Environment
            """
        )