from django import forms
from musicapp.comments.models import Post

class PostForm(forms.ModelForm):
    Post = 'Post'
    post = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Post', 'class': 'form-control'}))
    
    class Meta:
        model = Post
        fields = ['post']

# from django import forms
# from musicapp.comments.models import Comment

# class CommentForm(forms.ModelForm)
#     class Meta:
#         model = Comment
#         fields = ('email', 'body')
