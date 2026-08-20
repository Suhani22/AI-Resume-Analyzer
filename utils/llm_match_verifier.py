import json
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def verify_matches_with_llm(resume_skills, job_skills):

    if not resume_skills or not job_skills:
        return []

    prompt = f"""
You are an expert AI recruiter.

Compare the following Resume Skills and Job Skills.

Resume Skills:
{resume_skills}

Job Skills:
{job_skills}

Find only semantic matches.

Examples:

GitHub = Git
REST API = REST APIs
ML = Machine Learning
Amazon Web Services = AWS

Rules:

- Return ONLY valid JSON.
- Do not explain.
- Do not invent matches.
- Match only if they clearly represent the same skill or are closely related.

Return:

{{
    "matched":[
        {{
            "resume":"...",
            "job":"..."
            "confidence":0.96
        }}
    ]
}}
"""

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        content = response.choices[0].message.content.strip()

        content = content.replace("```json", "")
        content = content.replace("```", "").strip()

        data = json.loads(content)

        return data["matched"]

    except Exception as e:

        print(e)
        return []