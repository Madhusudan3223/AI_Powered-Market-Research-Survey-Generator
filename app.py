import streamlit as st
import json

# Load survey JSON
with open("generated_survey.json", "r") as f:
    survey = json.load(f)

st.set_page_config(page_title="SmartSurveyOps", layout="centered")
st.title(survey.get("surveyTitle", "Customer Survey"))

responses = {}

with st.form("survey_form"):
    for i, question in enumerate(survey["questions"]):
        q_text = question["questionText"]
        q_type = question["questionType"]
        
        if q_type == "rating" or q_type == "multipleChoice":
            options = question["options"]
            labels = [opt["label"] for opt in options]
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
