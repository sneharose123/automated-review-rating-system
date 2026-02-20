import streamlit as st
import joblib
import os

model_A = joblib.load("Model_A.pkl")

st.title("📚📝Automated Review Rating System ⭐")

review_text = st.text_area("Enter a review🖋️:")

if st.button("Predict Rating"):
    if review_text.strip() == "":
        st.warning("Please enter a review")
    else:
        prediction = model_A.predict([review_text])[0]
        st.success(f"Predicted Rating: ⭐ {prediction}")