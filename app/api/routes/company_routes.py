from fastapi import APIRouter

from app.schemas.company_schema import CompanyCreate

from app.models.company import Company

from app.services.company_service import (
    create_company,
    get_all_companies
)

router = APIRouter()


@router.post("/create")
async def create(company: CompanyCreate):

    data = Company(
        **company.model_dump()
    )

    return await create_company(data)


@router.get("/all")
async def all_companies():

    return await get_all_companies()