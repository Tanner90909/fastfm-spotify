from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column
from app.models.base_model import Base

class PlaylistModel(Base):
    __tablename__ = "playlists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")
    playlist_owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

class PlaylistSongsModel(Base):
    __tablename__ = "playlistsongs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlists.id"))
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))
    order_in_playlist: Mapped[int] = Column(Integer, default="order_in_playlist")

class PlaylistListeners(Base):
    __tablename__ = "playlistlisteners"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlists.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    