from django.contrib import admin
from musicapp.albums.models import Album
from musicapp.jamusers.models import CustomUser
from django.contrib.auth import get_user_model

from .authentication.forms import SignupForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = SignupForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_active',]

admin.site.register(Album)
admin.site.register(CustomUser, CustomUserAdmin)
