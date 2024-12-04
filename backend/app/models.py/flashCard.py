"""
SQLAlchemy model for Flashcard
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Flashcard(Base):
    __tablename__ = "flashcards"
    
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))