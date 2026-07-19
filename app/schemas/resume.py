from pydantic import BaseModel

from app.schemas.candidate import Candidate
from app.schemas.education import Education
from app.schemas.experience import Experience
from app.schemas.project import Project
from uuid import uuid4
from pydantic import Field

class Resume(BaseModel):
    resume_id: str = Field(default_factory=lambda:str(uuid4()))

    candidate: Candidate

    summary: str
    
    skills: list[str]

    experience: list[Experience]

    projects: list[Project]

    education: list[Education]

    certifications: list[str] = []

    achievements: list[str] = []
    
    publications: list[str] = []

    languages: list[str] = []

    interests: list[str] = []

    additional_sections: list[str] = []

    template: str = "classic"

    consent: bool = False