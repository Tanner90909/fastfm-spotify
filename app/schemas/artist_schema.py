from typing import Optional, List
from pydantic import BaseModel

class ArtistSchema(BaseModel):
    id: int
    name: str | None = None
    