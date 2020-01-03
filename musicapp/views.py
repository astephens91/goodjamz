from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from musicapp.albums.models import Album


class index(View):

    def get(self, request):

        html = "index.html"

        albums = Album.objects.all()

        return render(request, html, {'data': albums})