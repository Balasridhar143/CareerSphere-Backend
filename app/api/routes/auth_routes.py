from fastapi import APIRouter

from app.schemas.auth_schema import StudentSignup
from app.models.user import User
from app.schemas.auth_schema import Login
from app.services.auth_service import login_user
from app.services.auth_service import register_student

router = APIRouter()


@router.post("/signup/student")
async def signup_student(
    student: StudentSignup
):

    user = User(
        full_name=student.full_name,
        email=student.email,
        password=student.password,
        college=student.college,
        department=student.department,
        cgpa=student.cgpa,
        role="student"
    )

    return await register_student(
        user
    )
@router.post("/login")
async def login(login: Login):

    return await login_user(
        login.email,
        login.password
    )