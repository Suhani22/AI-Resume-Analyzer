SKILL_MAPPINGS = {
    # Cloud
    "aws": "amazon web services",
    "amazon web services": "amazon web services",

    # AI
    "ml": "machine learning",
    "machine learning": "machine learning",

    "ai": "artificial intelligence",
    "artificial intelligence": "artificial intelligence",

    "llm": "large language models",
    "large language models": "large language models",

    "rag": "retrieval augmented generation",
    "retrieval augmented generation": "retrieval augmented generation",

    # APIs
    "rest api": "rest api",
    "rest apis": "rest api",

    # Git
    "git": "git",
    "github": "git",

    # Adobe
    "photoshop cc": "adobe photoshop",
    "adobe photoshop": "adobe photoshop",

    # Medical
    "bls": "basic life support",
    "basic life support": "basic life support",
}

def normalize_skill(skill):
    skill = skill.strip().lower()
    return SKILL_MAPPINGS.get(skill, skill)

def find_matching_skills(resume_skills, job_skills):

    matching = []

    normalized_resume = {
        normalize_skill(skill): skill
        for skill in resume_skills
    }

    for job_skill in job_skills:

        normalized_job = normalize_skill(job_skill)

        if normalized_job in normalized_resume:

            matching.append(job_skill)

    return matching



def find_missing_skills(resume_skills, job_skills):

    missing = []

    normalized_resume = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    for job_skill in job_skills:

        if normalize_skill(job_skill) not in normalized_resume:

            missing.append(job_skill)

    return missing
