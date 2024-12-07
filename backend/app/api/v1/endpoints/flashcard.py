<<<<<<< HEAD
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
=======
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.flashcard import Flashcard
from app.models.user import User
from app.schemas.flashcard import FlashcardCreate, FlashcardResponse
from app.services.ai import gemini_service

router = APIRouter()

@router.post("/", response_model=FlashcardResponse)
async def create_flashcard(
    flashcard: FlashcardCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Create new flashcard
    db_flashcard = Flashcard(
        question=flashcard.question,
        answer=flashcard.answer,
        user_id=current_user.id
    )
    
    # Optionally enhance the answer using AI
    if flashcard.enhance_answer:
        enhanced_answer = await gemini_service.enhance_answer(
            flashcard.question,
            flashcard.answer
        )
        db_flashcard.answer = enhanced_answer
    
    db.add(db_flashcard)
    await db.commit()
    await db.refresh(db_flashcard)
    
    return db_flashcard

@router.get("/", response_model=List[FlashcardResponse])
async def get_flashcards(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Flashcard)
        .where(Flashcard.user_id == current_user.id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()

@router.get("/{flashcard_id}", response_model=FlashcardResponse)
async def get_flashcard(
    flashcard_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Flashcard)
        .where(
            Flashcard.id == flashcard_id,
            Flashcard.user_id == current_user.id
        )
    )
    flashcard = result.scalar_one_or_none()
    
    if not flashcard:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Flashcard not found"
        )
    
    return flashcard
>>>>>>> feature/1.34
