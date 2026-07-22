from fastapi import APIRouter

from app.schemas.internship_schema import InternshipCreate
from app.models.internship import Internship

from app.services.internship_service import (
    create_internship,
    get_all_internships
)

router = APIRouter()


@router.post("/create")
async def create(data: InternshipCreate):

    internship = Internship(
        **data.model_dump()
    )

    return await create_internship(internship)


@router.get("/all")
async def all_internships():

    return await get_all_internships()