from app.schemas.user_schema import UserSchema
from sqlalchemy.orm import Session
from app.models.user_model import UserModel, LikedSongsModel
from app.models.album_model import AlbumArtists, AlbumModel
from app.models.artist_model import ArtistModel
from app.models.playlist_model import PlaylistListenersModel, PlaylistModel, PlaylistSongsModel
from app.models.song_model import SongArtistsModel,SongModel


def get_all_users(db:Session):
    users_query = (
        db.query(UserModel).all()
    )

    return users_query