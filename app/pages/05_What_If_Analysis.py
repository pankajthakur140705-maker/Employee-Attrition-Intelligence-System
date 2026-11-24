
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

from src.preprocessing import create_employee_record
from src.prediction import predict_attrition


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="What-If Analysis",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 What-If Analysis")

st.markdown(
    """
    Simulate HR retention interventions and evaluate their
    impact on employee attrition probability.

    Compare the current employee profile with different
    intervention scenarios to understand potential changes
    in predicted attrition risk.
    """
)

st.divider()


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def get_attrition_probability(employee_data):
    """
    Convert employee information into model input
    and return attrition prediction results.
    """

    input_df = create_employee_record(employee_data)

    result = predict_attrition(input_df)

    if not isinstance(result, (tuple, list)) or len(result) != 4:
        raise ValueError(
            "Unexpected prediction output. Expected four values."
        )

    prediction, probability, risk_score, risk_level = result

    return (
        float(probability),
        float(risk_score),
        risk_level,
        int(prediction)
    )


# --------------------------------------------------
# EMPLOYEE INFORMATION
# --------------------------------------------------

st.header("👤 Employee Information")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Employee Details")

    age = st.slider(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    monthly_income = st.slider(
        "Monthly Income (₹)",
        min_value=1000,
        max_value=100000,
        value=10000,
        step=500
    )

    distance = st.slider(
        "Distance From Home",
        min_value=1,
        max_value=30,
        value=5
    )

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )


