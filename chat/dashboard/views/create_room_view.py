from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from ..forms import CreateRoomForm


@method_decorator(login_required(login_url=settings.LOGIN_URL), name="dispatch")
class CreateRoomView(View):
    def get(self, request):
        form = CreateRoomForm()
        context = {"form": form}
        return render(request, "dashboard/rooms/create.html", context)

    def post(self, request):
        form = CreateRoomForm(request.POST)
        if request.POST.get("button") == "Back":
            return redirect("rooms")
        if form.is_valid() and form.data["name"] != "":
            form.save()
            return redirect("rooms")
        context = {"form": form}
        return render(request, "dashboard/rooms/create.html", context)
