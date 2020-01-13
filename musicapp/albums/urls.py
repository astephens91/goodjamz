from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from musicapp.albums import views
from musicapp.albums import models

urlpatterns = [
    path('image_upload/', views.album_artwork_view, name='image_upload'),
    path('success', views.success, name='success'),
    path('rating/<int:id>/', views.rating_add_view, name='add_ratings')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
