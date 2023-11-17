from typing import Optional, List
from pydantic import BaseModel

class PlaylistSchema(BaseModel):
    id: int
    name: str | None = None
    playlist_owner_id: int
    