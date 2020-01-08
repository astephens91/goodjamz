from django.http import HttpResponse
from django.shortcuts import render, redirect
from musicapp.albums.forms import AlbumForm
from musicapp.albums.models import Album


def album_artwork_view(request):

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = AlbumForm()
    return render(request, 'generic_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded image')
