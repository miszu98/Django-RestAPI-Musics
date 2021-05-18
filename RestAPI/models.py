from django.db import models


# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    artistic_nickname = models.CharField(max_length=100)

    def __str__(self):
        return self.artistic_nickname


class Song(models.Model):
    name_of_song = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    youtube_url = models.URLField(blank=True)

    def __str__(self):
        return self.name_of_song
