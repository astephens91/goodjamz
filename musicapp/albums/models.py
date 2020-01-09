# from django.contrib.contenttypes.fields import GenericRelation
# from star_ratings.models import Rating
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from musicapp.jamusers.models import CustomUser


import datetime


class Album(models.Model):

    class Genre(models.TextChoices):
        ROCK = 'Rock', _('Rock')
        HIPHOP = 'HipHop', _('HipHop'),
        RHYTHMANDBLUES = 'R&B', _('R&B'),
        FUNK = 'Funk', _('Funk'),
        SOUL = 'Soul', _('Soul'),
        COUNTRY = 'Country', _('Country'),
        POP = 'Pop', _('Pop'),
        ELECTRONIC = 'Electronic', _('Electronic'),
        JAZZ = 'Jazz', _('Jazz'),
        FOLK = 'Folk', _('Folk'),
        MISCELLANEOUS = 'Miscellaneous', _('Miscellaneous')

    genre_choice = models.CharField(
        max_length=30,
        choices=Genre.choices,
        default=Genre.MISCELLANEOUS
    )
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    artwork = models.ImageField(upload_to='images/', null=True, blank=True)
    post_date = models.DateTimeField(default=datetime.datetime.now())
    description = models.TextField(max_length=None, blank=False)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,
                                    related_name='uploaded_by+', null=True)

    def __str__(self):
        return f'{self.title} by {self.artist} uploaded  by'


class Rating(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    # class Meta:
    #     block_multiple_ratings = (('user,' 'albums'),)
    #     index_together = (('user', 'albums'),)
