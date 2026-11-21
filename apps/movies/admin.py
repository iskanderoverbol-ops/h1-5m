from django.contrib import admin

from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_year", "rating")
    list_filter = ("release_year", "rating")
    search_fields = ("title",)