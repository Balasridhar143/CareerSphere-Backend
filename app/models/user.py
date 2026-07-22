from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):

    full_name: str

    email: EmailStr

    password: str

    role: str

    college: Optional[str] = None

    department: Optional[str] = None

    cgpa: Optional[float] = None

    created_at: datetime = datetime.utcnow()