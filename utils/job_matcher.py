def calculate_match(matching_skills, job_skills):

    matched = len(matching_skills)

    match_percentage = (matched / len(job_skills)) * 100

    return round(match_percentage, 1)