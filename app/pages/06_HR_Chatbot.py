import streamlit as st
from src.gemini_chatbot import ask_hr_assistant

st.set_page_config(
    page_title="Gemini HR Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Gemini HR Assistant")

st.markdown("""
### AI-Powered HR Consultant

Ask questions about employee attrition, retention strategies,
risk factors, HR interventions, and workforce analytics.
""")

st.markdown("---")

st.subheader("📊 Current Employee Risk Context")

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

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Current Risk Score",
        str(risk_score)
    )

with col2:

    st.metric(
        "Top Risk Factors",
        len(top_factors)
    )

st.markdown("---")

st.subheader("🎯 Available Employee Context")

if top_factors:

    st.write("Top Factors:")

    for factor in top_factors:

        st.info(factor)

else:

    st.warning(
        "No prediction context available yet. Run a prediction first."
    )

if recommendations:

    st.write("Retention Recommendations:")

    for rec in recommendations:

        st.success(rec)

st.markdown("---")

st.subheader("💬 Ask the HR Assistant")

question = st.text_area(
    "Enter your question",
    height=120,
    placeholder="""
Examples:

Why is this employee at risk?

How can HR reduce attrition?

What retention strategy should be used?

Explain the attrition risk score.

How does overtime affect attrition?
"""
)

col_a, col_b = st.columns(2)

with col_a:

    if st.button(
        "🚀 Generate Response",
        use_container_width=True
    ):

        if not question:

            st.warning(
                "Please enter a question."
            )

        else:

            try:

                with st.spinner(
                    "Gemini is analyzing..."
                ):

                    answer = ask_hr_assistant(
                        question,
                        risk_score,
                        top_factors,
                        recommendations
                    )

                st.markdown("---")

                st.subheader(
                    "🧠 Gemini Response"
                )

                st.write(answer)

            except Exception as e:

                st.error(
                    f"Gemini Error: {e}"
                )

with col_b:

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):

        st.rerun()

st.markdown("---")

st.subheader("⚡ Quick Questions")

quick_questions = [
    "Why is this employee at risk?",
    "Explain the attrition risk score.",
    "What retention strategy should HR use?",
    "How can HR reduce attrition?",
    "What are the major risk factors?"
]

for q in quick_questions:

    if st.button(q):

        try:

            answer = ask_hr_assistant(
                q,
                risk_score,
                top_factors,
                recommendations
            )

            st.markdown("---")

            st.subheader(
                "🧠 Gemini Response"
            )

            st.write(answer)

        except Exception as e:

            st.error(
                f"Gemini Error: {e}"
            )

st.markdown("---")

st.success("""
✅ Gemini HR Assistant is connected to your prediction engine,
retention recommendation engine, and what-if analysis system.
""")