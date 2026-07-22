import os

from fastapi import APIRouter, UploadFile, File
from app.ai.parser.resume_parser import extract_resume_text
from app.ai.recommendation.recommendation_engine import recommend_jobs
router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    resume_text = extract_resume_text(filepath)

    return {
        "filename": file.filename,
        "text": resume_text[:500]
    }
@router.post("/recommend")
async def recommend(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    resume_text = extract_resume_text(filepath)

    recommendations = recommend_jobs(resume_text)

    return {
        "matches": recommendations
    }