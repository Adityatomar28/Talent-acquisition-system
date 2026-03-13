from typing import TypedDict, List

class HiringState(TypedDict):

    resume_text: str
    candidate_skills: List[str]

    job_description: str
    job_skills: List[str]

    skill_match_score: float
    interview_score: float
    assessment_score: float

    final_decision: str