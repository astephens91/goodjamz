from django.shortcuts import HttpResponseRedirect, render, redirect, reverse
from musicapp.albums.forms import AlbumForm
from musicapp.albums.models import Album
from musicapp.albums.filters import AlbumFilter
from musicapp.jamusers.models import CustomUser


def album_artwork_view(request):

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = AlbumForm()
    return render(request, 'upload_form.html', {'form': form})


def success(request):
    return HttpResponseRedirect(reverse('homepage'))


def album_list(request):
    f = AlbumFilter(request.GET, queryset=Album.objects.all())
    return render(request, 'index.html', {'filter': f})


