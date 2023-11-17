from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database import SessionLocal
from app.schemas.user_schema import UserSchema
from app.controllers.user_controller import get_all_users

router = APIRouter(
    prefix="/users"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users