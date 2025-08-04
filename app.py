import streamlit as st
import os
from pathlib import Path

# Simulate GPT logic (replace with real API call if needed)
def generate_suggestions(job, resume):
    return f"""Suggested Improvements:
- Add skills related to: {job}
- Clarify experience with tools mentioned
- Improve alignment with job keywords
- Keep tone professional and focused"""

# Streamlit UI
st.set_page_config(page_title="AI Resume Optimizer", layout="centered")
st.title("📝 AI Resume Optimizer")
st.write("Upload a resume and job description to get suggestions.")

job_description = st.text_area("Job Description", height=150)
import os
import PyPDF2
import docx

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
resume_text = ""

if uploaded_file:
    file_ext = os.path.splitext(uploaded_file.name)[1].lower()

    if file_ext == ".pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            resume_text += page.extract_text()

    elif file_ext == ".docx":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            resume_text += para.text + "\n"

if st.button("Analyze"):
    if job_description and resume_text:
        response = generate_suggestions(job_description, resume_text)
        st.success("✅ Analysis Complete!")
        st.code(response)
    else:
        st.warning("Please fill in both fields.")
