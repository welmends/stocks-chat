from django.urls import path

from . import views

urlpatterns = [
    path("rooms", views.dashboard_view, name="rooms"),
    path("create_room", views.create_room_view, name="create_room"),
    path("chat/<int:room_id>", views.chat_view, name="chat"),
    path("send_message", views.send_message, name="send_message"),
    path("get_messages", views.get_messages, name="get_messages"),
]
