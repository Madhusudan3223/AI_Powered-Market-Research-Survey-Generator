import streamlit as st
import json
import os

st.set_page_config(page_title="SmartSurveyOps", layout="centered")

survey_path = "generated_survey.json"
survey = None

# Load the survey JSON safely
if os.path.exists(survey_path):
    try:
        with open(survey_path, "r") as f:
            survey = json.load(f)
    except Exception as e:
        st.error(f"Failed to load JSON file: {e}")
else:
    st.error(f"Survey file not found: {survey_path}")

# Fallback if loading failed
if not isinstance(survey, dict):
    survey = {
        "surveyTitle": "Survey Unavailable",
        "questions": []
    }

# Display survey title
st.title(survey.get("surveyTitle", "Customer Survey"))

responses = {}

with st.form("survey_form"):
    for i, question in enumerate(survey.get("questions", [])):
        q_text = question.get("questionText", "")
        q_type = question.get("questionType", "")

        if q_type in ["rating", "multipleChoice"]:
            options = question.get("options", [])
            labels = [opt.get("label", "") for opt in options]
            selected = st.radio(q_text, labels, key=f"q{i}")
            responses[q_text] = selected

        elif q_type == "text":
            answer = st.text_area(q_text, key=f"q{i}")
            responses[q_text] = answer

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Thank you for your response!")
    st.write("### Your Responses:")
    st.json(responses)
