from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render, redirect
# from django.contrib.auth.decorators import login_required
from musicapp.albums.forms import AlbumForm, RatingForm
from musicapp.albums.models import Album, Rating
from musicapp.jamusers.models import CustomUser
from django.views import View


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


# class AlbumFormView(View):
#     form_class = AlbumForm
#     queryset = Album.objects.all()

#     def rate_movie(self, request, pk=None):
#         if 'stars' in request.data:

#             album = Album.objects.get(id=pk)
#             stars = request.data['stars']
#             # user = request.user['user']
#             user = CustomUser.objects.get(id=1)
         
#             try:
#                 rating = Rating.objects.get(user=user.id, album=album.id)
#                 rating.stars = stars
#                 rating.save()

#             except:
#                 Rating.objects.create(user=user, album=album, stars=stars)


# class RatingFormView(View):
#     form_class = RatingForm
#     queryset = Rating.objects.all()
