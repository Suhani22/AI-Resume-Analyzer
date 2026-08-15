from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')
def semantic_match(resume_skills, job_skills):
    matched = []

    resume_embeddings= model.encode(resume_skills, convert_to_tensor=True)
    job_embeddings = model.encode(job_skills, convert_to_tensor=True)

    for i, job_skill in enumerate(job_skills):
        best_score=0
        best_resume_skill = None
        for j, resume_skill in enumerate(resume_skills):
            score = util.cos_sim(job_embeddings[i], resume_embeddings[j]).item()
            if score > best_score:
                best_score = score
                best_resume_skill = resume_skill
        if best_score >= 0.75:
            matched.append({
                "job_skill": job_skill,
                "resume_skill": best_resume_skill,
                "similarity": round(best_score, 2)
         })

    return matched