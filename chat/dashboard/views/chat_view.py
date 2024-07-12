from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from ..models import Room


@login_required(login_url=settings.LOGIN_URL)
class ChatView(View):
    def get(self, request, room_id=None):
        rooms = Room.objects.filter(id=room_id)
        if len(rooms) > 0:
            context = {"room": rooms[0]}
            return render(request, "dashboard/chat/home.html", context)
        return redirect("rooms")
