def calculate_match(resume_skills, job_skills):

    if len(job_skills)==0:
        return 0
    
    matched=0
    for skill in job_skills:
        if skill in resume_skills:
            matched+=1

    match_percentage = (matched / len(job_skills)) * 100
    return  round(match_percentage,1)