with col2:

    st.subheader("Employee Experience")

    job_satisfaction = st.slider(
        "Job Satisfaction",
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

    environment_satisfaction = st.slider(
        "Environment Satisfaction",
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


# --------------------------------------------------
# RUN INTERVENTION SIMULATION
# --------------------------------------------------

st.divider()

if st.button(
    "🚀 Run Intervention Simulation",
    use_container_width=True,
    type="primary"
):

    # Original employee profile
    original_employee = {
        "Age": age,
        "MonthlyIncome": monthly_income,
        "DistanceFromHome": distance,
        "OverTime": overtime,
        "JobSatisfaction": job_satisfaction,
        "WorkLifeBalance": work_life_balance,
        "EnvironmentSatisfaction": environment_satisfaction,
        "YearsSinceLastPromotion": years_since_promotion,
        "JobRole": job_role
    }

    # --------------------------------------------------
    # DEFINE INTERVENTION SCENARIOS
    # --------------------------------------------------

    scenarios = {

        "Current Employee Profile":
            original_employee.copy(),

        "Salary Increase (+10%)": {
            **original_employee,
            "MonthlyIncome": round(
                monthly_income * 1.10
            )
        },

        "Overtime Removed": {
            **original_employee,
            "OverTime": "No"
        },

        "Promotion Opportunity": {
            **original_employee,
            "YearsSinceLastPromotion": 0
        },

        "Combined Intervention": {
            **original_employee,
            "MonthlyIncome": round(
                monthly_income * 1.10
            ),
            "OverTime": "No",
            "YearsSinceLastPromotion": 0
        }
    }

    results = []

    # --------------------------------------------------
    # GENERATE PREDICTIONS
    # --------------------------------------------------

    try:

        with st.spinner(
            "Calculating employee intervention scenarios..."
        ):

            for scenario_name, scenario_employee in scenarios.items():

                (
                    probability,
                    risk_score,
                    risk_level,
                    prediction
                ) = get_attrition_probability(
                    scenario_employee
                )

                results.append({

                    "Scenario": scenario_name,

                    "Attrition Probability (%)": round(
                        risk_score, 2
                    ),

                    "Risk Level": risk_level,

                    "Prediction": (
                        "Likely Leave"
                        if prediction == 1
                        else "Likely Stay"
                    )
                })

        results_df = pd.DataFrame(results)

        # --------------------------------------------------
        # CALCULATE RETENTION IMPROVEMENT
        # --------------------------------------------------

        baseline_probability = results_df.iloc[0][
            "Attrition Probability (%)"
        ]

        results_df["Retention Improvement (%)"] = (
            baseline_probability
            - results_df["Attrition Probability (%)"]
        ).round(2)

        # Store simulation results
        st.session_state["what_if_results"] = results_df

        st.session_state["what_if_baseline"] = (
            baseline_probability
        )

        st.session_state["what_if_employee"] = (
            original_employee
        )

    except Exception as error:

        st.error(
            f"Unable to complete simulation: {error}"
        )


# --------------------------------------------------
# DISPLAY SIMULATION RESULTS
# --------------------------------------------------

if "what_if_results" in st.session_state:

    results_df = st.session_state["what_if_results"]

    baseline_probability = st.session_state[
        "what_if_baseline"
    ]

    st.divider()

    st.header("📊 Intervention Simulation Results")

    st.metric(
        "Current Attrition Probability",
        f"{baseline_probability:.2f}%"
    )

    st.caption(
        "All intervention scenarios are compared "
        "against the original employee profile."
    )

    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # ATTRITION PROBABILITY CHART
    # --------------------------------------------------

    st.divider()

    st.subheader("📉 Attrition Probability Comparison")

    chart_data = results_df.set_index(
        "Scenario"
    )["Attrition Probability (%)"]

    st.bar_chart(
        chart_data,
        horizontal=True
    )


    # --------------------------------------------------
    # RETENTION IMPROVEMENT
    # --------------------------------------------------

    st.divider()

    st.subheader("🎯 Retention Improvement")

    intervention_results = results_df.iloc[1:].copy()

    best_index = intervention_results[
        "Retention Improvement (%)"
    ].idxmax()

    best_scenario = intervention_results.loc[
        best_index
    ]

    best_improvement = best_scenario[
        "Retention Improvement (%)"
    ]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Best Intervention",
            best_scenario["Scenario"]
        )

    with col2:

        st.metric(
            "Probability Reduction",
            f"{best_improvement:.2f} percentage points"
        )

    if best_improvement > 0:

        st.success(
            f"The {best_scenario['Scenario']} scenario "
            f"produced the largest predicted reduction "
            f"in attrition probability."
        )

    elif best_improvement == 0:

        st.info(
            "The tested interventions did not change "
            "the predicted attrition probability."
        )

    else:

        st.warning(
            "The tested interventions increased the "
            "predicted attrition probability."
        )


    # --------------------------------------------------
    # BUSINESS INSIGHTS
    # --------------------------------------------------

    st.divider()

    st.header("💡 Business Insights")

    for _, row in intervention_results.iterrows():

        improvement = row[
            "Retention Improvement (%)"
        ]

        if improvement > 0:

            st.success(
                f"**{row['Scenario']}**: Predicted attrition "
                f"probability decreased by "
                f"{improvement:.2f} percentage points."
            )

        elif improvement < 0:

            st.warning(
                f"**{row['Scenario']}**: Predicted attrition "
                f"probability increased by "
                f"{abs(improvement):.2f} percentage points."
            )

        else:

            st.info(
                f"**{row['Scenario']}**: No change in "
                f"predicted attrition probability."
            )


    # --------------------------------------------------
    # INTERVENTION DETAILS
    # --------------------------------------------------

    st.divider()

    st.header("📋 Intervention Details")

    st.markdown(
        """
        | Intervention | Simulated Change |
        |---|---|
        | Salary Increase | Monthly income increased by 10% |
        | Overtime Removed | OverTime changed to No |
        | Promotion Opportunity | Years since last promotion set to 0 |
        | Combined Intervention | All three changes applied together |
        """
    )


    # --------------------------------------------------
    # FINAL NOTE
    # --------------------------------------------------

    st.divider()

    st.info(
        """
        **Important:** These results are model-based simulations.
        They indicate how the trained model's predicted attrition
        probability changes when employee attributes are modified.

        They do not guarantee employee retention or establish
        a causal relationship between an HR intervention
        and actual attrition.
        """
    )


    # --------------------------------------------------
    # RESET SIMULATION
    # --------------------------------------------------

    if st.button(
        "🔄 Clear Simulation Results",
        use_container_width=True
    ):

        st.session_state.pop(
            "what_if_results", None
        )

        st.session_state.pop(
            "what_if_baseline", None
        )

        st.session_state.pop(
            "what_if_employee", None
        )

        st.rerun()
