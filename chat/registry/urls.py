from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='registry/login', permanent=False), name='index'),
    path('registry/signUp', views.signUpView, name='signUp'),
    path('registry/login', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('registry/logout', LogoutView.as_view(next_page='login'), name='logout')
]