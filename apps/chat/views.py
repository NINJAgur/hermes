from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.chat.models import Room, Message

@login_required
def rooms(request):
    context = {'chat'}
    rooms = Room.objects.all()
    return render(request, 'chat/rooms.html', {'rooms': rooms, 'segment': context})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room.html', {'room': room, 'messages': messages})