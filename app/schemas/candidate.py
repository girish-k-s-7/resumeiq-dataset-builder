from pydantic import BaseModel, EmailStr


class Candidate(BaseModel):
    name: str

    title: str | None = None

    email: EmailStr | None = None

    phone: str | None = None

    linkedin: str | None = None

    github: str | None = None

    portfolio: str | None = None

    location: str | None = None