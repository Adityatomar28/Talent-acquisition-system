from agents.pre_screening_agent import PreScreeningAgent

agent = PreScreeningAgent()

role = "Machine Learning Engineer"

questions = agent.generate_questions(role)

print("Interview Questions:")
print(questions)

question = input("Enter a question to test: ")
answer = input("Candidate answer: ")

evaluation = agent.evaluate_answer(question, answer)

print("\nEvaluation:")
print(evaluation)