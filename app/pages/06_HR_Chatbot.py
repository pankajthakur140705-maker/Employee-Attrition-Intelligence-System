
import sys
from pathlib import Path

import streamlit as st

# --------------------------------------------------
# PROJECT IMPORTS
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.gemini_chatbot import ask_hr_assistant, get_gemini_status


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Gemini HR Assistant",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("🤖 Gemini HR Assistant")

st.markdown(
    """
    ### AI-Powered HR Assistant

    Ask questions about employee attrition, retention strategies,
    HR interventions, workforce analytics, and model predictions.

    The assistant uses Google's Gemini API to generate responses.
    """
)

st.divider()


# --------------------------------------------------
# GEMINI STATUS
# --------------------------------------------------

try:
    gemini_status = get_gemini_status()

    if gemini_status.get("available", False):
        st.success("Gemini AI is available.")
    else:
        st.warning(
            "Gemini AI is currently unavailable. "
            "Check your API key and application configuration."
        )

        if gemini_status.get("error"):
            st.caption(str(gemini_status["error"]))

except Exception as error:
    st.warning(f"Unable to verify Gemini status: {error}")


# --------------------------------------------------
# LOAD PREDICTION CONTEXT
# --------------------------------------------------

risk_score = st.session_state.get(
    "risk_score",
    "Unknown"
)

top_factors = st.session_state.get(
    "top_factors",
    []
)

recommendations = st.session_state.get(
    "recommendations",
    []
)


# --------------------------------------------------
# EMPLOYEE RISK CONTEXT
# --------------------------------------------------

st.header("📊 Current Employee Context")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Current Attrition Risk Score",
        (
            f"{risk_score}%"
            if isinstance(risk_score, (int, float))
            else str(risk_score)
        )
    )

with col2:

    st.metric(
        "Available Model Features",
        len(top_factors)
    )


if risk_score == "Unknown":

    st.info(
        "No prediction context is available. "
        "Run an employee prediction from the Prediction page first."
    )


# --------------------------------------------------
# FEATURE IMPORTANCE CONTEXT
# --------------------------------------------------

st.subheader("🧠 Important Model Features")

if top_factors:

    st.caption(
        "These are the available model feature-importance labels. "
        "They are global model-level features, not necessarily "
        "the individual causes of this employee's risk."
    )

    for factor in top_factors:
        st.info(str(factor))

else:

    st.warning(
        "No feature-importance context is available yet."
    )


# --------------------------------------------------
# RETENTION RECOMMENDATIONS
# --------------------------------------------------

st.subheader("🎯 Available Retention Recommendations")

if recommendations:

    for recommendation in recommendations:
        st.success(str(recommendation))

else:

    st.info(
        "No retention recommendations are available. "
        "Generate a prediction first."
    )


st.divider()


# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------

if "hr_chat_history" not in st.session_state:
    st.session_state["hr_chat_history"] = []


# --------------------------------------------------
# DISPLAY PREVIOUS MESSAGES
# --------------------------------------------------

st.header("💬 HR Assistant Chat")

for message in st.session_state["hr_chat_history"]:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# RESPONSE GENERATION FUNCTION
# --------------------------------------------------

def generate_hr_response(question):

    if not question.strip():
        return

    # Display user question in chat history
    st.session_state["hr_chat_history"].append({
        "role": "user",
        "content": question
    })

    try:

        answer = ask_hr_assistant(
            question,
            risk_score,
            top_factors,
            recommendations
        )

        if not answer:
            answer = (
                "The HR Assistant could not generate a response. "
                "Please try again."
            )

    except Exception as error:

        answer = (
            f"Unable to generate a Gemini response: {error}"
        )

    # Store assistant response
    st.session_state["hr_chat_history"].append({
        "role": "assistant",
        "content": str(answer)
    })


# --------------------------------------------------
# USER QUESTION INPUT
# --------------------------------------------------

question = st.chat_input(
    "Ask something about employee attrition or retention..."
)

if question:

    generate_hr_response(question)

    st.rerun()


# --------------------------------------------------
# QUICK QUESTIONS
# --------------------------------------------------

st.divider()

st.subheader("⚡ Quick Questions")

quick_questions = [
    "Why is employee attrition a concern for organizations?",
    "How can HR reduce employee attrition?",
    "Explain the current employee attrition risk score.",
    "What retention strategies can HR implement?",
    "How can overtime affect employee retention?",
    "What is the importance of feature importance in XGBoost?"
]

for index, quick_question in enumerate(quick_questions):

    if st.button(
        quick_question,
        key=f"quick_question_{index}",
        use_container_width=True
    ):

        generate_hr_response(quick_question)
        st.rerun()


# --------------------------------------------------
# CHAT CONTROLS
# --------------------------------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):

        st.session_state["hr_chat_history"] = []
        st.rerun()

with col2:

    st.caption(
        "The assistant uses the latest prediction context "
        "available in this Streamlit session."
    )


# --------------------------------------------------
# DISCLAIMER
# --------------------------------------------------

st.divider()

st.caption(
    """
    Note: Gemini-generated responses are AI-generated suggestions.
    HR managers should verify recommendations before making
    employment or workforce decisions. Model predictions do not
    establish the actual cause of employee attrition.
    """
)
