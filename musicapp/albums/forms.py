from django import forms
from musicapp.albums.models import Album


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['title',
                  'artist',
                  'artwork',
                  'genre_choice',
                  'post_date']
