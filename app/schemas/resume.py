from uuid import uuid4

from pydantic import BaseModel, Field

from app.schemas.achievement import Achievement
from app.schemas.candidate import Candidate
from app.schemas.certification import Certification
from app.schemas.education import Education
from app.schemas.experience import Experience
from app.schemas.project import Project
from app.schemas.publication import Publication


class Resume(BaseModel):
    resume_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    candidate: Candidate

    summary: str

    skills: list[str]

    education: list[Education]

    experience: list[Experience]

    projects: list[Project]

    certifications: list[Certification] = []

    achievements: list[Achievement] = []

    publications: list[Publication] = []

    languages: list[str] = []

    interests: list[str] = []

    additional_sections: list[str] = []

    template: str = "classic"

    consent: bool = False