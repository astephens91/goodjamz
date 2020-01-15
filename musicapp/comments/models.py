from django.db import models
from django.utils import timezone
from musicapp.albums.models import Album
import computed_property


class Post(models.Model):
    Post = 'Post'
    body = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    score = computed_property.ComputedIntegerField(compute_from='get_score')

    @property
    def get_score(self):
        vote_score = self.upvotes - self.downvotes
        return vote_score
 
    def __str__(self):
        return self.body


# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     # user = models.CharField(max_length=200)
#     email = models.EmailField()
#     body = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     # approved = models.BooleanField(default=False)

#     # def approved(self):
#     #     self.approved = True
#     #     self.save()

#     def __str__(self):
#         return self.body