from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.dashboardView, name='rooms'),
    path('chat', views.chatView, name='chat'),
]