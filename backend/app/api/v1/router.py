from fastapi import APIRouter
from app.api.v1.endpoints import auth, flashcards, pdf, study

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(flashcards.router, prefix="/flashcards", tags=["flashcards"])
api_router.include_router(pdf.router, prefix="/pdf", tags=["pdf"])
api_router.include_router(study.router, prefix="/study", tags=["study"])