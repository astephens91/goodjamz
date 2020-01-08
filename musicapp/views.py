from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from musicapp.albums.models import Album
from musicapp.jamusers.models import CustomUser

class index(View):

    def get(self, request):
        html = "index.html"
        albums = Album.objects.all()
        logged_in_user = CustomUser.objects.filter(email=request.user).first()

        data = {
        'albums': albums,
        'logged_in_user': logged_in_user,
        }
        return render(request, html, data)
