from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column
from app.models.base_model import Base

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")

    liked_song = relationship("LikedSongsModel", back_populates="user")

class LikedSongsModel(Base):
    __tablename__ = "likedsongs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))

    user = relationship("UserModel", back_populates="liked_song")
    song = relationship("SongModel", back_populates="liked_song")