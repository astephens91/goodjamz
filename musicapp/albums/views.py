from django.shortcuts import HttpResponseRedirect, render, redirect, reverse
# from django.contrib.auth.decorators import login_required
from musicapp.albums.models import Album, Rating
from musicapp.albums.forms import AlbumForm
from musicapp.albums.filters import AlbumFilter


def album_artwork_view(request):

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.uploaded_by = request.user
            instance.save()
            return redirect('success')

    else:
        form = AlbumForm()
    return render(request, 'upload_form.html', {'form': form})


def success(request):
    return HttpResponseRedirect(reverse('homepage'))


def album_list(request):
    f = AlbumFilter(request.GET, queryset=Album.objects.all())
    return render(request, 'index.html', {'filter': f})


def rating_add_view(request, id):

    if request.method == "POST":
        instance = Album.objects.get(id=id)
        star_rating = int(request.POST.get('rating')[0])
        add_rating = Rating.objects.create(
            album=instance, user=request.user, stars=star_rating)

    return HttpResponseRedirect(reverse('homepage'))
