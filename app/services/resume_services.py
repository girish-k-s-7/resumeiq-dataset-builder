from pathlib import Path
from app.schemas.resume import Resume
from app.services.json_services import save_resume
from app.services.template_services import save_html
from app.services.pdf_services import save_pdf

def generate_resume_files(resume: Resume) -> dict[str, Path]:
    generated_files = {}

    html_file = save_html(resume)

    try:

        pdf_file = save_pdf(html_file)
        generated_files["pdf"] = pdf_file

        if resume.consent:
            json_file = save_resume(resume)

            generated_files["json"] = json_file
            generated_files["html"] = html_file
    finally:
        if not resume.consent:
            html_file.unlink(missing_ok=True)
    return generated_files