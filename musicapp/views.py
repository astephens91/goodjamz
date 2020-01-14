from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views import View
from musicapp.albums.models import Album, Rating
from musicapp.jamusers.models import CustomUser
from musicapp.comments.models import Post


class index(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:

            html = "index.html"
            albums = Album.objects.all()
            posts = Post.objects.all()
 
            return render(request, html, {'albums': albums, 'posts':posts})


class albumview(View):
    def get(self, request, id):

        html = "album_details.html"
        album = Album.objects.filter(id=id)
        print(request.user)

        return render(request, html, {'album': album})


class userview(View):
    def get(self, request, id):

        html = "user_details.html"
        user = CustomUser.objects.filter(id=id)
        wishlist = Album.objects.filter(wishlist=request.user)
        albums_uploaded = Album.objects.filter(uploaded_by=request.user)

        return render(request, html, {'user': user,
                                      'wishlist': wishlist,
                                      'albums_uploaded': albums_uploaded})


def add_wishlist(request, id):
    target_user = request.user
    current_album = Album.objects.get(id=id)

    if current_album.wishlist.filter(id=target_user.id).exists():
        current_album.wishlist.remove(target_user)
        print("Removed from Wishlist!")
    else:
        current_album.wishlist.add(target_user)
        print("Added to Wishlist!")

    return redirect(request.META.get('HTTP_REFERER', '/'))


def rating(request):

    html = 'index.html'
    all_ratings = Rating.objects.all()

    return render(request, html, {'all_ratings': all_ratings})
