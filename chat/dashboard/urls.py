from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.dashboardView, name='rooms'),
    path('create_room', views.createRoomView, name='create_room'),
    path('chat/<int:room_id>', views.chatView, name='chat'),
    path('send_message', views.sendMessage, name='send_message'),
    path('get_messages', views.getMessages, name='get_messages'),
]