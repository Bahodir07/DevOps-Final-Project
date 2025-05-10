from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('genre/<int:genre_id>/', get_genre, name='genre'),
    path('game/<int:game_id>', game_view, name='game_view'),
    path('game/add_game/', add_game, name='add_game')
]
