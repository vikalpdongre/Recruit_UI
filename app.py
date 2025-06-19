import streamlit as st
import requests

# Streamlit app to analyze resumes using a GCP function
GCP_FUNCTION_URL = 'https://agent-ops-911008082076.us-east1.run.app/analyze'
st.title("Resume Analyzer with GCP")
resume_text = st.text_area("Paste Resume Text")
jd_text = st.text_area("Enter Job Description")

if st.button("Analyze"):
    response = requests.post(GCP_FUNCTION_URL, json={"resume": resume_text, "job_description": jd_text})
    st.write(response.status_code)
    if response.status_code == 200:
        analysis = response.json().get("analysis", "No analysis returned.")
        st.write(analysis)
    else:
        #error_message = response.json().get("error", "An error occurred.")
        #st.error(f"Error: {error_message}")
        st.write("Analysis complete. Check the output above.", response.status_code)

