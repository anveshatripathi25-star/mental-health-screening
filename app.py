import streamlit as st

st.title("AI Mental Health Screening & Wellness Support Agent")

st.warning("This tool is for awareness only. Not a medical diagnosis.")

questions = [
    "Feeling nervous, anxious, or on edge?",
    "Trouble relaxing or sleeping?",
    "Feeling tired or low on energy?",
    "Difficulty concentrating?",
    "Feeling sad or hopeless?"
]

responses = []

for q in questions:
    responses.append(st.selectbox(q, [0, 1, 2, 3]))

if st.button("Check Mental Health Risk"):
    score = sum(responses)

    if score <= 4:
        st.success("LOW RISK: Maintain healthy routine and self-care.")
    elif score <= 8:
        st.warning("MODERATE RISK: Practice stress management.")
    else:
        st.error("HIGH RISK: Seek professional help.")
        st.write("📞 Kiran Helpline: 1800-599-0019")

    st.write("Risk Score:", score)
