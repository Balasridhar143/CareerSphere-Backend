from pydantic import BaseModel
from typing import List, Optional


class InternshipCreate(BaseModel):
    title: str
    company_name: str
    location: str
    stipend: Optional[str] = None
    duration: str
    skills: List[str]
    description: str