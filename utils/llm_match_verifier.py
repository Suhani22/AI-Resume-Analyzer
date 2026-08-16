import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def verify_match(job_skill, resume_skill):
    prompt = f"""
You are an expert in professional skills, technologies, certifications, software tools, frameworks, programming languages, and job competencies.

Determine whether the following two skills should be considered the SAME skill for resume-job matching.

Skill 1:
{job_skill}

Skill 2:
{resume_skill}

Rules:

- Consider abbreviations.
- Consider full forms.
- Consider industry-standard synonyms.
- Consider commonly accepted equivalent names.
- Only answer YES if they represent the same competency.
- Otherwise answer NO.

Return ONLY one word.

YES

or

NO
"""

    try:
        response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=5
    )

        answer = response.choices[0].message.content.strip().upper()
        return answer == "YES"

    except Exception as e:
        print(e)
        return False