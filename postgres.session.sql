-- -- DROP TABLE "AlbumArtists";
-- DROP TABLE "Artist";
-- -- DROP TABLE "LikedSongs";
-- DROP TABLE "Playlist";
-- -- DROP TABLE "PlaylistListeners";
-- -- DROP TABLE "PlaylistSongs";
-- DROP TABLE "Song";
-- -- DROP TABLE "SongArtists";
-- DROP TABLE "User";
-- DROP TABLE "Album";

-- CREATE TABLE "Song" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "length_seconds" int,
--   "album_id" int
-- );

-- CREATE TABLE "Album" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar
-- );

-- CREATE TABLE "Artist" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar
-- );

-- CREATE TABLE "User" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar
-- );

-- CREATE TABLE "Playlist" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "playlist_owner_id" int
-- );

-- CREATE TABLE "SongArtists" (
--   "id" SERIAL PRIMARY KEY,
--   "song_id" int,
--   "artist_id" int,
--   FOREIGN KEY ("song_id") REFERENCES "Song" ("id"),
--   FOREIGN KEY ("artist_id") REFERENCES "Artist" ("id")
-- );

-- CREATE TABLE "AlbumArtists" (
--   "id" SERIAL PRIMARY KEY,
--   "album_id" int,
--   "artist_id" int,
--   FOREIGN KEY ("album_id") REFERENCES "Album" ("id"),
--   FOREIGN KEY ("artist_id") REFERENCES "Artist" ("id")
-- );

-- CREATE TABLE "PlaylistSongs" (
--   "id" SERIAL PRIMARY KEY,
--   "playlist_id" int,
--   "song_id" int,
--   "order_in_playlist" int,
--   FOREIGN KEY ("playlist_id") REFERENCES "Playlist" ("id"),
--   FOREIGN KEY ("song_id") REFERENCES "Song" ("id")
-- );

-- CREATE TABLE "LikedSongs" (
--   "id" SERIAL PRIMARY KEY,
--   "user_id" int,
--   "song_id" int,
--   FOREIGN KEY ("user_id") REFERENCES "User" ("id"),
--   FOREIGN KEY ("song_id") REFERENCES "Song" ("id")
-- );

-- CREATE TABLE "PlaylistListeners" (
--   "id" SERIAL PRIMARY KEY,
--   "playlist_id" int,
--   "user_id" int,
--   FOREIGN KEY ("playlist_id") REFERENCES "Playlist" ("id"),
--   FOREIGN KEY ("user_id") REFERENCES "User" ("id")
-- );


