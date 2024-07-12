from django.urls import path

from chat.dashboard.views import get_messages, send_message
from chat.dashboard.views.chat_view import ChatView
from chat.dashboard.views.create_room_view import CreateRoomView
from chat.dashboard.views.dashboard_view import DashboardView

urlpatterns = [
    path("rooms", DashboardView.as_view(), name="rooms"),
    path("create_room", CreateRoomView.as_view(), name="create_room"),
    path("chat/<int:room_id>", ChatView.as_view(), name="chat"),
    path("send_message", send_message, name="send_message"),
    path("get_messages", get_messages, name="get_messages"),
]
