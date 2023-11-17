from app.schemas.user_schema import UserSchema
from sqlalchemy.orm import Session, joinedload
from app.models.user_model import UserModel, LikedSongsModel
from app.models.album_model import AlbumArtistsModel, AlbumModel
from app.models.artist_model import ArtistModel
from app.models.playlist_model import PlaylistListenersModel, PlaylistModel, PlaylistSongsModel
from app.models.song_model import SongArtistsModel,SongModel


def get_all_users(db:Session):
    users_query = (
        db.query(UserModel).options(joinedload(UserModel.playlist_listener).joinedload(PlaylistListenersModel.user).joinedload(UserModel.liked_song).joinedload(LikedSongsModel.user)).all()
    )

    return users_query