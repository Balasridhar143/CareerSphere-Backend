from pydantic import BaseModel


class ResumeResponse(BaseModel):
    success: bool
    message: str