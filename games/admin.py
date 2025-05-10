from django.contrib import admin

from .models import Game
from .models import Genre


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_genres', 'price', 'release_date', 'updated_date', 'is_published')
    list_display_links = ('id', 'title', 'get_genres')
    search_fields = ('title', 'descr')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'genres')

    def get_genres(self, obj):
        return ", ".join(genre.title for genre in obj.genres.all())

    get_genres.short_description = 'Genres'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Game, GameAdmin)
admin.site.register(Genre, GenreAdmin)
