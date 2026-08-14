from utils.llm_skill_extractor import extract_skills_with_llm

sample = """
Digital Marketing Specialist

SEO

Google Ads

Meta Ads

Content Marketing

Email Marketing

Google Analytics

Canva

WordPress
"""

skills = extract_skills_with_llm(sample)

print(skills)