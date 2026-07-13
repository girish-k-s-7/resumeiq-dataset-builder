from pydantic import BaseModel

from app.schemas.candidate import Candidate
from app.schemas.education import Education
from app.schemas.experience import Experience
from app.schemas.project import Project

class Resume(BaseModel):
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