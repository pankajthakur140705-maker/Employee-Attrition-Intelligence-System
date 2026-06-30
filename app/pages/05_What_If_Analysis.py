import streamlit as st
import pandas as pd
from src.preprocessing import create_employee_record
from src.prediction import predict_attrition

st.set_page_config(
    page_title="What-If Analysis",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 What-If Analysis")

st.markdown("""
Simulate HR interventions and evaluate their impact on employee attrition risk.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Current Scenario")

    age = st.slider("Age", 18, 60, 30)

    monthly_income = st.slider(
        "Monthly Income",
        1000,
        50000,
        10000,
        500
    )

    distance = st.slider(
        "Distance From Home",
        1,
        30,
        5
    )

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )

with col2:

    st.subheader("Employee Experience")

    job_satisfaction = st.slider(
        "Job Satisfaction",
        1,
        4,
        3
    )

    work_life_balance = st.slider(
        "Work Life Balance",
        1,
        4,
        3
    )

    years_since_promotion = st.slider(
        "Years Since Last Promotion",
        0,
        15,
        2
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Human Resources",
            "Laboratory Technician",
            "Manager",
            "Manufacturing Director",
            "Research Director",
            "Research Scientist",
            "Sales Executive",
            "Sales Representative"
        ]
    )

if st.button("🚀 Run What-If Analysis"):

    employee_data = {
        "Age": age,
        "MonthlyIncome": monthly_income,
        "DistanceFromHome": distance,
        "OverTime": overtime,
        "JobSatisfaction": job_satisfaction,
        "WorkLifeBalance": work_life_balance,
        "YearsSinceLastPromotion": years_since_promotion,
        "JobRole": job_role
    }

    input_df = create_employee_record(
        employee_data
    )

    result = predict_attrition(input_df)

    if len(result) == 4:
        prediction, probability, risk_score, risk_level = result
    else:
        prediction, probability = result
        risk_score = round(probability * 100, 2)

        if risk_score >= 70:
            risk_level = "High"
        elif risk_score >= 40:
            risk_level = "Medium"
        else:
            risk_level = "Low"

    st.markdown("---")

    st.subheader("📊 Risk Assessment")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Risk Score",
            f"{risk_score:.2f}%"
        )

    with c2:
        st.metric(
            "Risk Level",
            risk_level
        )

    with c3:
        st.metric(
            "Prediction",
            "Likely Leave" if prediction == 1 else "Likely Stay"
        )

    st.progress(
        min(int(risk_score), 100)
    )

    if risk_level == "High":
        st.error(
            "🔴 High Attrition Risk"
        )

    elif risk_level == "Medium":
        st.warning(
            "🟠 Medium Attrition Risk"
        )

    else:
        st.success(
            "🟢 Low Attrition Risk"
        )

    st.markdown("---")

    st.subheader("👤 Scenario Summary")

    st.dataframe(
        pd.DataFrame(
            employee_data.items(),
            columns=["Feature", "Value"]
        ),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("💡 Business Insights")

    insights = []

    if overtime == "Yes":
        insights.append(
            "Overtime is significantly increasing attrition risk."
        )

    if monthly_income < 5000:
        insights.append(
            "Compensation level is below recommended threshold."
        )

    if job_satisfaction <= 2:
        insights.append(
            "Employee satisfaction is critically low."
        )

    if work_life_balance <= 2:
        insights.append(
            "Work-life balance concerns detected."
        )

    if years_since_promotion >= 5:
        insights.append(
            "Promotion delay may impact retention."
        )

    if len(insights) == 0:

        st.success(
            "No major risk indicators detected."
        )

    else:

        for item in insights:
            st.warning(item)

    st.markdown("---")

    st.subheader("🎯 Recommended HR Actions")

    actions = []

    if overtime == "Yes":
        actions.append("Reduce overtime workload")

    if monthly_income < 5000:
        actions.append("Review compensation package")

    if job_satisfaction <= 2:
        actions.append("Conduct employee engagement session")

    if work_life_balance <= 2:
        actions.append("Improve work-life balance policies")

    if years_since_promotion >= 5:
        actions.append("Discuss promotion opportunities")

    if len(actions) == 0:

        st.success(
            "No immediate retention action required."
        )

    else:

        for action in actions:
            st.info(f"✅ {action}")

    st.markdown("---")

    st.subheader("🧠 Executive Summary")

    if risk_score >= 70:

        st.error("""
High attrition risk detected.

Immediate HR intervention is recommended.
Employee retention initiatives should focus on
compensation, engagement, career growth,
and workload management.
""")

    elif risk_score >= 40:

        st.warning("""
Moderate attrition risk detected.

Regular monitoring and proactive engagement
are recommended.
""")

    else:

        st.success("""
Low attrition risk detected.

Current employee conditions appear healthy.
Continue existing retention practices.
""")