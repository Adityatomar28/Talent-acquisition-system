def match_skills(candidate_skills, job_skills):

    candidate_set = set([s.strip().lower() for s in candidate_skills])
    job_set = set([s.strip().lower() for s in job_skills])

    matched = candidate_set.intersection(job_set)
    missing = job_set - candidate_set
    extra = candidate_set - job_set

    score = len(matched) / len(job_set) if job_set else 0

    return {
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "extra_skills": list(extra),
        "skill_match_score": score
    }
    