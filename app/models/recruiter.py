from pydantic import BaseModel, EmailStr
from typing import Optional


class Recruiter(BaseModel):
    full_name: str
    email: EmailStr
    password: str

    company_name: str
    designation: str

    phone: Optional[str] = None

    role: str = "recruiter"