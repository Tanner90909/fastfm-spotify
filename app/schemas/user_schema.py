from typing import Optional, List
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str | None = None