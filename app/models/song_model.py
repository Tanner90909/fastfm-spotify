from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column
from .base import Base
# from app.models.artist_model import ArtistModel
# from app.models.playlist_model import PlaylistSongsModel


class SongModel(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")
    length_seconds: Mapped[int] = Column(Integer, default="length_seconds")
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))

    song_artist: Mapped[List["SongArtistsModel"]] = relationship(back_populates="song")
    liked_song: Mapped[List["LikedSongsModel"]] = relationship(back_populates="song")
    playlist_song: Mapped[List["PlaylistSongsModel"]] = relationship(back_populates="song")


class SongArtistsModel(Base):
    __tablename__ = "songartists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))

    song: Mapped[List["SongModel"]] = relationship(back_populates="song_artist")
    artist: Mapped[List["ArtistModel"]] = relationship(back_populates="song_artist")