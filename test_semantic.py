from utils.semantic_matcher import semantic_match

resume_skills = [
    "Amazon Web Services",
    "Machine Learning",
    "REST API",
    "Python",
    "GitHub",
    "TensorFlow"
]

job_skills = [
    "AWS",
    "ML",
    "REST APIs",
    "Python",
    "Git",
    "TensorFlow"
]

matched = semantic_match(resume_skills, job_skills)

print("\n========== Matched Skills ==========\n")

for item in matched:
    print(item)