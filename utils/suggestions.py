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
You are an experienced ATS Resume Reviewer.

Analyze the following resume.

Resume:
{resume_text}

Job Description:
{job_description}

Detected Skills:
{", ".join(detected_skills)}

Missing Skills:
{", ".join(missing_skills)}

Return the response EXACTLY in this Markdown format.

## 💪 Resume Strengths

- Strength 1
- Strength 2
- Strength 3

## ⚠️ Areas for Improvement

- Improvement 1
- Improvement 2
- Improvement 3

## 📈 ATS Improvement Tips

- Tip 1
- Tip 2
- Tip 3

## 🚀 Recommended Projects

- Project 1
- Project 2

Keep the response under 220 words.
Only return the markdown.
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
            max_tokens=500
        )

        print("\n========== SUGGESTIONS RESPONSE ==========\n")
        print(response)

        print("\n========== CONTENT ==========\n")
        print(repr(response.choices[0].message.content))

        print("\n========== REASONING ==========\n")
        print(response.choices[0].message.reasoning)

        print("\n========== FINISH REASON ==========\n")
        print(response.choices[0].finish_reason)

        return response.choices[0].message.content

    except Exception as e:
        print(e)

        return f"""
        ## AI Feedback

        Groq API Error

        {e}
        """
