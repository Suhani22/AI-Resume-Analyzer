from flask import Flask , render_template, request
from utils.pdf_reader import extract_text
from utils.skill_extractor import (extract_skills, SKILLS, find_missing_skills)
from utils.resume_scorer import calculate_score

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
    file_path= os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(file_path)
    text = extract_text(file_path)
    skills= extract_skills(text)
    matching_skills = extract_skills(text)
    score = calculate_score(skills, len(SKILLS))  
    print("Extracted Skills:", skills)
    print("Resume Score:", score)
    return render_template(
    "results.html",
    skills=skills,
    missing_skills=find_missing_skills(skills),
    score=score)

if __name__ == '__main__':
    app.run(debug=True)