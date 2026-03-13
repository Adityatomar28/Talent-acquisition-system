from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def match_score(resume, job_description):

    r = model.encode([resume])
    j = model.encode([job_description])

    score = cosine_similarity(r, j)

    return float(score[0][0])