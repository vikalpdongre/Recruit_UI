# text_extraction.py
import io
import pypdf
from docx import Document
import streamlit as st

def extract_text_from_pdf(file_bytes):
    """Extracts text from a PDF file."""
    if pypdf is None:
        st.error("pypdf library not found. Cannot process PDF files.")
        return None
    try:
        reader = pypdf.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

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
