from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

# https://testdriven.io/blog/django-custom-user-model/

class CustomUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    wishlist = models.ManyToManyField('self', related_name='wishlist+',
                                      symmetrical=False, blank=True)

    objects = CustomUserManager()

    def natural_key(self):
        return dict(email=self.email)


CustomUser._meta.get_field('email')._unique = True
CustomUser._meta.get_field('email')._blank = False
CustomUser._meta.get_field('username')._unique = False
CustomUser._meta.get_field('username')._blank = True
CustomUser._meta.get_field('username')._null = True