from django.contrib import admin
from musicapp.albums.models import Album, Rating
from musicapp.jamusers.models import CustomUser
from musicapp.comments.models import Post
# from musicapp.comments.models import Comment

admin.site.register(Album)
admin.site.register(CustomUser)
admin.site.register(Rating)
admin.site.register(Post)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('email',)
#     # list_display = ('email', 'approved')

# admin.site.register(Comment, CommentAdmin)
