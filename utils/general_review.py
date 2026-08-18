import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)


def generate_general_review(resume_text):

    prompt = f"""
You are an experienced ATS Resume Reviewer.

Analyze ONLY the resume below.

Resume:
{resume_text}

Evaluate the following:

1. ATS Compatibility (Score out of 100)
2. Resume Strengths
3. Weaknesses
4. Missing Sections (if any)
5. Resume Improvement Tips
6. Final Verdict


Return ONLY a valid JSON object.

Format:

{{
  
  "scores": {{
    "Resume Structure": 20,
    "Skills": 20,
    "Experience": 20,
    "Education": 10,
    "Projects": 20,
    "ATS Keywords": 5,
    "Formatting": 5
  }},


  "strengths": [
    "...",
    "...",
    "..."
  ],

  "weaknesses": [
    "...",
    "...",
    "..."
  ],

  "missing_sections": [
    "...",
    "..."
  ],

  "suggestions": [
    "...",
    "...",
    "..."
  ],

  "final_verdict": "..."
}}

Rules:

- Scores must be integers.
- Resume Structure: 0-20
- Skills: 0-20
- Experience: 0-20
- Education: 0-10
- Projects: 0-20
- ATS Keywords: 0-5
- Formatting: 0-5

The total score must not exceed 100.

Return JSON only.
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
            temperature=0.3,
            max_tokens=1500
        )

        content = response.choices[0].message.content
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()
        print("\n========== RAW MODEL RESPONSE ==========\n")
        print(content)
        print("\n========================================\n")
        review = json.loads(content) 
        return review

    except Exception as e:

      print(e)

      return {
        "scores": {
            "Resume Structure": 0,
            "Skills": 0,
            "Experience": 0,
            "Education": 0,
            "Projects": 0,
            "ATS Keywords": 0,
            "Formatting": 0
        },
        "strengths": [],
        "weaknesses": [],
        "missing_sections": [],
        "suggestions": [f"Error: {e}"],
        "final_verdict": "Unable to analyze the resume."
    }
