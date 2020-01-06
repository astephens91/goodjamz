from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
import datetime


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    artwork = models.ImageField(upload_to='images/', null=True, blank=True)
    ratings = GenericRelation(Rating, related_query_name='albums')
    post_date = models.DateTimeField(default=datetime.datetime.now())
    # uploaded_by = models.ForeignKey()

    def __str__(self):
        return f'{self.title} by {self.artist} uploaded  by'