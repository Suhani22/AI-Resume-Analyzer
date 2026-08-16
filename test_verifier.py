from utils.llm_match_verifier import verify_match

tests = [
    ("AWS", "Amazon Web Services"),
    ("ML", "Machine Learning"),
    ("REST APIs", "REST API"),
    ("Git", "GitHub"),
    ("Photoshop CC", "Adobe Photoshop"),
    ("BLS", "Basic Life Support"),
    ("Python", "Java")
]

for job_skill, resume_skill in tests:

    result = verify_match(
        job_skill,
        resume_skill
    )

    print(
        f"{job_skill} <-> {resume_skill} : {result}"
    )