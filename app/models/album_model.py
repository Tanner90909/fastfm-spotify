from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column
from .base import Base


class AlbumModel(Base):
    __tablename__= "albums"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")

    artist_albums: Mapped[List["AlbumArtistsModel"]] = relationship(back_populates="album")

class AlbumArtistsModel(Base):
    __tablename__= "albumartists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))

    album: Mapped[List["AlbumModel"]] = relationship(back_populates="artist_albums")
    artist: Mapped[List["ArtistModel"]] = relationship(back_populates="artist_albums")

