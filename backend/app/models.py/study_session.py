"""
SQLAlchemy model for StudySession
"""
from sqlalchemy import Column, Integer, DateTime, ForeignKey

class StudySession(Base):
    __tablename__ = "study_sessions"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
