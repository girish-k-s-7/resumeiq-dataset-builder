from pydantic import BaseModel


class Experience(BaseModel):
    company: str
    role: str
    duration: str
    location: str
    description: str