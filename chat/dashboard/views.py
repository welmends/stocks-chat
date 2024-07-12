from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .bot_client import BotClient
from .models import Message, Room
from .serializers import MessageSerializer


@login_required
@api_view(["POST"])
def send_message(request):
    if request.method == "POST":
        text = request.POST["message"]
        if len(text) == 0:
            return JsonResponse({"status": False})
        elif text[0] == "/" and "/stock=" in text:
            stock_code = text[text.index("=") + 1 :]  # noqa
            room = Room.objects.get(id=request.POST["room_id"])
            bot = BotClient(room, stock_code)
            bot.start()
            return JsonResponse({"status": True})
        elif text[0] == "/" and "=" in text:
            wrong_cmd = text[1 : text.index("=")]  # noqa
            room = Room.objects.get(id=request.POST["room_id"])
            user = User.objects.get(username="stocks-bot")
            message = Message.objects.create(
                room=room,
                user=user,
                text='There is no such command "{}"'.format(wrong_cmd),
            )
            message.save()
            return JsonResponse({"status": True})
        else:
            room = Room.objects.get(id=request.POST["room_id"])
            user = User.objects.get(id=request.user.id)
            message = Message.objects.create(room=room, user=user, text=text)
            message.save()
            return JsonResponse({"status": True})
    return JsonResponse({"status": False})


@login_required
@api_view(["GET"])
def get_messages(request):
    if request.method == "GET":
        messages = Message.objects.filter(room_id=request.GET["room_id"]).order_by(
            "-created_at"
        )
        if len(messages) == 0:
            return JsonResponse({"messages": None})
        elif len(messages) > 50:
            messages = messages[:50]

        serializable_messages = []
        for m in reversed(messages):
            serializable_messages.append(
                {
                    "text": m.text,
                    "user_name": m.user.username,
                    "user_id": m.user.id,
                    "room_name": m.room.name,
                    "room_id": m.room.id,
                    "datetime": m.created_at.strftime("%B %d, %Y %H:%M:%S"),
                }
            )
        return JsonResponse(
            {
                "bot_id": User.objects.get(username="stocks-bot").id,
                "messages": MessageSerializer(serializable_messages, many=True).data,
            }
        )
    return JsonResponse({"messages": None})
