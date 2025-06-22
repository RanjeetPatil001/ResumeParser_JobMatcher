🧠 Resume Parser & Job Matcher (NLP + Streamlit)
This project integrates a resume parser and job matcher built using Streamlit, SpaCy, and Scikit-learn, allowing users to upload a resume, paste a job description, and instantly see a match score based on AI-driven skill and text similarity analysis.

The code enables intelligent filtering of resumes using real-world NLP techniques in a clean, responsive web interface.

Features
Streamlit UI: Modern, animated frontend using HTML/CSS and responsive layout
Resume Parsing: Supports PDF and DOCX file types
Skill Extraction: Uses SpaCy NLP to pull out relevant candidate skills
Job Matching: Uses TF-IDF + cosine similarity to score resume against job description
Real-Time Results: Match score and skills displayed instantly
Deployable: Can be run locally or deployed on Streamlit Cloud

Prerequisites
1.Python 3.7+Streamlit
pip install streamlit

2.NLP Libraries
pip install spacy scikit-learn PyPDF2 python-docx
python -m spacy download en_core_web_sm

🚀 How to Use
Clone the repository or download the project files
Place your API-free code in app.py, resume_parser.py, and job_matcher.py
Run the app locally

streamlit run app.py
Open your browser

Usually: http://localhost:8501

Upload your resume and paste a job description

✅ See extracted skills and a match score!

🧾 Code Overview
app.py: Main Streamlit frontend with file uploader and results panel

resume_parser.py: Extracts and cleans text from resume files; pulls out skill keywords

job_matcher.py: Computes similarity between resume and job description using TF-IDF

requirements.txt: Includes all required Python libraries

📦 Project Structure
Resume_Parser_Job_Matcher_Project/
├── app.py
├── requirements.txt
├── README.md
└── utils/
    ├── resume_parser.py
    └── job_matcher.py

