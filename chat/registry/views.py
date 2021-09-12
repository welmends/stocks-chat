from django.shortcuts import redirect, render
from django.contrib.auth import login
from .forms import UserSignUpForm

def signUpView(request):
    form = UserSignUpForm()
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/signUp.html', context)