from flask import Flask , render_template, request
from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills

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
    print("Extracted Skills:", skills)
    return render_template(
    "results.html",
    skills=skills)

if __name__ == '__main__':
    app.run(debug=True)