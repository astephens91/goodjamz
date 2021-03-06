from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from musicapp.albums import views


urlpatterns = [
    path('album_upload/', views.album_artwork_view, name='album_upload'),
    path('', views.album_list, name='homepage'),
    path('rating/<int:id>/', views.rating_add_view, name='add_ratings'),
    path('edit/<int:id>/', views.editalbum, name='edit'),
    path('delete/<int:id>/', views.deletealbum, name='delete'),
    path('ballotstuff/', views.ballotstuff, name="ballotstuff")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
