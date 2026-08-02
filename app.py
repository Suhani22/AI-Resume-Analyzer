from flask import Flask , render_template, request, send_file
from utils.pdf_reader import extract_text
from utils.skill_extractor import (extract_skills, find_missing_skills, find_matching_skills)
from utils.job_matcher import calculate_match
from utils.suggestions import generate_suggestions
from utils.pdf_generator import create_pdf
import markdown
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

    skills= extract_skills(text)                           #resume skills
    job_skills= extract_skills(job_description)            #job description skills
    missing_skills= find_missing_skills(skills, job_skills)
    matching_skills = find_matching_skills(skills, job_skills)

    suggestions= generate_suggestions(text, job_description, skills, missing_skills)
    suggestions_html = markdown.markdown(suggestions)

    job_match = calculate_match(matching_skills, job_skills) 

    global report_data

    report_data = {
        "job_match": job_match,
        "skills": matching_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }
    return render_template(
    "results.html",
    skills=matching_skills,
    missing_skills=missing_skills,
    suggestions=suggestions_html,
    job_match=job_match    )

@app.route("/download")
def download_report():

    global report_data
    if "report_data" not in globals():
        return "Please analyze a resume first."
    filename = "Resume_Analysis_Report.pdf"

    create_pdf(
        filename,
        report_data["job_match"],
        report_data["skills"],
        report_data["missing_skills"],
        report_data["suggestions"]
    )

    return send_file(
        filename,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)