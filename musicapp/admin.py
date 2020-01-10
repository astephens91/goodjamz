from django.contrib import admin
from musicapp.albums.models import Album, Rating
from musicapp.jamusers.models import CustomUser

admin.site.register(Album)
admin.site.register(CustomUser)
admin.site.register(Rating)
