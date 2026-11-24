
import os
from pathlib import Path

from dotenv import load_dotenv


# ==========================================
# PROJECT CONFIGURATION
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Load local environment variables.
load_dotenv(PROJECT_ROOT / ".env")


# ==========================================
# GEMINI CONFIGURATION
# ==========================================

GEMINI_MODEL_NAME = "gemini-2.5-flash"

API_KEY = os.getenv("GEMINI_API_KEY")

# Support Streamlit Cloud Secrets.
try:
    import streamlit as st

    if not API_KEY:
        API_KEY = st.secrets.get(
            "GEMINI_API_KEY",
            None
        )

except Exception:
    pass


# ==========================================
# INITIALIZE GEMINI
# ==========================================

model = None
GEMINI_AVAILABLE = False
GEMINI_ERROR = None

try:

    if not API_KEY:

        GEMINI_ERROR = "Gemini API key is not configured."

    else:

        import google.generativeai as genai

        genai.configure(
            api_key=API_KEY
        )

        model = genai.GenerativeModel(
            GEMINI_MODEL_NAME
        )

        GEMINI_AVAILABLE = True

except ImportError:

    GEMINI_ERROR = (
        "Google Generative AI package is not installed. "
        "Install google-generativeai."
    )

except Exception as e:

    GEMINI_ERROR = str(e)


# ==========================================
# COMMON GEMINI RESPONSE FUNCTION
# ==========================================

def generate_response(prompt):

    """
    Generate a response using Google Gemini.

    Returns a text response or a readable error message.
    """

    if not GEMINI_AVAILABLE or model is None:

        return (
            "Gemini Assistant is currently unavailable. "
            "Please configure the API key and dependencies. "
            f"Details: {GEMINI_ERROR}"
        )

    try:

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.4,
                "max_output_tokens": 1500
            }
        )

        if response is None:

            return "Gemini returned an empty response."

        response_text = response.text

        if not response_text:

            return (
                "Gemini could not generate a text response. "
                "Please try asking your question again."
            )

        return response_text.strip()

    except Exception as e:

        return (
            "Gemini API Error: "
            f"{str(e)}"
        )


# ==========================================
# GEMINI HR CHATBOT
# ==========================================

def ask_hr_assistant(
    question,
    risk_score=None,
    top_factors=None,
    recommendations=None
):

    """
    Interactive HR Assistant.

    Provides:
    - Natural language explanations
    - Employee risk interpretation
    - Retention recommendations
    - HR analytics support
    - Interactive question answering
    """

    if not question or not str(question).strip():

        return "Please enter an HR-related question."

    prompt = f"""
You are a professional HR Analytics Consultant.

You assist HR managers using an Employee Attrition
Intelligence System developed using Machine Learning,
XGBoost and Google Gemini.

The project uses the IBM HR Analytics Employee Attrition
Dataset.

====================================
CURRENT EMPLOYEE ATTRITION CONTEXT
====================================

Predicted Attrition Risk:
{risk_score if risk_score is not None else "Not provided"}%

Important Model Features:
{top_factors if top_factors is not None else "Not provided"}

Retention Recommendations:
{recommendations if recommendations is not None else "Not provided"}

====================================
USER QUESTION
====================================

{question}

====================================
RESPONSE GUIDELINES
====================================

Answer in a professional and practical manner.

Where relevant, structure the answer using:

1. Executive Summary
2. Risk Interpretation
3. Key Observations
4. HR Recommendations
5. Final Conclusion

Requirements:

- Use clear and simple business language.
- Provide actionable HR recommendations.
- Explain employee attrition concepts when necessary.
- Do not invent employee information or model results.
- Do not claim that feature importance proves causation.
- Do not guarantee that an employee will leave.
- Clearly distinguish predictions from actual employee outcomes.
- Treat employee information confidentially.

If the question is unrelated to HR analytics,
politely guide the user back to HR-related topics.
"""

    return generate_response(prompt)


# ==========================================
# AUTOMATED GEMINI HR ANALYSIS
# ==========================================

def get_hr_analysis(
    employee_data,
    risk_score,
    top_factors=None,
    recommendations=None
):

    """
    Automatically analyze an employee profile.

    Used by the Employee Attrition Prediction page.
    """

    if not isinstance(employee_data, dict):

        return "Invalid employee information provided."

    prompt = f"""
You are an experienced HR Analytics Specialist.

Analyze the following employee profile using the
context of an Employee Attrition Intelligence System.

====================================
EMPLOYEE PROFILE
====================================

{employee_data}

====================================
ATTRITION PREDICTION
====================================

Predicted Attrition Risk:
{risk_score}%

Important XGBoost Features:
{top_factors if top_factors is not None else "Not available"}

Rule-Based Retention Recommendations:
{recommendations if recommendations is not None else "Not available"}

====================================
ANALYSIS REQUIREMENTS
====================================

Provide the following sections:

1. EMPLOYEE RISK ASSESSMENT

Interpret the predicted attrition probability.

2. IMPORTANT OBSERVATIONS

Discuss relevant employee attributes and important
model features. Do not confuse global feature importance
with employee-specific causal explanations.

3. POTENTIAL BUSINESS IMPACT

Explain possible workforce implications if attrition occurs.

4. RETENTION STRATEGIES

Suggest practical interventions related to:

- Compensation
- Overtime and workload
- Job satisfaction
- Work-life balance
- Career development
- Employee engagement

5. EXECUTIVE HR SUMMARY

Provide a concise conclusion for HR managers.

====================================
IMPORTANT INSTRUCTIONS
====================================

- Use professional HR terminology.
- Do not invent missing employee information.
- Do not claim that predicted attrition is certain.
- Do not make unsupported claims about employee behaviour.
- Recommendations should be practical and ethical.
- Clearly identify predictions as model estimates.

Keep the response concise, structured and actionable.
"""

    return generate_response(prompt)


# ==========================================
# GEMINI STATUS
# ==========================================

def get_gemini_status():

    return {

        "available": GEMINI_AVAILABLE,

        "model": GEMINI_MODEL_NAME,

        "api_key_configured": bool(API_KEY),

        "error": GEMINI_ERROR

    }
