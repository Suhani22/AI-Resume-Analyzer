from flask import Flask , render_template, request, send_file
from utils.pdf_reader import extract_text
from utils.job_match_engine import semantic_match    
from utils.llm_skill_extractor import extract_skills_with_llm
from utils.job_matcher import calculate_match
from utils.suggestions import generate_suggestions
from utils.pdf_generator import create_pdf
from utils.general_review import generate_general_review
import markdown
import os

app=Flask(__name__)         #application start

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok= True)
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    analysis_type = request.form["analysis_type"]      #general review or JD vs resume match

    resume = request.files["resume"]
    job_description = request.form["job_description"]

    file_path= os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(file_path)

    text = extract_text(file_path)

    if analysis_type == "general":

        review = generate_general_review(text)
        ats_score = sum(review["scores"].values())

        return render_template(
        "results.html",
        analysis_type="general",
        review=review,
        ats_score=ats_score
    )

    skills= extract_skills_with_llm(text)                           #resume skills
    job_skills= extract_skills_with_llm(job_description)            #job description skills

    #### from here 
    match_result = semantic_match(
       skills,
       job_skills
    )

    matching_skills = match_result["matched"]
    missing_skills = match_result["missing"]

    #### to here ---> replace hoga

    suggestions= generate_suggestions(text, job_description, skills, missing_skills)
    suggestions_html = markdown.markdown(suggestions)

    job_match = calculate_match( len(matching_skills),len(job_skills)) 


    #PDF report generation
    global report_data

    report_data = {
        "job_match": job_match,
        "skills": matching_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }

    #Results HTML page website pe bhej diii
    return render_template(
    "results.html",
    analysis_type="job",
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