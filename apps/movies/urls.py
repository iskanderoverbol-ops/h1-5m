from django.urls import path
from . import views


urlpatterns = [
    path("movies/", views.movie_list_create, name="movie-list-create"),
    path("movies/top/", views.top_movies, name="top-movies"),
    path("movies/<int:pk>/", views.movie_detail, name="movie-detail"),
]