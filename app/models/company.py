from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class Company(BaseModel):

    company_name: str

    email: EmailStr

    industry: str

    website: Optional[str] = None

    description: Optional[str] = None

    location: Optional[str] = None

    company_size: Optional[str] = None

    founded_year: Optional[int] = None

    created_at: datetime = datetime.utcnow()