from django import forms
from .models import Genre, Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        initial = {
            'is_published': True
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'descr': forms.Textarea(attrs={'rows': 10})
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

