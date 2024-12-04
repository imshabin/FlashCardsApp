"""
Authentication endpoints
"""
from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, User

router = APIRouter()

@router.post("/signup", response_model=User)
async def signup(user: UserCreate):
    # TODO: Implement user registration
    pass

@router.post("/login")
async def login():
    # TODO: Implement user login
    pass