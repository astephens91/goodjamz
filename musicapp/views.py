from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from musicapp.albums.models import Album

from musicapp.jamusers.models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()

class index(View):

    def get(self, request):
        html = "index.html"
        albums = Album.objects.all()
        
        data = {
        'albums': albums,
        }
        return render(request, html, data)
