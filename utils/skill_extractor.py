SKILLS = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "Flask",
    "Git",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
    "HTML",
    "CSS",
    "JavaScript"
]

def extract_skills(text):
    detected_skills = []
    for skill in SKILLS:
        if skill.lower() in text.lower():
            detected_skills.append(skill)
            
    return detected_skills

def find_missing_skills(detected_skills):
    missing_skills =[]
    for skill in SKILLS:
        if skill not in detected_skills:
            missing_skills.append(skill)

    return missing_skills

