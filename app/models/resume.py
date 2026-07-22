from pydantic import BaseModel
from datetime import datetime


class Resume(BaseModel):
    student_email: str
    filename: str
    filepath: str
    uploaded_at: datetime = datetime.utcnow()