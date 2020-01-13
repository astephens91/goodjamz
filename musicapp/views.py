from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from musicapp.albums.models import Album, Rating


class index(View):

    def get(self, request):

        html = "index.html"

        albums = Album.objects.all()

        return render(request, html, {'albums': albums})


def rating(request):

    html = 'index.html'

    all_ratings = Rating.objects.all()

    return render(request, html, {'all_ratings': all_ratings})
