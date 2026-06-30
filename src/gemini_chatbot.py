import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )
else:
    model = None


def ask_hr_assistant(
    question,
    risk_score,
    top_factors,
    recommendations
):

    if model is None:

        return """
❌ Gemini API Key not found.

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here
"""

    prompt = f"""
You are a Senior HR Analytics Consultant.

You are assisting HR managers using an Employee Attrition Intelligence System.

========================
EMPLOYEE ATTRITION DATA
========================

Attrition Risk Score:
{risk_score}%

Top Risk Factors:
{top_factors}

Recommended Retention Actions:
{recommendations}

========================
USER QUESTION
========================

{question}

========================
RESPONSE RULES
========================

Provide:

1. Executive Summary

2. Risk Interpretation

3. Business Impact

4. HR Recommendations

5. Final Conclusion

Keep the response professional,
easy to understand,
and suitable for HR managers.

Do not use technical ML terminology unless asked.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"""
❌ Gemini Error

{str(e)}
"""


def get_hr_analysis(
    employee_data,
    risk_score,
    top_factors=None,
    recommendations=None
):

    if model is None:

        return "Gemini API Key not configured."

    prompt = f"""
You are an HR Attrition Specialist.

Analyze the following employee profile.

Employee Data:
{employee_data}

Attrition Risk Score:
{risk_score}%

Top Risk Factors:
{top_factors}

Retention Recommendations:
{recommendations}

Provide:

1. Employee Risk Assessment

2. Key Risk Drivers

3. Business Impact

4. Recommended HR Actions

5. Executive Summary

Keep the response concise,
professional,
and HR-focused.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {str(e)}"