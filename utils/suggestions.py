import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)

def generate_suggestions(
    resume_text,
    job_description,
    detected_skills,
    missing_skills
):
    prompt = f"""
You are an experienced ATS Resume Reviewer and Career Coach.

Analyze the following resume against the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Detected Skills:
{", ".join(detected_skills)}

Missing Skills:
{", ".join(missing_skills)}

Respond in this format:

## Resume Strengths
- Mention 3 strengths.

## Areas for Improvement
- Mention 3 weaknesses.

## ATS Score Improvement Tips
- Give practical ATS improvement suggestions.

## Recommended Projects
- Suggest 2 projects based on the missing skills.

Keep the response under 250 words.
Use bullet points.
Be specific and actionable.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        print(e)

        return f"""
        ## AI Feedback

        Groq API Error

        {e}
        """
