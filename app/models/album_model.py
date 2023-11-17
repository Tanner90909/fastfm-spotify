from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column

class Base(DeclarativeBase):
    pass

class AlbumModel(Base):
    __tablename__= "albums"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")

    album_artists = relationship("AlbumArtists", back_populates="album")

class AlbumArtists(Base):
    __tablename__= "albumartists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"))

    album = relationship("AlbumModel", back_populates="album_artists")
    artist = relationship("ArtistModel", back_populates="album_artists")

