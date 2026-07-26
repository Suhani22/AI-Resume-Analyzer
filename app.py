from flask import Flask , render_template, request
from utils.pdf_reader import extract_text
from utils.skill_extractor import (extract_skills, SKILLS, find_missing_skills)
from utils.resume_scorer import calculate_score
from utils.job_matcher import calculate_match
from utils.suggestions import generate_suggestions
import os

app=Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok= True)
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    resume = request.files["resume"]
    job_description = request.form["job_description"]

    file_path= os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(file_path)

    text = extract_text(file_path)

    skills= extract_skills(text)
    job_skills= extract_skills(job_description)
    missing_skills= find_missing_skills(skills)

    suggestions= generate_suggestions(missing_skills)

    score = calculate_score(skills, len(SKILLS)) 
    job_match = calculate_match(skills, job_skills) 

    print("Job match:", job_match)
   
    return render_template(
    "results.html",
    skills=skills,
    missing_skills=missing_skills,
    score=score,
    job_match=job_match,
    suggestions=suggestions
    )

if __name__ == '__main__':
    app.run(debug=True)