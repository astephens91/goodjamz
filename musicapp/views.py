from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from musicapp.albums.models import Album
from musicapp.jamusers.models import CustomUser



class index(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:

            html = "index.html"

            albums = Album.objects.all()

            return render(request, html, {'albums': albums})


class albumview(View):
    def get(self, request, id):

        html = "album_details.html"

        album = Album.objects.filter(id=id)

        return render(request, html, {'album': album})


class userview(View):
    def get(self, request, id):

        html = "user_details.html"

        user = CustomUser.objects.filter(id=id)

        return render(request, html, {'user': user})

