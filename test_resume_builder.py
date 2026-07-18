from app.services.resume_builder import build_resume
from app.services.json_services import load_resume, save_resume
from app.services.template_services import save_html
from app.services.pdf_services import save_pdf

resume = build_resume(1)

json_file = save_resume(resume)
html_file = save_html(resume)
pdf_file = save_pdf(html_file)

print(f"JSON saved to : {json_file}")
print(f"HTML saved to : {html_file}")
print(f"PDF saved to: {pdf_file}")