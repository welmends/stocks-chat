from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboard', views.dashboardView, name='dashboard'),
    path('signIn', views.signInView, name='signIn'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='home'), name='logout')

]