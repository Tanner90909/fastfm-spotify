from typing import Optional, List
from pydantic import BaseModel

class SongSchema(BaseModel):
    id: int
    name: str | None = None
    length_seconds: int | None = None
    album_id: int | None = None