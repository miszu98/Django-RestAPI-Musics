from django.contrib import admin
from .models import Song, Artist
from django.utils.html import format_html

# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "artist", "name_of_song", "make_clickable_link"]
    list_filter = ["artist"]

    def make_clickable_link(self, obj):
        if obj.youtube_url is not None:
            return format_html(f'<a href="{obj.youtube_url}" target="_blank">{obj.youtube_url}</a>')
        else:
            return "Here should be a link"

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["id",   "artistic_nickname", "first_name", "last_name"]




