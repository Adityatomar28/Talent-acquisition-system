🤖 AI Talent Acquisition System


An AI-powered multi-agent recruitment system that automates candidate evaluation using intelligent agents.

The system screens resumes, conducts AI interviews, assigns technical assessments, and generates hiring decisions automatically.

This project demonstrates how LLMs + Multi-Agent AI + Workflow orchestration can transform traditional recruitment process

🧠 AI Agents in the System

The system is built using specialized AI agents, each responsible for a specific stage in recruitment.

1️⃣ Resume Screening Agent

Extracts skills from candidate resumes

Compares them with job requirements

Computes a skill match score

2️⃣ Pre-Screen Interview Agent

Generates role-specific interview questions

Evaluates candidate responses using an LLM

3️⃣ Technical Assessment Agent

Generates technical tasks

Evaluates candidate solutions

4️⃣ Decision Agent

Combines signals from all agents to produce the final hiring decision.

🏗 System Architecture

                    Resume PDF
                        │
                        ▼
           +---------------------------+
           | Resume Screening Agent    |
           +-------------+-------------+
                         │
                         ▼
           +---------------------------+
           | Pre-Screen Interview Agent|
           +-------------+-------------+
                         │
                         ▼
           +---------------------------+
           | Technical Assessment Agent|
           +-------------+-------------+
                         │
                         ▼
                 +------------------+
                 | Decision Engine  |
                 +------------------+

⚙️ Tech Stack
AI / Machine Learning

LangGraph – Multi-agent workflow orchestration

Ollama / LLMs – Question generation and evaluation

Sentence Transformers – Semantic similarity

Scikit-learn – Cosine similarity scoring

Backend

Python

Tools

PyPDF (resume parsing)

Git / GitHub

VS Code
