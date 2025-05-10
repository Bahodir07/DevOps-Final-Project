from django.db import models
from django.urls import reverse


class Genre(models.Model):
    title = models.CharField(max_length=150, db_index=True, unique=True, verbose_name="Жанр")

    def get_absolute_url(self):
        return reverse('genre', kwargs={"genre_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    descr = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Цена')
    release_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    genres = models.ManyToManyField(Genre, related_name='games', verbose_name='Жанр')

    def get_absolute_url(self):
        return reverse('game_view', kwargs={"game_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

