from django import forms
from musicapp.albums.models import Album, Rating


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['title',
                  'artist',
                  'artwork',
                  'genre_choice',
                  'post_date']


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['album',
                  'user',
                  'stars']
