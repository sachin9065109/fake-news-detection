import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.title("📰 Fake News Detection System (AI Powered)")

# -----------------------
# Sample Training Data
# -----------------------
data = {
    "text": [
        "India won the cricket match yesterday",
        "The government launched a new education policy",
        "You have won a lottery send money to claim prize",
        "This is a scam offer send bank details immediately",
        "New metro line opened in Delhi",
        "Click here to get free iphone now"
    ],
    "label": [0, 0, 1, 1, 0, 1]  # 0 = Real, 1 = Fake
}

df = pd.DataFrame(data)

# -----------------------
# Model Training
# -----------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
model = LogisticRegression()
model.fit(X, df["label"])

# -----------------------
# Session History
# -----------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------
# Input
# -----------------------
text = st.text_area("Enter News Text")

if st.button("Predict"):

    input_data = vectorizer.transform([text])
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0]

    confidence = max(prob) * 100

    if prediction == 1:
        result = f"⚠️ Fake News (Confidence: {confidence:.2f}%)"
    else:
        result = f"✅ Real News (Confidence: {confidence:.2f}%)"

    st.write(result)

    # save history
    st.session_state.history.append((text, result))

# -----------------------
# History Section
# -----------------------
st.subheader("📌 Prediction History")

for t, r in reversed(st.session_state.history):
    st.write("📰", t)
    st.write("➡️", r)
    st.write("---")
