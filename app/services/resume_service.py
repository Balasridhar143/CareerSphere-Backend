import os
import shutil

from fastapi import UploadFile

from app.database.mongodb import mongodb


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


async def upload_resume(
    student_email: str,
    file: UploadFile
):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    database = mongodb.db

    await database.resumes.insert_one(
        {
            "student_email": student_email,
            "filename": file.filename,
            "filepath": filepath
        }
    )

    return {
        "success": True,
        "message": "Resume Uploaded Successfully."
    }
async def get_latest_resume():

    database = mongodb.db

    resume = await database.resumes.find_one(
        sort=[("_id", -1)]
    )

    return resume