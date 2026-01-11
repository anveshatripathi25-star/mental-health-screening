import streamlit as st

# Page config
st.set_page_config(page_title="Mental Health Screening", layout="centered")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>🧠 AI Mental Health Screening & Wellness Support Agent</h1>",
    unsafe_allow_html=True
)

# Disclaimer box
st.warning(
    "⚠️ **Disclaimer:** This tool is for awareness and early screening only. "
    "It does NOT provide medical diagnosis."
)

st.markdown("---")

# Scale explanation
st.markdown("### 🔢 Response Scale")
st.info(
    """
    **0** – Not at all  
    **1** – Several days  
    **2** – More than half the days  
    **3** – Nearly every day  
    """
)

st.markdown("---")

# Questions
st.markdown("### 📝 Please answer the following questions:")

questions = [
    "Feeling nervous, anxious, or on edge?",
    "Trouble relaxing or sleeping?",
    "Feeling tired or low on energy?",
    "Difficulty concentrating on daily tasks?",
    "Feeling sad or hopeless?"
]

responses = []

for q in questions:
    responses.append(
        st.selectbox(q, [0, 1, 2, 3], key=q)
    )

st.markdown("---")

# Button
if st.button("🔍 Check Mental Health Risk"):
    score = sum(responses)

    st.markdown(f"### 📊 **Your Total Risk Score:** `{score}`")

    if score <= 4:
        st.success(
            "🟢 **LOW RISK**\n\n"
            "• Maintain a healthy routine\n"
            "• Exercise regularly\n"
            "• Practice mindfulness"
        )

    elif score <= 8:
        st.warning(
            "🟡 **MODERATE RISK**\n\n"
            "• Practice stress management\n"
            "• Take regular breaks\n"
            "• Talk to friends or family"
        )

    else:
        st.error(
            "🔴 **HIGH RISK**\n\n"
            "• Please consider seeking professional help\n"
            "• Reach out to a trusted person"
        )

        st.markdown(
            "📞 **Emergency Helpline (India):**  \n"
            "**Kiran Mental Health Helpline – 1800-599-0019 (24/7)**"
        )

st.markdown("---")

# Footer
st.markdown(
    "<p style='text-align: center; color: grey;'>"
    "© 2026 | AI Mental Health Screening Project | SDG 3 – Good Health & Well-Being"
    "</p>",
    unsafe_allow_html=True
)
