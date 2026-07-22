from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Internship(BaseModel):
    title: str
    company_name: str
    location: str
    stipend: Optional[str] = None
    duration: str
    skills: List[str]
    description: str
    created_at: datetime = datetime.utcnow()