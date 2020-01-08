from django.urls import path
from musicapp.authentication import views

from .views import SignUpView

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
]
