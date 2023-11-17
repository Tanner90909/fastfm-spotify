from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database import SessionLocal
from app.schemas.user_schema import UserSchema
from app.controllers.user_controller import get_all_users, create_new_user

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

# @router.post("/create", response_class=UserSchema)
# def create_user(*, db: Session = Depends(get_db), user_in: UserSchema):
#     new_user = create_new_user(db, user_in)
#     return new_user