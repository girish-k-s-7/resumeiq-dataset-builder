from app.schemas.candidate import Candidate
from app.schemas.education import Education
from app.schemas.experience import Experience
from app.schemas.project import Project
from app.schemas.resume import Resume

from app.services.candidate_identity import generate_candidate_identity

def build_resume(candidate_number: int) -> Resume:
    identity = generate_candidate_identity(candidate_number)

    candidate = Candidate(
        candidate_id=identity["candidate_id"],
        name=identity["candidate_id"],
        title="Software Engineer",
        email=identity["email"],
        phone=identity["phone"],
        github=identity["github"],
        linkedin=identity["linkedin"],
        location=identity["location"],
    )

    experience = [
        Experience(
            company="ABC Technologies",
            role="Software Engineer",
            duration="jan 2024 - present",
            location="Banglore, India",
            description=[
                "Developed REST API's using FasteAPI.",
                "Improved application performance."
            ],
            )
    ]

    projects=[
        Project(
            name="ResumeIQ Dataset Builder",
            duration="2026",
            description=[
                "Built an internal too for resume data set creation.",
                "Genarated ATS friendly resume PDFs.",
            ],
        
        )
    ]

    education=[
        Education(
            degree="Bachelor of Engineering",
            institution="TOCE",
            duration="2022 - 2026",
            location="Banglore, India",
        )
    ]

    return Resume(
        candidate=candidate,
        summary="Passionate software engineer with strong python and backend development skills.",
        skills=[
            "Python",
            "FastAPI",
            "Pydantic",
            "Git",
            "Docker",
        ],
        experience=experience,
        projects=projects,
        education=education,
    )