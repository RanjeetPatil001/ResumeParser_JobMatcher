import streamlit as st
import os
import requests
from utils.resume_parser import extract_text_from_pdf, extract_text_from_docx, extract_skills, clean_text
from utils.job_matcher import match_resume_to_job

st.set_page_config(page_title="Resume Parser", layout="wide")

# --------------------------- Styling with CSS ---------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        background-color: lightblue;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: left;
        animation: slideIn 1s ease-out;
        color: black;
    }

    .subtitle {
        font-size: 1.2rem;
        color: #963e4a;
        margin-bottom: 2rem;
    }

    @keyframes slideIn {
      0% { transform: translateX(-50px); opacity: 0; }
      100% { transform: translateX(0); opacity: 1; }
    }

    .banner {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        padding: 2rem;
        margin-top: 2rem;
    }

    .left {
        flex: 2;
    }

    .right img {
        max-height: 200px;
    }

    .stButton > button {
        background-color: #0984e3;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6em 2em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --------------------------- Animated Header ---------------------------
st.markdown("""
<div class='banner'>
    <div class='left'>
        <div class='main-title'>🚀 Revolutionize Your Recruitment<br>with Next-Gen Resume Parsing</div>
        <div class='subtitle'>Unlock the potential of every application with our advanced resume parser, designed to enhance the speed and accuracy of your hiring decisions.</div>
    </div>
    <div class='right'>
        <img src='https://cdn-icons-png.flaticon.com/512/6165/6165722.png' />
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------- Upload Inputs ---------------------------
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    uploaded_resume = st.file_uploader("📄 Upload Resume (.pdf or .docx)", type=["pdf", "docx"])
    if uploaded_resume:
        st.success("✅ Resume uploaded!")

with col2:
    uploaded_jd = st.text_area("📝 Paste Job Description", height=250)
    if uploaded_jd:
        st.success("✅ Job description received!")

# --------------------------- Process & Match ---------------------------
if st.button("🔍 Match Resume to Job"):
    if uploaded_resume and uploaded_jd:
        # Resume Text Extraction
        if uploaded_resume.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_resume)
        else:
            with open("temp.docx", "wb") as f:
                f.write(uploaded_resume.read())
            resume_text = extract_text_from_docx("temp.docx")
            os.remove("temp.docx")

        resume_text = clean_text(resume_text)
        jd_text = clean_text(uploaded_jd)

        # Skill Extraction and Matching
        skills = extract_skills(resume_text)
        score = match_resume_to_job(resume_text, jd_text)

        # Display Output
        st.markdown("## ✅ Match Result")
        st.metric("Match Score", f"{score} %")

        st.subheader("🛠️ Extracted Skills:")
        st.success(", ".join(skills) if skills else "No skills found")
    else:
        st.warning("⚠️ Please upload resume and paste job description.")
