from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.study_session import StudySession
from app.models.user import User
from app.schemas.study import StudySessionResponse

router = APIRouter()

@router.post("/start", response_model=StudySessionResponse)
async def start_session(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Create new study session
    session = StudySession(
        user_id=current_user.id,
        start_time=datetime.utcnow()
    )
    db.add(session)
    await db.commit()
    await db.refresh(session)
    
    return session

@router.post("/end/{session_id}", response_model=StudySessionResponse)
async def end_session(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Get and update study session
    result = await db.execute(
        select(StudySession)
        .where(
            StudySession.id == session_id,
            StudySession.user_id == current_user.id
        )
    )
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Study session not found"
        )
    
    session.end_time = datetime.utcnow()
    await db.commit()
    await db.refresh(session)
    
    return session
