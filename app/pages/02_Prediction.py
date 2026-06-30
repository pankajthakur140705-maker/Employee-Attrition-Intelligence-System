import streamlit as st
import pandas as pd

from src.preprocessing import create_employee_record
from src.prediction import predict_attrition, get_top_factors

try:
    from src.gemini_chatbot import get_hr_analysis
    GEMINI_AVAILABLE = True
except:
    GEMINI_AVAILABLE = False

st.set_page_config(
    page_title="Employee Attrition Intelligence System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Employee Attrition Intelligence System")

st.markdown("""
Predict employee attrition risk using XGBoost,
Explainable AI (XAI), and Gemini HR Assistant.
""")

st.markdown("---")

st.header("👤 Employee Information")

col1, col2 = st.columns(2)

with col1:

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
        value=10000
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=50,
        value=5
    )

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )

with col2:

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

    environment_satisfaction = st.slider(
        "Environment Satisfaction",
        1,
        4,
        3
    )

if st.button(
    "🚀 Predict Attrition Risk",
    use_container_width=True
):

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

        employee_df = create_employee_record(
            employee_data
        )

        result = predict_attrition(
            employee_df
        )

        if len(result) == 4:

            prediction, probability, risk_score, risk_level = result

        else:

            prediction, probability = result

            risk_score = round(
                probability * 100,
                2
            )

            if risk_score >= 70:
                risk_level = "High"

            elif risk_score >= 40:
                risk_level = "Medium"

            else:
                risk_level = "Low"

        top_factors = get_top_factors(
            employee_df
        )

        st.session_state["risk_score"] = risk_score
        st.session_state["top_factors"] = top_factors

        st.markdown("---")

        st.subheader("📈 Prediction Result")

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
                "Likely Leave"
                if prediction == 1
                else "Likely Stay"
            )

        st.progress(
            min(
                int(risk_score),
                100
            )
        )

        if risk_level == "High":

            st.error(
                f"🔴 High Attrition Risk ({risk_score:.2f}%)"
            )

        elif risk_level == "Medium":

            st.warning(
                f"🟠 Medium Attrition Risk ({risk_score:.2f}%)"
            )

        else:

            st.success(
                f"🟢 Low Attrition Risk ({risk_score:.2f}%)"
            )

        st.markdown("---")

        st.subheader("👤 Employee Summary")

        summary_df = pd.DataFrame(
            employee_data.items(),
            columns=[
                "Feature",
                "Value"
            ]
        )

        st.dataframe(
            summary_df,
            use_container_width=True
        )

        st.markdown("---")

        st.subheader("🎯 Key Risk Factors")

        if len(top_factors) == 0:

            st.success(
                "No significant risk factors detected."
            )

        else:

            for factor in top_factors:

                st.warning(
                    f"⚠️ {factor}"
                )

        st.markdown("---")

        st.subheader(
            "💡 Retention Recommendations"
        )

        recommendations = []

        if overtime == "Yes":
            recommendations.append(
                "Reduce overtime workload."
            )

        if monthly_income < 5000:
            recommendations.append(
                "Review compensation package."
            )

        if job_satisfaction <= 2:
            recommendations.append(
                "Improve employee engagement."
            )

        if work_life_balance <= 2:
            recommendations.append(
                "Improve work-life balance."
            )

        if years_since_promotion >= 5:
            recommendations.append(
                "Discuss promotion opportunities."
            )

        st.session_state[
            "recommendations"
        ] = recommendations

        if len(recommendations) == 0:

            st.success(
                "No major retention issues detected."
            )

        else:

            for item in recommendations:

                st.success(
                    f"✅ {item}"
                )

        st.markdown("---")

        st.subheader("📊 HR Risk Dashboard")

        d1, d2, d3 = st.columns(3)

        with d1:
            st.metric(
                "Risk Score",
                f"{risk_score:.2f}%"
            )

        with d2:
            st.metric(
                "Risk Level",
                risk_level
            )

        with d3:
            st.metric(
                "Risk Factors",
                len(top_factors)
            )

        if GEMINI_AVAILABLE:

            st.markdown("---")

            st.subheader(
                "🤖 Gemini HR Analysis"
            )

            try:

                analysis = get_hr_analysis(
                    employee_data,
                    risk_score,
                    top_factors,
                    recommendations
                )

                st.write(
                    analysis
                )

            except Exception as e:

                st.warning(
                    f"Gemini Error: {e}"
                )

        st.markdown("---")

        st.subheader(
            "🧠 Executive HR Summary"
        )

        if risk_score >= 70:

            st.error(
                """
High Attrition Risk Detected

Recommended Actions:

• Reduce overtime

• Review compensation

• Improve engagement

• Discuss promotion opportunities
                """
            )

        elif risk_score >= 40:

            st.warning(
                """
Medium Attrition Risk Detected

Recommended Actions:

• Conduct feedback sessions

• Improve recognition programs

• Monitor employee sentiment
                """
            )

        else:

            st.success(
                """
Low Attrition Risk Detected

Employee appears stable.

Continue career development,
recognition, and engagement programs.
                """
            )

        st.markdown("---")

        st.subheader(
            "📋 AI Generated HR Action Plan"
        )

        if len(top_factors) == 0:

            st.success(
                "No immediate HR action required."
            )

        else:

            for idx, factor in enumerate(
                top_factors,
                start=1
            ):

                st.write(
                    f"{idx}. Investigate and address: {factor}"
                )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )