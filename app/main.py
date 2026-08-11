from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.resume import router as resume_router

app = FastAPI(
    title="ResumeIQ Dataset Builder",
    description="Build professional ATS-Friendly resumes and optionally contribute anonymized data for ResumeIQ.",
    version="0.1.0",
)

# Allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to ResumeIQ API.",
        "docs": "/docs",
    }