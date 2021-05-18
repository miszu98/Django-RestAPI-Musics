from django.urls import path
from . import views as v

urlpatterns = [
    path("songs/", v.songs_list),
    path("artists/", v.artists_list),
    path("artist/<int:artist_id>", v.get_details_about_artist_by_id),
    path("songs/artist_id=<int:artist_id>", v.get_songs_from_artist_by_id),
    path("songs/artistic_nickname=<str:artistic_nickname>", v.get_songs_from_artist_by_nickname),
    path("add_song/", v.add_song),
    path("add_artist/", v.add_artist),
    path("update_song/<int:song_id>", v.update_song),
    path("delete_song/<int:song_id>", v.delete_song),
    path("delete_artist/<int:artist_id>", v.delete_artist),
]