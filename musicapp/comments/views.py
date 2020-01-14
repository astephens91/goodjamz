from django.shortcuts import render, redirect
from musicapp.comments.forms import PostForm
from musicapp.comments.models import Post
from django.db.models import F

def post(request):
    if request.method == 'POST':
            form = PostForm(data=request.POST)
            if form.is_valid():
                data = form.cleaned_data
                boast = Post.objects.create(body=data['post'])
                redirecturl = request.POST.get('redirect', '/')
                return redirect(redirecturl)
    else:
        form = PostForm()
    return render(request, 'generic_form.html', {'form': form})

def upvote(request, element_id):
    post = Post.objects.get(id=element_id)
    post.upvotes += 1
    post.save()
    return redirect('/')

def downvote(request, element_id):
    post = Post.objects.get(id=element_id)
    post.downvotes += 1
    post.save()
    return redirect('/')

def highestvoted(request):
    votes_with_score = Post.objects.annotate(vote_score=(F('upvotes')-F('downvotes')))
    posts = votes_with_score.order_by('-vote_score')

    return render(request, 'highestvoted.html', {'posts': posts})