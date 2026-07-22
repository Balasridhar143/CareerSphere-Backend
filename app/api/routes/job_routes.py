from fastapi import APIRouter

from app.schemas.job_schema import JobCreate
from app.models.job import Job
from app.services.job_service import (
    create_job,
    get_all_jobs
)

router = APIRouter()


@router.post("/create")
async def create(job: JobCreate):

    data = Job(**job.model_dump())

    return await create_job(data)


@router.get("/all")
async def all_jobs():

    return await get_all_jobs()