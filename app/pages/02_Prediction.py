
# ==========================================
# EMPLOYEE ATTRITION PREDICTION PAGE
# ==========================================

import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


# ==========================================
# IMPORT LIBRARIES
# ==========================================

import streamlit as st
import pandas as pd

from src.preprocessing import create_employee_record

from src.prediction import (
    predict_attrition,
    get_top_factors,
    generate_hr_summary
)


# ==========================================
# GEMINI IMPORT
# ==========================================

try:
    from src.gemini_chatbot import (
        get_hr_analysis,
        get_gemini_status
    )

    GEMINI_AVAILABLE = get_gemini_status()["available"]

except ImportError:
    GEMINI_AVAILABLE = False


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="🎯",
    layout="wide"
)


# ==========================================
# PAGE HEADER
# ==========================================

st.title("🎯 Employee Attrition Prediction")

st.markdown("""
Predict employee attrition probability using the trained
**XGBoost Classification Model**.

The module provides employee risk categorization,
model-based feature importance and personalized
retention decision support.
""")

st.divider()


# ==========================================
# EMPLOYEE INFORMATION FORM
# ==========================================

st.header("👤 Employee Information")

st.caption(
    "Enter the employee details to estimate attrition risk."
)

with st.form("employee_prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Personal and Organizational Details")

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=65,
            value=30
        )

        monthly_income = st.number_input(
            "Monthly Income",
            min_value=1000,
            max_value=100000,
            value=10000,
            step=500
        )

        distance_from_home = st.number_input(
            "Distance From Home",
            min_value=1,
            max_value=50,
            value=5
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

        overtime = st.selectbox(
            "OverTime",
            ["No", "Yes"]
        )

    with col2:

        st.subheader("Employee Satisfaction Details")

        job_satisfaction = st.slider(
            "Job Satisfaction",
            min_value=1,
            max_value=4,
            value=3,
            help="1 = Low, 4 = Very High"
        )

        environment_satisfaction = st.slider(
            "Environment Satisfaction",
            min_value=1,
            max_value=4,
            value=3
        )

        work_life_balance = st.slider(
            "Work-Life Balance",
            min_value=1,
            max_value=4,
            value=3
        )

        years_since_promotion = st.slider(
            "Years Since Last Promotion",
            min_value=0,
            max_value=15,
            value=2
        )

    st.divider()

    submitted = st.form_submit_button(
        "🚀 Predict Attrition Risk",
        use_container_width=True
    )


# ==========================================
# PREDICTION PROCESS
# ==========================================

if submitted:

    employee_data = {

        "Age": age,

        "MonthlyIncome": monthly_income,

        "DistanceFromHome": distance_from_home,

        "OverTime": overtime,

        "JobRole": job_role,

        "JobSatisfaction": job_satisfaction,

        "WorkLifeBalance": work_life_balance,

        "YearsSinceLastPromotion": years_since_promotion,

        "EnvironmentSatisfaction": environment_satisfaction

    }

    try:

        with st.spinner(
            "Analyzing employee information..."
        ):

            # ----------------------------------
            # CREATE MODEL INPUT
            # ----------------------------------

            employee_df = create_employee_record(
                employee_data
            )

            # ----------------------------------
            # XGBOOST PREDICTION
            # ----------------------------------

            (
                prediction,
                probability,
                risk_score,
                risk_level
            ) = predict_attrition(
                employee_df
            )

            # ----------------------------------
            # GLOBAL FEATURE IMPORTANCE
            # ----------------------------------

            top_factors = get_top_factors(
                top_n=5
            )

            # ----------------------------------
            # RETENTION RECOMMENDATIONS
            # ----------------------------------

            recommendations = []

            if overtime == "Yes":

                recommendations.append(
                    "Reduce excessive overtime and "
                    "improve workload distribution."
                )

            if job_satisfaction <= 2:

                recommendations.append(
                    "Introduce employee engagement "
                    "and job satisfaction improvement programs."
                )

            if work_life_balance <= 2:

                recommendations.append(
                    "Consider flexible working arrangements "
                    "to improve work-life balance."
                )

            if years_since_promotion > 5:

                recommendations.append(
                    "Review career development and "
                    "promotion opportunities."
                )

            if environment_satisfaction <= 2:

                recommendations.append(
                    "Investigate workplace conditions "
                    "and improve employee satisfaction."
                )

            if not recommendations:

                recommendations.append(
                    "Continue regular employee monitoring, "
                    "recognition and career development."
                )

            # ----------------------------------
            # SAVE RESULTS IN SESSION STATE
            # ----------------------------------

            st.session_state["employee_data"] = employee_data

            st.session_state["employee_df"] = employee_df

            st.session_state["prediction"] = prediction

            st.session_state["probability"] = probability

            st.session_state["risk_score"] = risk_score

            st.session_state["risk_level"] = risk_level

            st.session_state["top_factors"] = top_factors

            st.session_state["recommendations"] = recommendations

    except Exception as e:

        st.error(
            "Unable to generate employee attrition prediction."
        )

        st.exception(e)


# ==========================================
# DISPLAY PREDICTION RESULTS
# ==========================================

if "risk_score" in st.session_state:

    prediction = st.session_state["prediction"]

    risk_score = st.session_state["risk_score"]

    risk_level = st.session_state["risk_level"]

    top_factors = st.session_state["top_factors"]

    recommendations = st.session_state["recommendations"]

    employee_data = st.session_state["employee_data"]

    st.divider()

    st.header("📊 Prediction Results")

    # --------------------------------------
    # MAIN METRICS
    # --------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Attrition Probability",
            f"{risk_score:.2f}%"
        )

    with col2:

        st.metric(
            "Risk Category",
            risk_level
        )

    with col3:

        st.metric(
            "Predicted Attrition",
            "Likely Leave" if prediction == 1 else "Likely Stay"
        )

    # --------------------------------------
    # PROBABILITY INDICATOR
    # --------------------------------------

    st.subheader("Employee Risk Assessment")

    st.progress(
        min(
            max(float(risk_score) / 100, 0.0),
            1.0
        )
    )

    if risk_level == "High":

        st.error(
            f"""
            🔴 HIGH ATTRITION RISK

            Estimated attrition probability: {risk_score:.2f}%

            Immediate HR review and targeted retention
            intervention are recommended.
            """
        )

    elif risk_level == "Medium":

        st.warning(
            f"""
            🟠 MEDIUM ATTRITION RISK

            Estimated attrition probability: {risk_score:.2f}%

            Targeted employee engagement and retention
            strategies are recommended.
            """
        )

    else:

        st.success(
            f"""
            🟢 LOW ATTRITION RISK

            Estimated attrition probability: {risk_score:.2f}%

            Continue regular employee monitoring
            and engagement activities.
            """
        )

    st.caption(
        "Risk categories: Low <30%, Medium 30% to <70%, "
        "High ≥70%, according to the project report."
    )

    st.divider()


    # ======================================
    # EMPLOYEE PROFILE SUMMARY
    # ======================================

    st.header("👤 Employee Profile Summary")

    summary_df = pd.DataFrame(
        employee_data.items(),
        columns=["Employee Attribute", "Value"]
    )

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()


    # ======================================
    # FEATURE IMPORTANCE
    # ======================================

    st.header("📈 XGBoost Feature Importance")

    st.markdown("""
    The following features are the most influential
    attributes in the trained XGBoost model.
    """)

    if top_factors:

        for index, factor in enumerate(
            top_factors,
            start=1
        ):

            st.write(
                f"**{index}.** {factor}"
            )

    else:

        st.info(
            "Feature importance information is unavailable."
        )

    st.caption(
        "These are global model-level feature rankings, "
        "not individual employee-specific explanations."
    )

    st.divider()


    # ======================================
    # RETENTION RECOMMENDATIONS
    # ======================================

    st.header("💡 Retention Recommendation Engine")

    st.markdown("""
    Suggested HR interventions based on employee attributes
    and the project's rule-based recommendation approach.
    """)

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        st.success(
            f"**Action {index}:** {recommendation}"
        )

    st.divider()


    # ======================================
    # HR DASHBOARD SUMMARY
    # ======================================

    st.header("📋 HR Risk Dashboard")

    d1, d2, d3 = st.columns(3)

    with d1:

        st.metric(
            "Attrition Probability",
            f"{risk_score:.2f}%"
        )

    with d2:

        st.metric(
            "Risk Category",
            risk_level
        )

    with d3:

        st.metric(
            "Recommended Actions",
            len(recommendations)
        )

    st.divider()


    # ======================================
    # GEMINI HR ANALYSIS
    # ======================================

    st.header("🤖 Gemini-Powered HR Analysis")

    if GEMINI_AVAILABLE:

        if st.button(
            "Generate AI HR Analysis",
            use_container_width=True
        ):

            try:

                with st.spinner(
                    "Gemini is analyzing the employee profile..."
                ):

                    analysis = get_hr_analysis(
                        employee_data=employee_data,
                        risk_score=risk_score,
                        top_factors=top_factors,
                        recommendations=recommendations
                    )

                    st.session_state["gemini_analysis"] = analysis

            except Exception as e:

                st.error(
                    f"Gemini Analysis Error: {e}"
                )

        if "gemini_analysis" in st.session_state:

            st.markdown("### AI-Generated HR Report")

            st.markdown(
                st.session_state["gemini_analysis"]
            )

    else:

        st.info(
            "Gemini is unavailable. Configure GEMINI_API_KEY "
            "in your local .env file or Streamlit Cloud Secrets."
        )

    st.divider()


    # ======================================
    # EXECUTIVE HR SUMMARY
    # ======================================

    st.header("🧠 Executive HR Summary")

    try:

        executive_summary = generate_hr_summary(
            risk_score,
            risk_level,
            top_factors
        )

        st.info(
            executive_summary
        )

    except Exception:

        st.info(
            f"Employee attrition probability is {risk_score:.2f}%. "
            f"The employee is classified as {risk_level} risk."
        )


    # ======================================
    # FINAL DISCLAIMER
    # ======================================

    st.divider()

    st.caption("""
    **Decision-support notice:** The predicted probability is a
    machine-learning estimate based on the trained IBM HR Analytics
    model. It is not a certainty that an employee will leave.
    HR decisions should include appropriate human review.
    """)


else:

    st.info(
        "👆 Enter employee information above and click "
        "'Predict Attrition Risk' to generate the prediction."
    )
