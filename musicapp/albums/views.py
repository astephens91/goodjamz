from django.shortcuts import HttpResponseRedirect, HttpResponse, render, redirect, reverse
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
            return HttpResponseRedirect(reverse('homepage'))

    else:
        form = AlbumForm()
    return render(request, 'upload_form.html', {'form': form})



def album_list(request):
    f = AlbumFilter(request.GET, queryset=Album.objects.all())
    return render(request, 'index.html', {'filter': f})


def rating_add_view(request, id):

    if request.method == "POST":
        instance = Album.objects.get(id=id)
        star_rating = int(request.POST.get('rating')[0])
        targeted_rating = Rating.objects.filter(user=request.user).filter(album=instance)
        if targeted_rating:
            return HttpResponse("No ballot stuffin")
        add_rating = Rating.objects.create(
            album=instance, user=request.user, stars=star_rating)

    return HttpResponseRedirect(reverse('homepage'))


def editalbum(request, id):
    html = "edit_form.html"
    instance = Album.objects.get(id=id)

    if request.method == "POST":
        form = AlbumForm(request.POST, instance=instance)
        form.save()

        return HttpResponseRedirect(reverse('homepage'))

    form = AlbumForm(instance=instance)

    return render(request, html, {'form': form})


def deletealbum(request, id):
    album_to_delete = Album.objects.get(id=id)

    album_to_delete.delete()

    return HttpResponseRedirect(reverse('homepage'))
