from app.services.resume_builder import build_resume
from app.services.json_services import load_resume, save_resume

resume = build_resume(1)
file_path = save_resume(resume)
print(f"Resume saved to: {file_path}")
loaded_resume=load_resume(file_path)
print("\nLoaaaaded Resume:\n")
print(resume.model_dump_json(indent=4))