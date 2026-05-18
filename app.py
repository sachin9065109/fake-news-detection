import streamlit as st

st.title("Fake News Detection System")

text = st.text_area("Enter News Text")

if st.button("Predict"):

    fake_words = ["fake", "fraud", "scam", "hoax"]

    score = 0

    for word in fake_words:
        if word in text.lower():
            score += 1

    if score > 0:
        st.error("⚠️ Potential Fake News")
    else:
        st.success("✅ Looks Real")
