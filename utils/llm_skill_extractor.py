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
        model="groq/compound-mini",
        messages=[{
            "role": "user",
            "content": prompt 
        }],

        temperature=0.0,
        max_tokens=500
    )
        print("\n========== FULL RESPONSE ==========\n")
        print(response)

        print("\n========== CHOICE ==========\n")
        print(response.choices[0])

        print("\n========== MESSAGE ==========\n")
        print(response.choices[0].message)

        print("\n========== FINISH REASON ==========\n")
        print(response.choices[0].finish_reason) 
        content = response.choices[0].message.content
        print("CONTENT:", repr(content))
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        print("\n========== LLM SKILL EXTRACTION ==========\n")
        print(content)
        print("\n=========================================\n")
 
        data=json.loads(content)
        return data.get("skills", [])

    except Exception as e:

        print(e)

        return []
