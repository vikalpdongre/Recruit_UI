import streamlit as st
import requests
import base64 # Still useful if we want to send files, but text extraction now happens upfront
import io # Needed for handling file-like objects

# Libraries for PDF and DOCX parsing in the frontend
try:
    import pypdf # For PDF parsing
except ImportError:
    st.error("Please install pypdf: pip install pypdf")
    pypdf = None

try:
    from docx import Document # For DOCX parsing
except ImportError:
    st.error("Please install python-docx: pip install python-docx")
    Document = None


# Streamlit app to analyze resumes using a GCP function
# IMPORTANT: Your GCP function at this URL will now primarily receive plain text,
# as file parsing (PDF/DOCX) is handled in the frontend.
GCP_FUNCTION_URL = 'https://agent-ops-911008082076.us-east1.run.app/analyze'

st.set_page_config(layout="centered", page_title="Advanced Resume Analyzer")

st.title("📄 Advanced Resume & Job Description Analyzer")
st.markdown("Upload your resume and a job description to get an instant analysis!")

# --- Helper function to extract text from PDF ---
def extract_text_from_pdf(file_bytes):
    """Extracts text from a PDF file."""
    if pypdf is None:
        st.error("pypdf library not found. Cannot process PDF files.")
        return None
    try:
        reader = pypdf.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or "" # Handle potential None from extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

# --- Helper function to extract text from DOCX ---
def extract_text_from_docx(file_bytes):
    """Extracts text from a DOCX file."""
    if Document is None:
        st.error("python-docx library not found. Cannot process DOCX files.")
        return None
    try:
        doc = Document(io.BytesIO(file_bytes))
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading DOCX file: {e}")
        return None

# --- Resume Upload Section ---
st.header("Upload Your Resume")
resume_file = st.file_uploader("Choose a PDF or Word file for your Resume", type=["pdf", "docx"], key="resume_upload")
resume_text_input = st.text_area("Or paste your resume text here (overrides file upload)", height=250, key="resume_text_area")

resume_content_to_send = ""
if resume_text_input: # Pasted text takes precedence
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
        # Fallback for unexpected file types if any
        resume_content_to_send = file_bytes.decode('utf-8')
        st.info("Using uploaded file content directly (assumed text).")
    st.write("Using uploaded file (converted to text) for resume analysis.")
else:
    st.warning("Please upload a resume file or paste resume text.")

# --- Job Description Upload Section ---
st.header("Upload Job Description")
jd_file = st.file_uploader("Choose a PDF or Word file for Job Description", type=["pdf", "docx"], key="jd_upload")
jd_text_input = st.text_area("Or paste job description text here (overrides file upload)", height=200, key="jd_text_area")

jd_content_to_send = ""
if jd_text_input: # Pasted text takes precedence
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
        # Fallback for unexpected file types if any
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


