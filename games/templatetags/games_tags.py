from django import template

from games.models import Genre

register = template.Library()


@register.simple_tag()
def get_list_genres():
    return Genre.objects.all()


@register.inclusion_tag('games/list_genres.html')
def list_genres():
    genres = Genre.objects.all()
    return {'genres': genres}