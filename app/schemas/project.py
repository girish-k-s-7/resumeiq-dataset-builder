from pydantic import BaseModel

class Project(BaseModel):
    name: str
    duration: str
    description: list[str]