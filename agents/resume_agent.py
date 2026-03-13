from tools.resume_parser import extract_text
from tools.skill_extractor import extract_skills
from tools.embeddings import match_score
from tools.skill_matcher import match_skills

class ResumeAgent:

    def analyze(self, resume_path, job_description, job_skills):

        text = extract_text(resume_path)

        skills_text = extract_skills(text)

        candidate_skills = [s.strip() for s in skills_text]

        skill_analysis = match_skills(candidate_skills, job_skills)

        score = match_score(text, job_description)

        return {
            "candidate_skills": candidate_skills,
            "skill_analysis": skill_analysis,
            "semantic_score": score
        }