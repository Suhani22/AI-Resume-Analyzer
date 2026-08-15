def calculate_match(matched_count, total_job_skills):

    if total_job_skills == 0:
        return 0

    return round((matched_count / total_job_skills) * 100, 1)