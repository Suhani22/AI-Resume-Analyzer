import os
import json

from dotenv import load_dotenv

from groq import Groq

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))


def extract_skills_with_llm(text):
    prompt = f"""
You are an expert skill extraction system.

Extract every professional skill,
technology,
tool,
framework,
software,
programming language,
platform,
domain knowledge,
certification,
methodology,
or competency
explicitly mentioned in the following text.

Rules:

- Return ONLY valid JSON.
- Do NOT explain anything.
- Do NOT infer skills.
- Do NOT add skills that are not mentioned.
- Remove duplicate skills.
- Keep original names whenever possible.

Return in this format:

{{
    "skills": [
        "...",
        "...",
        "..."
    ]
}}

Text:

{text}
"""
    try:
        response= client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": prompt 
        }],

        temperature=0.0,
        max_tokens=500
    )

        content = response.choices[0].message.content.strip()
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        data=json.loads(content)
        return data.get("skills", [])

    except Exception as e:

        print(e)

        return []
