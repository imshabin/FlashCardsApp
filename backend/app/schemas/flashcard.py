"""
Pydantic schemas for Flashcard
"""
from pydantic import BaseModel

class FlashcardBase(BaseModel):
    question: str
    answer: str

class FlashcardCreate(FlashcardBase):
    pass

class Flashcard(FlashcardBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
