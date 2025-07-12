# analyzer_ui.py
import streamlit as st
import requests
from text_extraction import extract_text_from_pdf, extract_text_from_docx
import os
#GCP_FUNCTION_URL = os.getenv('GCP_FUNCTION_URL_OPS')
#FEEDBACK_BACKEND_URL = os.getenv('FEEDBACK_BACKEND_URL_OPS')
GCP_FUNCTION_URL = 'https://agent-ops-911008082076.us-east1.run.app/analyze'
FEEDBACK_BACKEND_URL = 'https://feedback-firestore-911008082076.europe-west1.run.app'
def main_analyzer_app():
    """Contains the main application functionality, accessible after login."""
    #add user name in the header
    if "username" in st.session_state:
        st.header(f"Welcome, {st.session_state['username']}! 🎉")
    st.title("Advanced Resume & Job Description Analyzer")
    st.markdown("Upload  resume and a job description to get an instant analysis!")

    # --- Resume Upload Section ---
    st.header("Upload  Resume")
    resume_content_to_send = ""
    resume_text_input = ""  
    resume_file = st.file_uploader("Choose a PDF or Word file for  Resume", type=["pdf", "docx"], key="resume_upload", accept_multiple_files=False)
    # Allow users to paste resume text as an alternative to file upload, hide and show text area check box
    if st.checkbox("You can also paste  resume text below if you prefer not to upload a file.", value=False, key="paste_resume_text_checkbox"):
        resume_text_input = st.text_area("Or paste  resume text here (overrides file upload)", height=250, key="resume_text_area")

    
    if resume_text_input:
        resume_content_to_send = resume_text_input
        st.write("Using pasted text for resume analysis.")
    elif resume_file:
        file_bytes = resume_file.read()
        if resume_file.type == "application/pdf":
            resume_content_to_send = extract_text_from_pdf(file_bytes)
            if resume_content_to_send:
                st.success("PDF resume text extracted successfully!")
            else:
                st.error("Failed to extract text from PDF resume. Please try pasting text or another file.")
        elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_content_to_send = extract_text_from_docx(file_bytes)
            if resume_content_to_send:
                st.success("Word (DOCX) resume text extracted successfully!")
            else:
                st.error("Failed to extract text from DOCX resume. Please try pasting text or another file.")
        else:
            resume_content_to_send = file_bytes.decode('utf-8')
            st.info("Using uploaded file content directly (assumed text).")
        st.write("Using uploaded file (converted to text) for resume analysis.")
    else:
        st.warning("Please upload a resume file or paste resume text.")

    # --- Job Description Upload Section ---
    st.header("Upload Job Description")
    jd_content_to_send = "" 
    jd_text_input = ""
    jd_file = st.file_uploader("Choose a PDF or Word file for Job Description", type=["pdf", "docx"], key="jd_upload", accept_multiple_files=False)
    if st.checkbox("You can also paste job description text below if you prefer not to upload a file.", value=False, key="paste_jd_text_checkbox"):
        jd_text_input = st.text_area("Or paste job description text here (overrides file upload)", height=200, key="jd_text_area")

    
    if jd_text_input:
        jd_content_to_send = jd_text_input
        st.write("Using pasted text for job description.")
    elif jd_file:
        file_bytes = jd_file.read()
        if jd_file.type == "application/pdf":
            jd_content_to_send = extract_text_from_pdf(file_bytes)
            if jd_content_to_send:
                st.success("PDF job description text extracted successfully!")
            else:
                st.error("Failed to extract text from PDF job description. Please try pasting text or another file.")
        elif jd_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            jd_content_to_send = extract_text_from_docx(file_bytes)
            if jd_content_to_send:
                st.success("Word (DOCX) job description text extracted successfully!")
            else:
                st.error("Failed to extract text from DOCX job description. Please try pasting text or another file.")
        else:
            jd_content_to_send = file_bytes.decode('utf-8')
            st.info("Using uploaded file content directly (assumed text).")
        st.write("Using uploaded file (converted to text) for job description.")
    else:
        st.warning("Please upload a job description file or paste job description text.")

    # --- Analyze Button ---
    if st.button("Analyze", type="primary"):
        if not (resume_content_to_send and jd_content_to_send):
            st.error("Please provide both resume and job description before analyzing.")
        else:
            with st.spinner("Analyzing your resume... This may take a moment."):
                response = requests.post(GCP_FUNCTION_URL, json={"resume": resume_content_to_send, "job_description": jd_content_to_send})
                st.write(response.status_code)
                if response.status_code == 200:
                    analysis = response.json().get("analysis", "No analysis returned.")
                    st.write(analysis)
                else:
                    error_message = response.json().get("error", "An error occurred.")
                    st.error(f"Error: {error_message}")
                st.write("Analysis complete. Check the output above.", response.status_code)
    
    # --- Feedback Section ---
    st.markdown("<hr style='border:1px solid #BBDEFB;'>", unsafe_allow_html=True)
    st.header("Provide Feedback (If Necessary)")
    st.markdown("<p style='color:#34495E;'>Your feedback helps us improve! Please share your thoughts below.</p>", unsafe_allow_html=True)

    feedback_text = st.text_area("What are your thoughts or suggestions?", height=150, key="feedback_text_area")

    if st.button("Submit Feedback", type="secondary"):
        if feedback_text:
            with st.spinner("Transmitting feedback..."):
                try:
                    # Construct payload for the backend
                    payload = {
                        "feedback": feedback_text,
                        "email": st.user.email ,#st.session_state.get(, "anonymous_user") ,# Pass username if available
                        "jobdes":jd_content_to_send,
                        "resume":resume_content_to_send
                    }
                    feedback_response = requests.post(FEEDBACK_BACKEND_URL, json=payload)
                    
                    if feedback_response.status_code == 200:
                        st.success("Thank you for your valuable feedback! We appreciate it.")
                        # Optionally clear feedback text area by re-rendering
                        #st.session_state["feedback_text_area"] = "" 
                    else:
                        st.error(f"Feedback submission failed: {feedback_response.status_code} - {feedback_response.text}. Investigate network or service status.")
                except requests.exceptions.RequestException as e:
                    st.error(f"Network error during feedback submission: {e}. Verify connectivity.")
        else:
            st.warning("Feedback field cannot be empty. Provide relevant information.")

    st.markdown("<p style='text-align: center; color:#7F8C8D;'>End of operational interface.</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border:1px solid #BBDEFB;'>", unsafe_allow_html=True)
