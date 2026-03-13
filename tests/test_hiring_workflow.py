from workflows.hiring_graph import hiring_graph


result = hiring_graph.invoke({

    "resume_path": "resume.pdf",

    "job_description": "Machine learning engineer with Python and AWS",

    "job_skills": ["Python", "TensorFlow", "AWS", "Machine Learning"]

})

print("\nFinal Result:")
print(result)

