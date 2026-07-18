from pydantic import BaseModel, EmailStr

class Candidate(BaseModel):

    name: str

    title: str | None = None

    email: EmailStr

    phone: str

    github: str | None = None

    linkedin: str | None = None

    location: str | None = None