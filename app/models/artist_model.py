from typing import List, Optional
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column
from app.models.base_model import Base
from app.models.album_model import AlbumModel
from app.models.song_model import SongModel


class ArtistModel(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name:Mapped[str] = Column(String, default="Name")

    artist_albums: Mapped[List["AlbumModel"]] = relationship("AlbumArtists", back_populates="artist")
    song_artist: Mapped[List["SongModel"]] = relationship("SongArtists", back_populates="artist")
