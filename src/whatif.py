from src.preprocessing import create_employee_record
from src.prediction import predict_attrition


def what_if_analysis(
    employee_data,
    feature_name,
    new_value
):

    # Original Scenario

    original_df = create_employee_record(
        employee_data
    )

    (
        original_prediction,
        original_probability,
        original_risk_score,
        original_risk_level
    ) = predict_attrition(
        original_df
    )

    # Modified Scenario

    modified_employee = employee_data.copy()

    modified_employee[
        feature_name
    ] = new_value

    modified_df = create_employee_record(
        modified_employee
    )

    (
        modified_prediction,
        modified_probability,
        modified_risk_score,
        modified_risk_level
    ) = predict_attrition(
        modified_df
    )

    # Risk Change

    risk_difference = round(
        modified_risk_score -
        original_risk_score,
        2
    )

    # Business Interpretation

    if risk_difference > 5:

        impact = (
            "Attrition risk increased significantly."
        )

    elif risk_difference > 0:

        impact = (
            "Attrition risk increased slightly."
        )

    elif risk_difference < -5:

        impact = (
            "Attrition risk decreased significantly."
        )

    elif risk_difference < 0:

        impact = (
            "Attrition risk decreased slightly."
        )

    else:

        impact = (
            "No significant change detected."
        )

    return {

        "feature_changed":
            feature_name,

        "new_value":
            new_value,

        "original_prediction":
            original_prediction,

        "modified_prediction":
            modified_prediction,

        "original_probability":
            original_probability,

        "modified_probability":
            modified_probability,

        "original_risk_score":
            original_risk_score,

        "modified_risk_score":
            modified_risk_score,

        "original_risk_level":
            original_risk_level,

        "modified_risk_level":
            modified_risk_level,

        "risk_difference":
            risk_difference,

        "business_impact":
            impact
    }


def simulate_salary_increase(
    employee_data,
    increase_amount
):

    new_salary = (
        employee_data[
            "MonthlyIncome"
        ]
        + increase_amount
    )

    return what_if_analysis(
        employee_data,
        "MonthlyIncome",
        new_salary
    )


def simulate_overtime_removal(
    employee_data
):

    return what_if_analysis(
        employee_data,
        "OverTime",
        "No"
    )


def simulate_promotion(
    employee_data
):

    return what_if_analysis(
        employee_data,
        "YearsSinceLastPromotion",
        0
    )


def simulate_worklife_improvement(
    employee_data
):

    return what_if_analysis(
        employee_data,
        "WorkLifeBalance",
        4
    )


def generate_whatif_summary(
    result
):

    return f"""
Feature Changed:
{result['feature_changed']}

Original Risk:
{result['original_risk_score']}%

Modified Risk:
{result['modified_risk_score']}%

Risk Change:
{result['risk_difference']}%

Business Impact:
{result['business_impact']}
"""