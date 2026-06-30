def hr_chatbot(question):

    q = question.lower()

    if any(word in q for word in ["why", "leave", "attrition"]):

        return """
🔍 Attrition Analysis

Employees generally leave because of:

• Excessive Overtime
• Low Job Satisfaction
• Poor Work-Life Balance
• Low Compensation
• Lack of Career Growth
• Delayed Promotions
• Poor Work Environment

Business Impact:
• Increased hiring cost
• Knowledge loss
• Reduced productivity

HR Recommendation:
• Conduct stay interviews
• Improve engagement
• Create promotion pathways
"""

    elif any(word in q for word in ["salary", "income", "compensation", "pay"]):

        return """
💰 Compensation Analysis

Salary is one of the strongest retention factors.

Warning Signs:

• Salary below market average
• Limited salary growth
• Pay inequity

Recommended Actions:

• Salary benchmarking
• Annual compensation review
• Performance incentives
• Retention bonuses

Expected Outcome:
Lower attrition probability and higher employee satisfaction.
"""

    elif any(word in q for word in ["overtime", "workload", "burnout"]):

        return """
⏰ Overtime Analysis

Overtime is a major driver of employee burnout.

Potential Risks:

• Stress
• Fatigue
• Reduced motivation
• Lower productivity

Recommended Actions:

• Reduce overtime dependency
• Increase staffing
• Flexible schedules
• Better workload distribution

Expected Outcome:
Improved retention and employee well-being.
"""

    elif any(word in q for word in ["promotion", "career", "growth"]):

        return """
📈 Career Growth Analysis

Employees expect continuous career progression.

Warning Signs:

• More than 5 years without promotion
• Lack of career roadmap
• Limited learning opportunities

Recommended Actions:

• Internal promotion plans
• Skill development programs
• Mentorship initiatives
• Leadership training

Expected Outcome:
Improved engagement and reduced attrition.
"""

    elif any(word in q for word in ["satisfaction", "engagement", "motivation"]):

        return """
😊 Employee Satisfaction Analysis

Low job satisfaction is strongly associated with attrition.

Improvement Strategies:

• Recognition programs
• Employee feedback surveys
• Better manager support
• Learning opportunities
• Team-building activities

Expected Outcome:
Higher employee loyalty and retention.
"""

    elif any(word in q for word in ["environment", "culture", "workplace"]):

        return """
🏢 Workplace Environment Analysis

A positive workplace environment improves retention.

Key Areas:

• Manager support
• Team collaboration
• Workplace culture
• Psychological safety

Recommended Actions:

• Leadership training
• Employee recognition
• Regular feedback sessions
• Diversity and inclusion initiatives
"""

    elif any(word in q for word in ["retention", "retain", "keep employees"]):

        return """
🎯 Employee Retention Strategy

Top Retention Strategies:

1. Reduce Overtime
2. Improve Compensation
3. Increase Job Satisfaction
4. Promote Career Growth
5. Improve Work-Life Balance
6. Strengthen Workplace Culture
7. Conduct Stay Interviews
8. Employee Recognition Programs

Expected Result:
Lower attrition and higher employee engagement.
"""

    elif any(word in q for word in ["top factors", "risk factors"]):

        return """
⚠️ Top Employee Attrition Factors

1. Overtime
2. Monthly Income
3. Job Satisfaction
4. Work-Life Balance
5. Years Since Last Promotion
6. Environment Satisfaction
7. Distance From Home
8. Age
9. Job Role

These are the most influential factors used by the prediction model.
"""

    elif any(word in q for word in ["high risk", "risk score"]):

        return """
🚨 High Risk Employee Interpretation

A high attrition risk score indicates that the employee shows multiple characteristics commonly associated with resignation.

Possible Reasons:

• Low satisfaction
• High overtime
• Low salary
• Career stagnation

Recommended Actions:

• Immediate HR discussion
• Manager intervention
• Compensation review
• Career development planning
"""

    elif any(word in q for word in ["xgboost", "model", "prediction"]):

        return """
🤖 Model Information

Algorithm:
XGBoost Classifier

Explainability:
SHAP (SHapley Additive Explanations)

Optimization:
Bayesian Optimization

Purpose:
Predict the probability of employee attrition and identify major risk factors.

Dataset:
IBM HR Analytics Employee Attrition Dataset
"""

    else:

        return """
🤖 HR Assistant

I can answer questions about:

• Attrition Analysis
• Salary & Compensation
• Overtime & Burnout
• Promotions & Career Growth
• Job Satisfaction
• Workplace Environment
• Retention Strategies
• Risk Factors
• High Risk Employees
• XGBoost Model Information

Example Questions:

• Why are employees leaving?
• How does salary affect attrition?
• What are the top risk factors?
• How can HR improve retention?
• Explain overtime impact.
"""