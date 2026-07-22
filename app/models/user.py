from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime


class User(BaseModel):

    full_name: str

    email: EmailStr

    password: str

    role: str = "student"

    college: Optional[str] = None

    department: Optional[str] = None

    cgpa: Optional[float] = None

    skills: List[str] = []

    certifications: List[str] = []

    projects: List[str] = []

    resume_url: Optional[str] = None

    profile_picture: Optional[str] = None

    resume_score: int = 0

    ai_score: int = 0

    saved_jobs: List[str] = []

    applied_jobs: List[str] = []

    notifications: List[str] = []

    is_active: bool = True

    created_at: datetime = Field(default_factory=datetime.utcnow)