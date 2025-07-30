import streamlit as st
import json
import os

st.set_page_config(page_title="SmartSurveyOps", layout="centered")

survey = None

# Attempt to load the survey JSON file
survey_path = "generated_survey.json"

if os.path.exists(survey_path):
    try:
        with open(survey_path, "r") as f:
            survey = json.load(f)
    except Exception as e:
        st.error(f"Error loading JSON file: {e}")
else:
    st.error(f"Survey file not found at path: {survey_path}")

# If loading failed, provide fallback empty survey
if not isinstance(survey, dict):
    survey = {
        "surveyTitle": "Survey Unavailable",
        "questions": []
    }

st.title(survey.get("surveyTitle", "Customer Survey"))

# ...rest of your app code here...
