from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.dashboardView, name='rooms'),
    path('create-room', views.createRoomView, name='create-room'),
    path('chat/<int:room_id>', views.chatView, name='chat'),
]