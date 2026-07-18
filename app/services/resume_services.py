from pathlib import Path
from app.schemas.resume import Resume
from app.services.json_services import save_resume
from app.services.template_services import save_html
from app.services.pdf_services import save_pdf

def generate_resume_files(resume: Resume) -> dict[str, Path]:
    """Generate all resumeartifacts.
    steps:
    save resume as json
    render and save html
    generate pdf

    returns: dictionary containing generated file paths."""

    json_file = save_resume(resume)
    html_file = save_html(resume)
    pdf_file = save_pdf(html_file)

    return {
        "json":json_file,
        "html":html_file,
        "pdf":pdf_file,
    }