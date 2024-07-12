from django.urls import path

from .views.chat_view import ChatView
from .views.create_room_view import CreateRoomView
from .views.dashboard_view import DashboardView
from .views.message_views import get_messages, send_message

urlpatterns = [
    path("rooms", DashboardView.as_view(), name="rooms"),
    path("create_room", CreateRoomView.as_view(), name="create_room"),
    path("chat/<int:room_id>", ChatView.as_view(), name="chat"),
    path("send_message", send_message, name="send_message"),
    path("get_messages", get_messages, name="get_messages"),
]
