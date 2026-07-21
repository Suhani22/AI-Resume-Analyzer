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