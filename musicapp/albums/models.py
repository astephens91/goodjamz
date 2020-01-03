from django.db import models
import datetime


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    artwork = models.ImageField(upload_to='images/', null=True, blank=True)
    post_date = models.DateTimeField(default=datetime.datetime.now())
    # uploaded_by = models.ForeignKey()

    def __str__(self):
        return f'{self.title} by {self.artist} uploaded  by'