from fastapi import APIRouter

from app.schemas.recruiter_schema import RecruiterSignup
from app.schemas.recruiter_schema import RecruiterLogin

from app.models.recruiter import Recruiter

from app.services.recruiter_service import register_recruiter
from app.services.recruiter_service import login_recruiter

router = APIRouter()


@router.post("/signup/recruiter")
async def signup_recruiter(
    recruiter: RecruiterSignup
):

    data = Recruiter(
        **recruiter.model_dump()
    )

    return await register_recruiter(data)


@router.post("/login/recruiter")
async def recruiter_login(
    recruiter: RecruiterLogin
):

    return await login_recruiter(
        recruiter.email,
        recruiter.password
    )