from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserSignUpForm


class SignUpView(View):
    def get(self, request):
        form = UserSignUpForm()
        context = {"form": form}
        return render(request, "registration/signUp.html", context)

    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")

        context = {"form": form}
        return render(request, "registration/signUp.html", context)
