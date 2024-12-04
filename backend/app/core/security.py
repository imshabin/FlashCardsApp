"""
Security utilities for authentication and authorization
"""
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# TODO: Implement password hashing and verification
# TODO: Implement JWT token creation and validation