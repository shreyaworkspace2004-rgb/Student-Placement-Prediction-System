#  Student Placement Prediction System

An end-to-end Machine Learning web application built with **Streamlit**, **Scikit-Learn**, and **Joblib** to predict whether a student is likely to get campus placed based on their academic and skill profile[cite: 41].

---

##  Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-blue?style=for-the-badge)

---

##  Features & User Inputs

The model evaluates placement readiness across 5 key parameters[cite: 41]:

* **CGPA:** Academic score on a scale of 0.0 to 10.0[cite: 41]
* **Number of Internships:** Total industrial internships completed[cite: 41]
* **Number of Projects:** Technical and academic portfolio projects[cite: 41]
* **Aptitude Score:** Quantitative and logical test evaluation (0–100)[cite: 41]
* **Communication Score:** Soft skills and interview readiness rating (0–100)[cite: 41]

---

##  Project Directory Structure

```text
├── models/
│   └── placement_model.pkl
├── app.py
├── requirements.txt
└── README.md

```
## Clone the Repository

git clone [https://github.com/your-username/student-placement-prediction.git](https://github.com/your-username/student-placement-prediction.git)
cd student-placement-prediction

```
## Install Required Libraries

pip install streamlit joblib numpy scikit-learn

```
## Run the Streamlit Application

streamlit run app.py
