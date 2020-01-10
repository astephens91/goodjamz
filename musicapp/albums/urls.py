from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static
from musicapp.albums import views

urlpatterns = [ 
    path('album_upload/', views.album_artwork_view, name='image_upload'), 
    path('success', views.success, name='success'), 
] 

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) 