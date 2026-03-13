import ollama


class PreScreeningAgent:

    def generate_questions(self, role):

        prompt = f"""
        Generate 3 interview questions for a {role}.
        Focus on experience and technical knowledge.
        """

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]


    def evaluate_answer(self, question, answer):

        prompt = f"""
        Evaluate this interview answer.

        Question: {question}
        Answer: {answer}

        Give:
        - Score out of 10
        - Short feedback
        """

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]