from django.shortcuts import render, get_object_or_404

from .forms import GameForm
from .models import Game, Genre


def index(request):
    games = Game.objects.all()
    context = {
        'games': games,
        'title': 'ArcadiaX'
    }
    return render(request, 'games/index.html', context=context)


def get_genre(request, genre_id):
    games = Game.objects.filter(genres__id=genre_id)
    genre = get_object_or_404(Genre, pk=genre_id)  # Безопаснее
    context = {
        'games': games,
        'genre': genre
    }
    return render(request, 'games/genre.html', context=context)


def game_view(request, game_id):
    game_item = get_object_or_404(Game, id=game_id)
    return render(request, 'games/view_game.html', {'game_item': game_item})


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
    else:
        form = GameForm()
    return render(request, 'games/add_game.html', context={'form': form})


from .tasks import notify_new_game

notify_new_game.delay(add_game.id)
