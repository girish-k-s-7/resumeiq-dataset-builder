from fastapi import FastAPI

app = FastAPI(
    title="ResumeIQ Dataset Builder",
    description="Internal tool for generating anonymized ATS-friendly resumes.",
    version="0.1.0",
)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "ResumeIQ Dataset Builder API is running."
    }