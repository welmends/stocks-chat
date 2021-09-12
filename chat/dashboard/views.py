from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room
from .forms import CreateRoomForm

@login_required
def dashboardView(request):
    if request.method == "POST":
        selected_room = request.POST.get('room_button')
        context = {"room": selected_room}
        return render(request, 'dashboard/chat/home.html', context)
    context = {"rooms": Room.objects.all()}
    return render(request, 'dashboard/rooms/home.html', context)

@login_required
def createRoomView(request):
    form = CreateRoomForm()
    if request.method == 'POST':
        if request.POST.get('button')=='Back':
            return redirect('rooms')
        form = CreateRoomForm(request.POST)
        if form.is_valid and form.data['name']!='':
            form.save()
            return redirect('rooms')
    context = {'form': form}
    return render(request, 'dashboard/rooms/create.html', context)

@login_required
def chatView(request):
    return render(request, 'dashboard/chat/home.html')