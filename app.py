import streamlit as st
import json

st.set_page_config(page_title="SmartSurveyOps", layout="centered")

# Load survey JSON safely
try:
    with open("generated_survey.json", "r") as f:
        survey = json.load(f)
except Exception as e:
    st.error(f"Failed to load survey file: {e}")
    # Provide fallback empty survey so app doesn't break
    survey = {
        "surveyTitle": "Survey Unavailable",
        "questions": []
    }

st.title(survey.get("surveyTitle", "Customer Survey"))

responses = {}

with st.form("survey_form"):
    for i, question in enumerate(survey["questions"]):
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
