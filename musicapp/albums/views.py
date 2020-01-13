from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, redirect, render, reverse
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


def rating_add_view(request, id):

    if request.method == "POST":
        instance = Album.objects.get(id=id)
        # star_rating_one = int(request.POST.get('1')[0])
        # star_rating_two = int(request.POST.get('2')[0])
        # star_rating_three = int(request.POST.get('3')[0])
        # star_rating_four = int(request.POST.get('4')[0])
        star_rating = int(request.POST.get('rating')[0])
        add_rating = Rating.objects.create(
            album=instance, user=request.user, stars=star_rating)

    return HttpResponseRedirect(reverse('homepage'))


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
