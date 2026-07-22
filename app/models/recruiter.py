from pydantic import BaseModel


class Recruiter(BaseModel):

    full_name: str

    email: str

    company_name: str

    password: str