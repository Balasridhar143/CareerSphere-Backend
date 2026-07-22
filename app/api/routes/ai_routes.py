import os

from fastapi import APIRouter, UploadFile, File

from app.ai.parser.resume_parser import extract_resume_text
from app.ai.analysis.resume_analyzer import analyze_resume
from app.ai.analysis.skill_gap import skill_gap_analysis
from app.ai.recommendation.recommendation_engine import recommend_jobs

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # Save uploaded resume
    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as f:
        f.write(await file.read())

    # Extract resume text
    resume_text = extract_resume_text(filepath)

    # Resume analysis
    resume_analysis = analyze_resume(resume_text)

    # Job recommendations
    recommendations = recommend_jobs(resume_text)

    # Default values
    job_text = ""

    # Get first recommended job details safely
    if recommendations and len(recommendations) > 0:

        first_job = recommendations[0]

        details = first_job.get("details", {})

        job_text = (
            details.get("title", "") + " " +
            details.get("company", "") + " " +
            details.get("location", "") + " " +
            details.get("job_type", "")
        )

    # Skill Gap Analysis
    skill_gap = skill_gap_analysis(
        resume_text,
        job_text
    )

    return {
        "filename": file.filename,
        "resume_score": resume_analysis["resume_score"],
        "suggestions": resume_analysis["suggestions"],
        "recommended_jobs": recommendations,
        "skill_gap": skill_gap
    }