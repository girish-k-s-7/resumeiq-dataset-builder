from pydantic import BaseModel


class Publication(BaseModel):
    title: str
    publisher: str
    date: str