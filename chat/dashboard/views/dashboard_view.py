from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from ..models import Room


@method_decorator(login_required(login_url=settings.LOGIN_URL), name="dispatch")
class DashboardView(View):
    def get(self, request):
        context = {"rooms": Room.objects.all()}
        return render(request, "dashboard/rooms/home.html", context)

    def post(self, request):
        rooms = Room.objects.filter(name=request.POST.get("room_button"))
        if len(rooms) > 0:
            room = rooms[0]
            return redirect("chat/{}".format(room.id))
        else:
            context = {"rooms": rooms}
            return render(request, "dashboard/rooms/home.html", context)
