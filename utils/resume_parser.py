import re
import docx2txt
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_skills(text):
    skills = ['python', 'java', 'sql', 'machine learning', 'deep learning', 'nlp',
              'data analysis', 'communication', 'tensorflow', 'flask']
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return list(set(found_skills))

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
