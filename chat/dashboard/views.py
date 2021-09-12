from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Room, Message
from .forms import CreateRoomForm

@login_required
def dashboardView(request):
    if request.method == 'POST':
        room = Room.objects.filter(name=request.POST.get('room_button'))[0]
        context = {'room': room, 'messages': []}
        return redirect('chat/{}'.format(room.id))
    context = {'rooms': Room.objects.all()}
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
def chatView(request, room_id=None):
    msgs = Message.objects.filter(room_id=room_id)
    if request.method == 'POST':
        room = Room.objects.get(id=room_id)
        user = User.objects.get(id=request.user.id)
        message = Message.objects.create(room_id=room, user_id=user, text=request.POST['message'])
        print(room,user,message)
        message.save()
    room = Room.objects.filter(id=room_id)[0]
    context = {'room': room, 'messages': msgs}
    return render(request, 'dashboard/chat/home.html', context)