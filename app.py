import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mental Health Chatbot",
    page_icon="🧠",
    layout="centered"
)

# ---------------- SESSION INIT ----------------
if "started" not in st.session_state:
    st.session_state.started = False

# ---------------- WELCOME ANIMATION ----------------
if not st.session_state.started:
    st.markdown(
        """
        <div style="background-color:#E8F4FD;padding:25px;border-radius:15px;text-align:center;">
            <h2 style="color:#1F4E79;">🧠 Welcome to the AI Mental Health Support Chatbot</h2>
            <p style="font-size:16px;">Your friendly assistant for early mental health screening</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.spinner("🤖 Bot is getting ready..."):
        time.sleep(2)

    st.success("✨ Ready to chat!")

    if st.button("▶️ Start Chat"):
        st.session_state.started = True
        st.rerun()

    st.stop()

# ---------------- MAIN CHATBOT UI ----------------

st.markdown(
    "<h2 style='text-align:center;color:#2E86C1;'>🤖 Mental Health Support Chatbot</h2>",
    unsafe_allow_html=True
)

st.warning(
    "⚠️ **Disclaimer:** This chatbot is for awareness and early screening only. "
    "It does NOT provide medical diagnosis."
)

with st.expander("ℹ️ Response Scale"):
    st.markdown(
        """
        **0** – Not at all  
        **1** – Several days  
        **2** – More than half the days  
        **3** – Nearly every day  
        """
    )

st.markdown("---")

questions = [
    "Hello 👋 How often have you been feeling nervous or anxious?",
    "How often do you have trouble relaxing or sleeping?",
    "How often do you feel tired or low on energy?",
    "How often do you find it difficult to concentrate?",
    "How often do you feel sad or hopeless?"
]

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = []

# ---------------- CHAT FLOW ----------------
if st.session_state.step < len(questions):

    st.markdown(
        f"""
        <div style="background-color:#F1F8FF;padding:15px;border-radius:12px;">
            🤖 <b>Bot:</b> {questions[st.session_state.step]}
        </div>
        """,
        unsafe_allow_html=True
    )

    response = st.selectbox(
        "Your response:",
        [0, 1, 2, 3],
        key=f"q_{st.session_state.step}"
    )

    if st.button("➡️ Send"):
        st.session_state.responses.append(response)
        st.session_state.step += 1
        st.rerun()

# ---------------- RESULT ----------------
else:
    score = sum(st.session_state.responses)

    st.markdown("### 📊 Chatbot Analysis Completed")
    st.markdown(f"**Total Risk Score:** `{score}`")

    if score <= 4:
        st.success(
            "🟢 **LOW RISK**\n\nMaintain a healthy routine and practice self-care."
        )
    elif score <= 8:
        st.warning(
            "🟡 **MODERATE RISK**\n\nTry stress management and talk to someone you trust."
        )
    else:
        st.error(
            "🔴 **HIGH RISK**\n\nPlease consider seeking professional help."
        )
        st.markdown(
            "📞 **Kiran Mental Health Helpline (India): 1800-599-0019**"
        )

    if st.button("🔄 Restart Chat"):
        st.session_state.started = False
        st.session_state.step = 0
        st.session_state.responses = []
        st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;font-size:13px;'>"
    "AI Mental Health Screening Project | SDG 3 – Good Health & Well-Being"
    "</p>",
    unsafe_allow_html=True
)
