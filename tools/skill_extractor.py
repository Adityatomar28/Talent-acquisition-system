import ollama


def extract_skills(resume_text):

    prompt = f"""
Extract ONLY the technical skills from this resume.

Rules:
- Return ONLY a comma separated list
- Do NOT write sentences
- Do NOT add explanations

Example output:
Python, TensorFlow, React, AWS

Resume:
{resume_text}
"""

    response = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": prompt}]
)

    skills_text = response["message"]["content"]

    skills = [s.strip() for s in skills_text.split(",")]

    return skills