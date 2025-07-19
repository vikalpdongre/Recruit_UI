# analyzer_ui.py
import streamlit as st
import requests
from text_extraction import extract_text_from_pdf, extract_text_from_docx
import os
GCP_FUNCTION_URL = os.getenv('GCP_FUNCTION_URL_OPS')
FEEDBACK_BACKEND_URL = os.getenv('FEEDBACK_BACKEND_URL_OPS')

def main_analyzer_app():
    """Contains the main application functionality, accessible after login."""
    # Add a less welcoming header
    if "username" in st.session_state:
        st.header(f"Welcome, {st.session_state['username']}. Proceed as required. 😐")
    
    # Unfriendly title and intro
    st.title("Resume & Job Description Analysis Platform: Expedite Your Submission.")
    st.markdown("""
        <style>
        .stApp {
            background-color: #E0F2F7; /* Very light blue background */
            color: #2C3E50; /* Dark blue-grey text */
            font-family: 'Inter', sans-serif; /* Modern font */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #1A5276; /* Darker blue for headers */
        }
        .stButton>button {
            background-color: #3498DB; /* Professional blue button */
            color: white;
            border-radius: 8px;
            border: 1px solid #2874A6;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            transition: all 0.2s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #2874A6; /* Darker blue on hover */
            transform: translateY(-2px);
            box-shadow: 4px 4% 10px rgba(0,0,0,0.3);
        }
        .stFileUploader label, .stTextArea label, .stCheckbox label {
            color: #34495E; /* Slightly darker label */
        }
        .stSuccess {
            background-color: #D4EDDA; /* Light green-blue for success */
            color: #155724;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #C3E6CB;
        }
        .stError {
            background-color: #F8D7DA; /* Light red for error */
            color: #721C24;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #F5C6CB;
        }
        .stWarning {
            background-color: #FFF3CD; /* Light yellow for warning */
            color: #856404;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #FFEBA8;
        }
        .stInfo {
            background-color: #D1ECF1; /* Light blue for info */
            color: #0C5460;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #BEE5EB;
        }
        </style>
        <p style="color:#34495E;">Submit your documentation. Promptly.</p>
    """, unsafe_allow_html=True)

    # --- Resume Upload Section ---
    st.header("Resume Document Submission")
    resume_content_to_send = ""
    resume_text_input = ""  
    
    # Use columns for a slightly less conventional layout
    col1, col2 = st.columns([1, 1])

    with col1:
        resume_file = st.file_uploader("Upload your resume file (PDF/Word).", type=["pdf", "docx"], key="resume_upload", accept_multiple_files=False)
    
    with col2:
        # Checkbox for pasting text, with a hint of disdain
        if st.checkbox("Alternatively, provide textual input directly.", value=False, key="paste_resume_text_checkbox"):
            resume_text_input = st.text_area("Paste resume text here (this input supersedes file upload).", height=250, key="resume_text_area")

    if resume_text_input:
        resume_content_to_send = resume_text_input
        st.info("Textual resume input received for analysis. Ensure accuracy.")
    elif resume_file:
        file_bytes = resume_file.read()
        if resume_file.type == "application/pdf":
            resume_content_to_send = extract_text_from_pdf(file_bytes)
            if resume_content_to_send:
                st.success("PDF text extraction complete. Proceeding.")
            else:
                st.error("PDF text extraction failed. Verify document integrity or provide text directly.")
        elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_content_to_send = extract_text_from_docx(file_bytes)
            if resume_content_to_send:
                st.success("DOCX text extraction complete. Initiating next phase.")
            else:
                st.error("DOCX text extraction failed. Confirm file format or input text directly.")
        else:
            resume_content_to_send = file_bytes.decode('utf-8')
            st.info("Raw file content utilized. Assumed text format.")
        st.info("Resume document processed. Awaiting further input.")
    else:
        st.warning("Resume document not provided. Input is required for progression.")

    # --- Job Description Upload Section ---
    st.header("Job Description Document Submission")
    jd_content_to_send = "" 
    jd_text_input = ""

    col3, col4 = st.columns([1, 1])

    with col3:
        jd_file = st.file_uploader("Upload the job description file (PDF/Word).", type=["pdf", "docx"], key="jd_upload", accept_multiple_files=False)
    
    with col4:
        if st.checkbox("Alternatively, paste job description text below.", value=False, key="paste_jd_text_checkbox"):
            jd_text_input = st.text_area("Paste job description text here (this input supersedes file upload).", height=200, key="jd_text_area")

    if jd_text_input:
        jd_content_to_send = jd_text_input
        st.info("Textual job description input received.")
    elif jd_file:
        file_bytes = jd_file.read()
        if jd_file.type == "application/pdf":
            jd_content_to_send = extract_text_from_pdf(file_bytes)
            if jd_content_to_send:
                st.success("JD PDF text extraction complete. Data acquired.")
            else:
                st.error("JD PDF text extraction failed. Review file or provide text directly.")
        elif jd_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            jd_content_to_send = extract_text_from_docx(file_bytes)
            if jd_content_to_send:
                st.success("JD DOCX text extraction complete. Ready for processing.")
            else:
                st.error("JD DOCX text extraction failed. Confirm document validity or input text directly.")
        else:
            jd_content_to_send = file_bytes.decode('utf-8')
            st.info("Raw JD file content utilized. Assumed text format.")
        st.info("Job description document processed. Finalizing inputs.")
    else:
        st.warning("Job description document not provided. Analysis cannot proceed.")

    # --- Analyze Button ---
    st.markdown("<hr style='border:1px solid #BBDEFB;'>", unsafe_allow_html=True) # A subtle blue divider
    if st.button("Initiate Analysis (Mandatory)", type="primary"):
        if not (resume_content_to_send and jd_content_to_send):
            st.error("Both resume and job description inputs are prerequisite for analysis. Fulfill requirements.")
        else:
            with st.spinner("Executing analysis protocol... Stand by for results."):
                try:
                    response = requests.post(GCP_FUNCTION_URL, json={"resume": resume_content_to_send, "job_description": jd_content_to_send})
                    
                    if response.status_code == 200:
                        analysis = response.json().get("analysis", "Analysis returned no discernible data. Re-evaluate inputs.")
                        st.subheader("Analysis Output:")
                        st.markdown(f"<div style='background-color:#F0F8FF; padding:15px; border-radius:8px; border:1px solid #B0D9E8; color:#2C3E50;'>{analysis}</div>", unsafe_allow_html=True)
                        st.success("Analysis concluded. Review findings.")
                    else:
                        error_message = response.json().get("error", "An unhandled error occurred. Investigate system status.")
                        st.error(f"Error: {error_message}. Problem persists.")
                except requests.exceptions.RequestException as e:
                    st.error(f"Connectivity error or service unavailability: {e}. Verify network connection.")
    st.markdown("<hr style='border:1px solid #BBDEFB;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color:#7F8C8D;'>Analysis complete. No further action required from this interface.</p>", unsafe_allow_html=True)

    # --- Feedback Section ---
    st.markdown("<hr style='border:1px solid #BBDEFB;'>", unsafe_allow_html=True)
    st.header("Provide Feedback (If Necessary)")
    st.markdown("<p style='color:#6C757D;'>Your feedback helps us improve! Please share your thoughts below.</p>", unsafe_allow_html=True)

    feedback_text = st.text_area("What are your thoughts or suggestions?", height=150, key="feedback_text_area")
    if feedback_text:
        st.info("Feedback text captured. Ready for submission.")
    else:
        st.warning("Feedback field is empty. Input is required for submission.")
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
