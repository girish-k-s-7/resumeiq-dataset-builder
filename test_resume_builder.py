from app.services.resume_builder import build_resume
from app.services.json_services import load_resume, save_resume
from app.services.template_services import save_html

resume = build_resume(1)

json_file = save_resume(resume)
html_file = save_html(resume)

print(f"JSON saved to : {json_file}")
print(f"HTML saved to : {html_file}")