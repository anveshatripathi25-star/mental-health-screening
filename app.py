import streamlit as st

st.set_page_config(page_title="Mental Health Chatbot", layout="centered")

st.markdown(
    "<h1 style='text-align:center;color:#2E86C1;'>🤖 Mental Health Support Chatbot</h1>",
    unsafe_allow_html=True
)

st.warning(
    "⚠️ Disclaimer: I am not a doctor. This chatbot is for awareness and early screening only."
)

st.markdown("---")

st.markdown("### 💬 Chat with the Assistant")

questions = [
    "Hello! How often have you been feeling nervous or anxious?",
    "How often do you have trouble relaxing or sleeping?",
    "How often do you feel tired or low on energy?",
    "How often do you face difficulty concentrating?",
    "How often do you feel sad or hopeless?"
]

st.info(
    """
    **Response Scale**
    - 0: Not at all
    - 1: Several days
    - 2: More than half the days
    - 3: Nearly every day
    """
)

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = []

if st.session_state.step < len(questions):
    st.markdown(f"**Bot:** {questions[st.session_state.step]}")

    response = st.selectbox(
        "Your response:",
        [0, 1, 2, 3],
        key=f"q_{st.session_state.step}"
    )

    if st.button("Send"):
        st.session_state.responses.append(response)
        st.session_state.step += 1
        st.rerun()   # ✅ FIXED LINE

else:
    score = sum(st.session_state.responses)

    st.markdown("### 📊 Chatbot Analysis Result")
    st.write("**Total Risk Score:**", score)

    if score <= 4:
        st.success(
            "🟢 **Low Risk**\n\nYou seem to be doing okay. Maintain a healthy routine and self-care."
        )
    elif score <= 8:
        st.warning(
            "🟡 **Moderate Risk**\n\nTry stress management techniques and talk to someone you trust."
        )
    else:
        st.error(
            "🔴 **High Risk**\n\nPlease seek professional help."
        )
        st.markdown(
            "**📞 Kiran Mental Health Helpline (India): 1800-599-0019**"
        )

    if st.button("Restart Chat"):
        st.session_state.step = 0
        st.session_state.responses = []
        st.rerun()
