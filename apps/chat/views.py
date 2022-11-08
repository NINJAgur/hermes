from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.chat.models import Room, Message

@login_required
def rooms(request):
    context = {'chat'}
    rooms = Room.objects.all()
    return render(request, 'chat/rooms.html', {'rooms': rooms, 'messages': [], 'segment': context})

@login_required
def rooms_id(request, slug):
    context = {'chat'}
    rooms = Room.objects.all()
    current = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=current)[0:25]
    return render(request, 'chat/rooms.html', {'room': current, 'rooms': rooms, 'messages': messages, 'segment': context})

@login_required
def room(request, slug):
    context = {'chat'}
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room.html', {'room': room, 'messages': messages, 'segment': context})