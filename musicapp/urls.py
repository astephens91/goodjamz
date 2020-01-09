"""musicapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from musicapp.albums.urls import urlpatterns as album_urls
from musicapp.authentication.urls import urlpatterns as auth_urls

from musicapp import views

app_name = 'ratings'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name='homepage'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('album/<int:id>/', views.albumview.as_view(), name='album_details'),
    path('userdetails/<int:id>/', views.userview.as_view(), name='user_details')
]

urlpatterns += album_urls
urlpatterns += auth_urls

