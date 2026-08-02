SKILLS = [
    # Languages
    "Python", "Java", "C", "C++", "C#",

    # Web
    "HTML", "CSS", "JavaScript", "TypeScript",
    "React", "Angular", "Vue", "Node.js",

    # Backend
    "Flask", "Django", "Spring Boot", "Express",

    # Databases
    "SQL", "MySQL", "PostgreSQL", "MongoDB",

    # AI
    "Machine Learning", "Deep Learning",
    "TensorFlow", "PyTorch", "Scikit-learn",
    "OpenCV", "Pandas", "NumPy",

    # Cloud
    "AWS", "Azure", "GCP",

    # DevOps
    "Docker", "Kubernetes",

    # Tools
    "Git", "GitHub", "VS Code",

    # APIs
    "REST API", "GraphQL"
]

def extract_skills(text):
    detected_skills = []
    for skill in SKILLS:
        if skill.lower() in text.lower():
            detected_skills.append(skill)
            
    return detected_skills

def find_missing_skills(resume_skills, job_skills):

    missing=[]

    for skill in job_skills:

        if skill not in resume_skills:

            missing.append(skill)

    return missing



def find_matching_skills(resume_skills, job_skills):

    matching = []

    for skill in job_skills:

        if skill in resume_skills:

            matching.append(skill)

    return matching
