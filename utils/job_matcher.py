from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_resume_to_job(resume_text, job_desc_text):
    embeddings = model.encode([resume_text, job_desc_text])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(similarity * 100, 2)
