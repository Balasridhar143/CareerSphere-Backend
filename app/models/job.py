from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Job(BaseModel):
    title: str
    company_name: str
    location: str
    salary: Optional[str] = None
    experience: Optional[str] = None
    job_type: str
    skills: List[str]
    description: str
    created_at: datetime = datetime.utcnow()