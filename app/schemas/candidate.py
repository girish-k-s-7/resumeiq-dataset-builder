from pydantic import BaseModel, EmailStr

class Candidate(BaseModel):
    candidate_id: str
    name: str
    title: str

    email: EmailStr
    phone: str

    github: str
    linkedin: str

    location: str