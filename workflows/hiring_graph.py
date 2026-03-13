from langgraph.graph import StateGraph
from typing import TypedDict

from agents.resume_agent import ResumeAgent
from agents.pre_screening_agent import PreScreeningAgent


class HiringState(TypedDict):
    resume_path: str
    job_description: str
    job_skills: list

    candidate_skills: list
    skill_match_score: float

    interview_score: float
    final_decision: str


resume_agent = ResumeAgent()
prescreen_agent = PreScreeningAgent()


def resume_screening_node(state):

    result = resume_agent.analyze(
        state["resume_path"],
        state["job_description"],
        state["job_skills"]
    )

    state["candidate_skills"] = result["candidate_skills"]
    state["skill_match_score"] = result["skill_analysis"]["skill_match_score"]

    return state


def interview_node(state):

    role = "Machine Learning Engineer"

    questions = prescreen_agent.generate_questions(role)

    print("\nInterview Questions:")
    print(questions)

    answer = input("\nCandidate answer: ")

    evaluation = prescreen_agent.evaluate_answer(questions, answer)

    print("\nInterview Evaluation:")
    print(evaluation)

    state["interview_score"] = 7  # placeholder

    return state


def decision_node(state):

    if state["skill_match_score"] > 0.6:
        state["final_decision"] = "Proceed to next round"
    else:
        state["final_decision"] = "Rejected"

    return state


graph = StateGraph(HiringState)

graph.add_node("resume_screening", resume_screening_node)
graph.add_node("interview", interview_node)
graph.add_node("decision", decision_node)

graph.set_entry_point("resume_screening")

graph.add_edge("resume_screening", "interview")
graph.add_edge("interview", "decision")

hiring_graph = graph.compile()