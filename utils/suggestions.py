import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def generate_suggestions(
    resume_text,
    job_description,
    detected_skills,
    missing_skills
):
    prompt = f"""
    You are an expert ATS Resume Reviewer and technical recruiter.
    Your goal is to help candidates improve their resumes for software engineering internships and jobs.
    Resume:{resume_text}
    Job Description: {job_description}

    Detected_skills:{", ".join(detected_skills)}

    Missing skills: {", ".join(missing_skills)}

    Respond in the following format:

    ## Resume Strengths
    - Mention 3 strengths.

    ## Areas for Improvement
    - Mention 3 weaknesses.

    ## ATS Score Improvement Tips
    - Suggest concrete improvements to increase ATS score.

    ## Recommended Projects
    - Suggest 2 portfolio projects based on the missing skills.

    Keep the response under 250 words.
    Use bullet points.
    Be specific and actionable.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt)
        return response.text

    except Exception as e:
        return """
        ## AI Feedback

        The AI service is temporarily unavailable.

        Your resume has still been analyzed successfully.
        Please try again in a few minutes.
        """
