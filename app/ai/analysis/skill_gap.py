import re

SKILLS = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "React",
    "Node.js",
    "FastAPI",
    "MongoDB",
    "SQL",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "Git",
    "Machine Learning",
    "Deep Learning",
    "HTML",
    "CSS"
]


def extract_skills(text):
    found = []

    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):
            found.append(skill)

    return list(set(found))


def skill_gap_analysis(resume_text, job_text):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    missing = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    matched = [
        skill for skill in resume_skills
        if skill in job_skills
    ]

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing
    }