from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SongSerializer, ArtistSerializer
from .models import Song, Artist
from rest_framework import status


# Create your views here.
@api_view(["GET"])
def songs_list(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def artists_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_details_about_artist_by_id(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    serializer = ArtistSerializer(artist, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_songs_from_artist_by_id(request, artist_id):
    songs = Song.objects.filter(artist_id=artist_id)
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_songs_from_artist_by_nickname(request, artistic_nickname):
    songs = Song.objects.filter(artist_id=Artist.objects.get(artistic_nickname=artistic_nickname).id)
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_song(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def add_artist(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_song(request, song_id):
    song = Song.objects.get(id=song_id)
    serializer = SongSerializer(instance=song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_song(request, song_id):
    song = Song.objects.get(id=song_id)
    song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["DELETE"])
def delete_artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    artist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



