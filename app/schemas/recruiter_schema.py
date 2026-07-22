from pydantic import BaseModel, EmailStr
from typing import Optional


class RecruiterSignup(BaseModel):
    full_name: str
    email: EmailStr
    password: str

    company_name: str
    designation: str

    phone: Optional[str] = None


class RecruiterLogin(BaseModel):
    email: EmailStr
    password: str