from fastapi import APIRouter

from app.schemas.hackathon_schema import HackathonCreate
from app.models.hackathon import Hackathon

from app.services.hackathon_service import (
    create_hackathon,
    get_all_hackathons
)

router = APIRouter()


@router.post("/create")
async def create(data: HackathonCreate):

    hackathon = Hackathon(
        **data.model_dump()
    )

    return await create_hackathon(hackathon)


@router.get("/all")
async def all_hackathons():

    return await get_all_hackathons()