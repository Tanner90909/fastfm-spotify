from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column

class Base (DeclarativeBase):
    pass

class ArtistModel(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name:Mapped[str] = Column(String, default="Name")

    artist_albums = relationship("AlbumArtists", back_populates="artist")
