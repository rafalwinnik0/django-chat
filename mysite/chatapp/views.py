from django.shortcuts import render
from .models import ChatRoom
def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {'chatrooms':chatrooms})

def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    return render(request, 'chatapp/room.html', {'chatroom':chatroom})