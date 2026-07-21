from pydantic import BaseModel, Field

class Book(BaseModel):
    id: int
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    price: float = Field(gt=0) 