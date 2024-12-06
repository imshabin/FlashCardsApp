from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user
from app.core.database import get_db
from app.core.config import settings
from app.models.user import User
from app.services.pdf import extract_text_from_pdf
from app.services.ai import gemini_service

router = APIRouter()

@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    num_cards: int = 5,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Validate file size and type
    if not file.filename.endswith('.pdf'):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )
    
    content = await file.read()
    if len(content) > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds {settings.MAX_UPLOAD_SIZE // 1024 // 1024}MB limit"
        )
    
    # Extract text from PDF
    text = await extract_text_from_pdf(content)
    
    # Generate flashcards using AI
    flashcards = await gemini_service.generate_flashcards(text, num_cards)
    
    # Store flashcards in database
    db_flashcards = []
    for card in flashcards:
        db_flashcard = Flashcard(
            question=card.question,
            answer=card.answer,
            user_id=current_user.id
        )
        db.add(db_flashcard)
        db_flashcards.append(db_flashcard)
    
    await db.commit()
    
    # Generate study tips
    study_tips = await gemini_service.generate_study_tips(flashcards)
    
    return {
        "flashcards": db_flashcards,
        "study_tips": study_tips
    }