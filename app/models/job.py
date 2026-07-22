from pydantic import BaseModel
from typing import List


class Job(BaseModel):

    title: str

    company: str

    location: str

    salary: str

    skills: List[str]

    description: str

    deadline: str