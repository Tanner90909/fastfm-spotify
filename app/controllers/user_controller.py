from app.schemas.user_schema import UserSchema
from sqlalchemy.orm import Session
from app.models.user_model import UserModel

def get_all_users(db:Session):
    users_query = (
        db.query(UserModel).all()
    )

    return users_query