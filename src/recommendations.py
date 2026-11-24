
"""
Employee Attrition Intelligence System
Rule-Based Employee Retention Recommendation Engine

Recommendations follow the internship project report.
"""

def generate_recommendations(
    employee,
    organizational_average_income=None
):
    """
    Generate retention recommendations using employee attributes.

    Args:
        employee (dict): Employee information.
        organizational_average_income (float, optional):
            Organizational average monthly income.
            If not provided, salary-based recommendations are skipped.

    Returns:
        list: Retention recommendations.
    """

    recommendations = []

    overtime = employee.get("OverTime", "No")
    monthly_income = employee.get("MonthlyIncome")
    job_satisfaction = employee.get("JobSatisfaction", 3)
    work_life_balance = employee.get("WorkLifeBalance", 3)
    years_since_promotion = employee.get(
        "YearsSinceLastPromotion", 0
    )

    # 1. Overtime recommendation
    if overtime == "Yes":
        recommendations.append(
            "Reduce overtime workload and monitor employee burnout levels."
        )

    # 2. Salary recommendation
    if (
        organizational_average_income is not None
        and monthly_income is not None
        and monthly_income < organizational_average_income
    ):
        recommendations.append(
            "Review the employee's compensation package against "
            "the organizational average."
        )

    # 3. Job satisfaction recommendation
    if job_satisfaction <= 2:
        recommendations.append(
            "Conduct employee engagement programs and gather feedback "
            "to improve job satisfaction."
        )

    # 4. Work-life balance recommendation
    if work_life_balance <= 2:
        recommendations.append(
            "Consider flexible working arrangements to improve "
            "work-life balance."
        )

    # 5. Promotion and career development recommendation
    if years_since_promotion > 5:
        recommendations.append(
            "Review career development opportunities and discuss "
            "potential promotion pathways."
        )

    # No identified rule-based concerns
    if not recommendations:
        recommendations.append(
            "No retention concerns were identified by the configured "
            "rules. Continue employee engagement and development initiatives."
        )

    return recommendations
