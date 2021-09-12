from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboardView(request):
    if request.method == "POST":
        selected_room = request.POST.get('room_button')
        context = {"room": selected_room}
        return render(request, 'dashboard/chat/home.html', context)
    context = {"rooms": []}
    return render(request, 'dashboard/rooms/home.html', context)

@login_required
def chatView(request):
    return render(request, 'dashboard/chat/home.html')