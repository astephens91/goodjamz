import django_filters
from musicapp.albums.models import Album


class AlbumFilter(django_filters.FilterSet):
    class Meta:
        model = Album
        fields = ['genre_choice']
