from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column
# from app.models.playlist_model import PlaylistListenersModel
# from app.models.song_model import SongModel

class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")

    liked_song: Mapped[List["LikedSongsModel"]] = relationship("LikedSongsModel", back_populates="user")
    playlist_listener: Mapped[List["PlaylistListenersModel"]] = relationship("PlaylistListenersModel", back_populates="user")


class LikedSongsModel(Base):
    __tablename__ = "likedsongs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))

    user: Mapped[List["UserModel"]] = relationship("UserModel", back_populates="liked_song")
    song: Mapped[List["SongModel"]] = relationship("SongModel", back_populates="liked_song")