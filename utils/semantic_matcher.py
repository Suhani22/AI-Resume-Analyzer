from sentence_transformers import SentenceTransformer, util
from utils.llm_match_verifier import verify_match
model = SentenceTransformer('all-MiniLM-L6-v2')
def semantic_match(resume_skills, job_skills):
    matched = []
    missing = []

    used_resume_indices = set()

    resume_embeddings= model.encode(resume_skills, convert_to_tensor=True)
    job_embeddings = model.encode(job_skills, convert_to_tensor=True)

    for i, job_skill in enumerate(job_skills):
        best_score=0
        best_resume_skill = None
        best_index = None
        for j, resume_skill in enumerate(resume_skills):
            if j in used_resume_indices:
                continue
            score = util.cos_sim(job_embeddings[i], resume_embeddings[j]).item()
            if score > best_score:
                best_score = score
                best_resume_skill = resume_skill
                best_index = j
        HIGH_THRESHOLD = 0.90
        LOW_THRESHOLD = 0.60

        if best_score >= HIGH_THRESHOLD:

                matched.append({
        "job_skill": job_skill,
        "resume_skill": best_resume_skill,
        "similarity": round(best_score, 2)
        })

                used_resume_indices.add(best_index)
        elif best_score < LOW_THRESHOLD:

                missing.append(job_skill)

        else:

                

                print(
                    f"\n🤖 Verifying: {job_skill} ↔ {best_resume_skill} ({best_score:.2f})"
                     )

                if verify_match(job_skill, best_resume_skill):

                    matched.append({
                        "job_skill": job_skill,
                        "resume_skill": best_resume_skill,
                        "similarity": round(best_score, 2)
                    })

                    used_resume_indices.add(best_index)

                else:

                    missing.append(job_skill)

    return {
    "matched": matched,
    "missing": missing
}