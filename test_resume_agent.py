from agents.resume_agent import ResumeAgent

print("Starting Resume Test...")

agent = ResumeAgent()

resume_path = "resume.pdf"
job_description = "Machine learning engineer with Python, TensorFlow and AWS"

job_skills = ["Python", "TensorFlow", "AWS", "Machine Learning"]


result = agent.analyze(resume_path, job_description,job_skills)

print("Result:")
print(result)

