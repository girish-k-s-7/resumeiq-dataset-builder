from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.schemas.resume import Resume
from app.schemas.resume_create import ResumeCreate
from app.services.resume_services import generate_resume_files

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.post("/")
async def generate_resume(resume_data: ResumeCreate):
    
    # creating internal resume  object with auto genarte UUID
    resume = Resume(
        resume_id=str(uuid4()),
        **resume_data.model_dump()
    )

    # generating JSON, HTML, PDF
    generate_resume_files(resume)

    return{
        "status": "success",
        "message": "Resume generated successfully.",
        "resume_id": resume.resume_id,
        "download_url": f"/resume/{resume.resume_id}/download"
            }

@router.get("/{resume_id}/download")
async def download_resume(resume_id: str):
    pdf_path = Path(f"generated/pdf/{resume_id}.pdf")
    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Resume Not Found."
        )
    
    return FileResponse(
        path=pdf_path,
        media_type="application/pdf",
        filename=f"{resume_id}.pdf",
    )