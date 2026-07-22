from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Hackathon(BaseModel):
    title: str
    organizer: str
    location: str
    mode: str
    prize_pool: Optional[str] = None
    registration_deadline: str
    event_date: str
    skills: List[str]
    description: str
    created_at: datetime = datetime.utcnow()