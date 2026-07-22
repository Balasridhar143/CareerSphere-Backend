from pydantic import BaseModel, EmailStr


class StudentSignup(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    college: str
    department: str
    cgpa: float


class RecruiterSignup(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    company_name: str


class Login(BaseModel):
    email: EmailStr
    password: str