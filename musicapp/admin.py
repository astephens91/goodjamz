from django.contrib import admin
from musicapp.albums.models import Album
from musicapp.jamusers.models import CustomUser
from django.contrib.auth import get_user_model

from .authentication.forms import SignupForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_staff', 'date_joined')
    search_fields = ('email', 'is_staff', 'wishlist', 'date_joined')
    ordering = ('email',)

admin.site.register(Album)
admin.site.register(CustomUser, CustomUserAdmin)
    