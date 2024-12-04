"""
Flashcard management endpoints
"""
from fastapi import APIRouter, Depends
from app.schemas.flashcard import FlashcardCreate, Flashcard

router = APIRouter()

@router.post("/", response_model=Flashcard)
async def create_flashcard(flashcard: FlashcardCreate):
    # TODO: Implement flashcard creation
    pass

@router.get("/{flashcard_id}", response_model=Flashcard)
async def get_flashcard(flashcard_id: int):
    # TODO: Implement get flashcard
    pass