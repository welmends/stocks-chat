from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='registration/login', permanent=False), name='index'),
    path('registration/signUp', views.signUpView, name='signUp'),
    path('registration/login', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('registration/logout', LogoutView.as_view(next_page='login'), name='logout')
]