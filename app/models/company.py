from pydantic import BaseModel
from typing import Optional


class Company(BaseModel):

    company_name: str

    email: str

    industry: str

    website: Optional[str] = None

    description: Optional[str] = None