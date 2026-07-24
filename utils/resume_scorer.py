def calculate_score(detected_skills, total_skills):
    score= (len(detected_skills) / total_skills) * 100
    return round(score)