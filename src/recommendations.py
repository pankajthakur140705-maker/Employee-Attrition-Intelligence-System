def generate_recommendations(employee):

    recommendations = []

    overtime = employee.get(
        "OverTime",
        "No"
    )

    monthly_income = employee.get(
        "MonthlyIncome",
        10000
    )

    job_satisfaction = employee.get(
        "JobSatisfaction",
        3
    )

    environment_satisfaction = employee.get(
        "EnvironmentSatisfaction",
        3
    )

    work_life_balance = employee.get(
        "WorkLifeBalance",
        3
    )

    years_since_promotion = employee.get(
        "YearsSinceLastPromotion",
        0
    )

    distance_from_home = employee.get(
        "DistanceFromHome",
        5
    )

    job_role = employee.get(
        "JobRole",
        "Unknown"
    )

    # Overtime

    if overtime == "Yes":

        recommendations.append(
            "Reduce overtime workload and monitor employee burnout levels."
        )

    # Salary

    if monthly_income < 5000:

        recommendations.append(
            "Review compensation package and evaluate salary competitiveness."
        )

    elif monthly_income < 10000:

        recommendations.append(
            "Consider performance incentives or retention bonuses."
        )

    # Job Satisfaction

    if job_satisfaction <= 2:

        recommendations.append(
            "Conduct employee engagement sessions and gather feedback."
        )

    # Environment Satisfaction

    if environment_satisfaction <= 2:

        recommendations.append(
            "Improve workplace culture and manager support."
        )

    # Work Life Balance

    if work_life_balance <= 2:

        recommendations.append(
            "Implement flexible working policies and improve work-life balance."
        )

    # Promotion Delay

    if years_since_promotion >= 5:

        recommendations.append(
            "Discuss promotion opportunities and career development plans."
        )

    # Distance From Home

    if distance_from_home >= 20:

        recommendations.append(
            "Consider remote work or flexible scheduling options."
        )

    # High Risk Roles

    high_risk_roles = [
        "Sales Representative",
        "Laboratory Technician"
    ]

    if job_role in high_risk_roles:

        recommendations.append(
            f"Provide additional retention support for {job_role} employees."
        )

    # No Risks

    if len(recommendations) == 0:

        recommendations.append(
            "Employee profile appears healthy. Continue recognition, learning, and career development initiatives."
        )

    return recommendations


def get_retention_priority(employee):

    score = 0

    if employee.get("OverTime") == "Yes":
        score += 2

    if employee.get("MonthlyIncome", 10000) < 5000:
        score += 2

    if employee.get("JobSatisfaction", 3) <= 2:
        score += 2

    if employee.get("WorkLifeBalance", 3) <= 2:
        score += 2

    if employee.get("YearsSinceLastPromotion", 0) >= 5:
        score += 2

    if score >= 8:
        return "High"

    elif score >= 4:
        return "Medium"

    else:
        return "Low"


def generate_hr_action_plan(employee):

    priority = get_retention_priority(
        employee
    )

    if priority == "High":

        return [
            "Immediate HR intervention",
            "Salary review",
            "Career growth discussion",
            "Reduce overtime exposure",
            "Manager feedback meeting"
        ]

    elif priority == "Medium":

        return [
            "Monthly employee check-ins",
            "Recognition program",
            "Engagement survey",
            "Skill development opportunities"
        ]

    else:

        return [
            "Continue current engagement strategy",
            "Maintain recognition initiatives",
            "Monitor employee satisfaction"
        ]