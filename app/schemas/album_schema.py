from typing import Optional, List
from pydantic import BaseModel

class AlbumSchema(BaseModel):
    id: int
    name: str | None = None

