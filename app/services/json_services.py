import json
from pathlib import Path
from app.schemas.resume import Resume

OUTPUT_DIR = Path("generated/json")

def save_resume(resume: Resume) -> Path:

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    file_path = OUTPUT_DIR / f"{resume.candidate.candidate_id.lower()}.josn"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            resume.model_dump(),
            file,
            indent=4,
            ensure_ascii=False,
        )
    return file_path

def load_resume(file_path: Path) -> Resume:
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    return Resume(**data)