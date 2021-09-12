from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboardView(request):
    return render(request, 'dashboard/home.html')
