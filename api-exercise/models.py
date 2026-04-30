from pydantic import BaseModel, Field


class Book(BaseModel):
    id: int 
    title: str
    author: str 
    price: float = Field(gt=0)


