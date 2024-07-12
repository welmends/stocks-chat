from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic.base import RedirectView

from chat.registration.views import SignUpView

urlpatterns = [
    path(
        "",
        RedirectView.as_view(url="registration/login", permanent=False),
        name="index",
    ),
    path("registration/signUp", SignUpView.as_view(), name="signUp"),
    path(
        "registration/login",
        LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("registration/logout", LogoutView.as_view(next_page="login"), name="logout"),
]
