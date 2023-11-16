from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column
from app.models.base_model import Base

class SongModel(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")
    length_seconds: Mapped[int] = Column(Integer, default="length_seconds")
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))

    song_artist = relationship("SongArtists", back_populates="song")


class SongArtists(Base):
    __tablename__ = "songartists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    song_id: Mapped[int] = mapped_column(ForeignKey("songs.id"))
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))

    song = relationship("SongModel", back_populates="song_artist")
    artist = relationship("ArtistModel", back_populates="song_artist")