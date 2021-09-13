from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models.query import QuerySet
from rest_framework.decorators import api_view
from .models import Room, Message
from .forms import CreateRoomForm
from .serializers import MessageSerializer

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
    room = Room.objects.filter(id=room_id)[0]
    context = {'room': room}
    return render(request, 'dashboard/chat/home.html', context)

@login_required
@api_view(['POST'])
def sendMessage(request):
    if request.method == 'POST':
        room = Room.objects.get(id=request.POST['room_id'])
        user = User.objects.get(id=request.user.id)
        message = Message.objects.create(room=room, user=user, text=request.POST['message'])
        message.save()
    return JsonResponse({'status': True})

@login_required
@api_view(['GET'])
def getMessages(request):
    if request.method == 'GET':
        messages = Message.objects.filter(room_id=request.GET['room_id']).order_by('-created_at')
        if len(messages)==0:
            return JsonResponse({'messages': None})
        elif len(messages)>50:
            messages = messages[:50]

        serializable_messages = []
        for m in reversed(messages):
            serializable_messages.append(
                {
                    'text': m.text,
                    'user_name': m.user.username,
                    'user_id': m.user.id,
                    'room_name': m.room.name,
                    'room_id': m.room.id,
                    'datetime': m.created_at.strftime("%B %d, %Y %H:%M:%S"),
                }
            )
        return JsonResponse({'messages': MessageSerializer(serializable_messages, many=True).data})
    return JsonResponse({'messages': None})