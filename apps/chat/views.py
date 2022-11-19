from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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

@login_required
def get_chat_room(request, slug):
    try:
        requestedRoom = Room.objects.get(slug=slug)

    except Room.DoesNotExist:
        try:
            names = slug.split('ROOM')
            print(names)
            altslug = names[1] + 'ROOM' + names[0]
            print(altslug)
            requestedRoom = Room.objects.get(slug=altslug)
            return redirect('/chat/', altslug)

        except Room.DoesNotExist:
            print("still failed")
            members = slug.split('ROOM')
            name = members[0] + '&' + members[1]
            requestedRoom = Room(name=name, slug=slug)
            requestedRoom.save()
    
    return redirect('/chat/', slug)


