from utils.skill_matcher import (
    find_matching_skills,
    find_missing_skills
)
from utils.llm_match_verifier import verify_matches_with_llm

def semantic_match(resume_skills, job_skills):
    """
    Returns:
    {
        "matched": [...],
        "missing": [...]
    }
    """

    matched = find_matching_skills(
    resume_skills,
    job_skills
)

    missing = find_missing_skills(
    resume_skills,
    job_skills
)
    # --------------------------
    # Remaining skills
    # --------------------------

    remaining_resume = [
    skill
    for skill in resume_skills
    if skill not in matched
]

    remaining_job = missing  # Already computed missing skills

    print("\nRemaining Resume Skills:", remaining_resume)
    print("Remaining Job Skills:", remaining_job)

    # --------------------------
    # LLM verification
    # --------------------------

    llm_matches = verify_matches_with_llm(
        remaining_resume,
        remaining_job
    )

    print("\nLLM Matches:", llm_matches)
    for item in llm_matches:

        if item["job"] not in matched:
           matched.append(item["job"])

        if item["job"] in missing:
           missing.remove(item["job"])

    print("\nFinal Matched:", matched)
    print("Final Missing:", missing)

    matched = list(dict.fromkeys(matched))
    missing = list(dict.fromkeys(missing))

    return {
        "matched": matched,
        "missing": missing
    }