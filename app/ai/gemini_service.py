from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6JixGwL5_VwnzvYYeduR5RcJJG5e9GgD2wwB-pBtfifbA"
)


def analyze_resume(resume_text: str):

    prompt = f"""
You are an expert HR recruiter.

Analyze the following resume.

Resume:
{resume_text}

Return:

1. Candidate Summary
2. Technical Skills
3. Soft Skills
4. Strengths
5. Missing Skills
6. Suitable Job Roles
7. Resume Score out of 100
8. Suggestions for Improvement
"""

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)
    return response.text