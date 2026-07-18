from fastapi import FastAPI

from app.api.routes.resume import router as resume_router
app = FastAPI(
    title="ResumeIQ Dataset Builder",
    description="Build professional ATS-Friendly resumes and optioanlly contribute anonymized data for ResumeIQ.",
    version="0.1.0",
)


app.include_router(resume_router)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to ResumeIQ API.",
        "docs":"/docs"
    }