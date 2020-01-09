from django.urls import path
from musicapp.jamusers import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup')
]