from pydantic import BaseModel

class Content(BaseModel):
    title: str
    year: int
    length: int
    producer: str
    description: str
    genre: str