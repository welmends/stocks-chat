from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path(
        "",
        RedirectView.as_view(url="registration/login", permanent=False),
        name="index",
    ),
    path("registration/signUp", views.signUp_view, name="signUp"),
    path(
        "registration/login",
        LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("registration/logout", LogoutView.as_view(next_page="login"), name="logout"),
]
