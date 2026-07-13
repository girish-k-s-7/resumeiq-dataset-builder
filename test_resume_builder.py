from app.services.resume_builder import build_resume

resume = build_resume(1)

print(resume.model_dump_json(indent=4))