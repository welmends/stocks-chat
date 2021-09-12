from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm

def signUpView(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    else:
        form = UserSignUpForm()
    context = {'form': form}
    return render(request, 'registration/signUp.html', context)

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')