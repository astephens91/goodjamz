from django.urls import path
from musicapp.comments.views import post

urlpatterns = [
    path('postsubmit/', post, name="post"),
]
