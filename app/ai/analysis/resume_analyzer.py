import re


def analyze_resume(resume_text: str):

    score = 40
    suggestions = []

    # Skills
    if len(re.findall(r"\b(Python|Java|C\+\+|JavaScript|FastAPI|MongoDB|SQL|React|Docker|AWS)\b",
                      resume_text,
                      re.IGNORECASE)) >= 3:
        score += 20
    else:
        suggestions.append("Add more technical skills.")

    # Projects
    if "project" in resume_text.lower():
        score += 15
    else:
        suggestions.append("Include academic or personal projects.")

    # Education
    if "education" in resume_text.lower():
        score += 10
    else:
        suggestions.append("Add education details.")

    # Experience
    if "experience" in resume_text.lower():
        score += 10
    else:
        suggestions.append("Add internship or work experience.")

    # Certifications
    if "certificate" in resume_text.lower() or "certification" in resume_text.lower():
        score += 5
    else:
        suggestions.append("Add certifications.")

    score = min(score, 100)

    return {
        "resume_score": score,
        "suggestions": suggestions
    }