from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models.query import QuerySet
from rest_framework.decorators import api_view
from asgiref.sync import sync_to_async
from .models import Room, Message
from .forms import CreateRoomForm
from .serializers import MessageSerializer
from .bot_client import BotClient

@login_required
def dashboard_view(request):
    if request.method == 'POST':
        rooms = Room.objects.filter(name=request.POST.get('room_button'))
        if len(rooms)>0:
            room = rooms[0]
            context = {'room': room, 'messages': []}
            return redirect('chat/{}'.format(room.id))
        else:
            context = {'rooms': rooms}
            return render(request, 'dashboard/rooms/home.html', context)
    context = {'rooms': Room.objects.all()}
    return render(request, 'dashboard/rooms/home.html', context)

@login_required
def create_room_view(request):
    form = CreateRoomForm()
    if request.method == 'POST':
        if request.POST.get('button')=='Back':
            return redirect('rooms')
        form = CreateRoomForm(request.POST)
        if form.is_valid() and form.data['name']!='':
            form.save()
            return redirect('rooms')
    context = {'form': form}
    return render(request, 'dashboard/rooms/create.html', context)

@login_required
def chat_view(request, room_id=None):
    room = Room.objects.filter(id=room_id)[0]
    context = {'room': room}
    return render(request, 'dashboard/chat/home.html', context)

@login_required
@api_view(['POST'])
def send_message(request):
    if request.method == 'POST':
        text = request.POST['message']
        if len(text)==0:
            return JsonResponse({'status': False})
        elif '/stock=' in text and text[0]=='/':
            stock_code = text[text.index('=')+1:]
            room = Room.objects.get(id=request.POST['room_id'])
            bot = BotClient(room, stock_code)
            bot.start()
            return JsonResponse({'status': False})
        else:
            room = Room.objects.get(id=request.POST['room_id'])
            user = User.objects.get(id=request.user.id)
            message = Message.objects.create(room=room, user=user, text=text)
            message.save()
            return JsonResponse({'status': True})
    return JsonResponse({'status': False})

@login_required
@api_view(['GET'])
def get_messages(request):
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
        return JsonResponse({'bot_id': User.objects.get(username='stocks-bot').id, 'messages': MessageSerializer(serializable_messages, many=True).data})
    return JsonResponse({'messages': None})