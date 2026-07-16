from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from app.schemas.resume import Resume

TEMPLATE_DIR = Path("app/templates")
OUTPUT_DIR = Path("generated/html")

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
)

def render_resume(resume: Resume) -> str:
    """render a resume into html"""
    template = env.get_template("ats_v1.html")
    return template.render(resume=resume)

def save_html(resume: Resume) -> Path:
    """save the rendered html to a file"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html = render_resume(resume)
    file_path = OUTPUT_DIR / f"{resume.candidate.candidate_id.lower()}.html"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html)
    return file_path