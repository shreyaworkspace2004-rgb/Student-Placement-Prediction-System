import streamlit as st
import joblib
import numpy as np
import os

# Current project folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model path
MODEL_PATH = os.path.join(BASE_DIR, "models", "placement_model.pkl")

# Check if model exists
if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found!\nExpected location:\n{MODEL_PATH}")
    st.stop()

# Load model
model = joblib.load(MODEL_PATH)

# Page settings
st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Placement Prediction System")

st.markdown("""
Enter student details below and click **Predict Placement**.
""")

# Inputs
cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

internship = st.number_input(
    "Number of Internships",
    min_value=0,
    max_value=10,
    value=1
)

projects = st.number_input(
    "Number of Projects",
    min_value=0,
    max_value=20,
    value=2
)

aptitude = st.number_input(
    "Aptitude Score",
    min_value=0,
    max_value=100,
    value=70
)

communication = st.number_input(
    "Communication Score",
    min_value=0,
    max_value=100,
    value=70
)

# Prediction Button
if st.button("Predict Placement"):

    data = np.array([
        [
            cgpa,
            internship,
            projects,
            aptitude,
            communication
        ]
    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Student is Likely to be Placed")
        st.balloons()
    else:
        st.error("❌ Student is Not Likely to be Placed")

# Footer
st.markdown("---")
st.caption("Machine Learning Project - Student Placement Prediction")