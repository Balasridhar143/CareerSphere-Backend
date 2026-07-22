from pydantic import BaseModel, EmailStr
from typing import Optional


class CompanyCreate(BaseModel):

    company_name: str

    email: EmailStr

    industry: str

    website: Optional[str] = None

    description: Optional[str] = None

    location: Optional[str] = None

    company_size: Optional[str] = None

    founded_year: Optional[int] = None