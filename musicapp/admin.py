from django.contrib import admin
from musicapp.albums.models import Album
from musicapp.jamusers.models import CustomUser

from .authentication.forms import SignupForm


admin.site.register(Album)
admin.site.register(CustomUser)

    