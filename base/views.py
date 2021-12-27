from django.http.response import HttpResponse
from django.shortcuts import render,redirect

import base
from django.db.models import Q
from .models import Room,Topic
from django.urls import path
from .forms import RoomForm
# Create your views here.


# rooms =[
#     {
#         'id':1, 'name':'Lets Learn python'
#     },
#     {
#         'id':2, 'name':'Design with me'
#     },
#     {
#         'id':3, 'name':'frontend Developers'
#     },
    
# ]
def home(request):
    q =  request.GET.get('q') if request.GET.get('q')!=None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains =q) |
        Q(desciption__icontains =q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()

    context ={'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'rooms':room}
    return render(request,'base/room.html',context)

def createRoom(request):
    form = RoomForm
    if request.method =='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method =='POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method =='POST': 
        room.delete()
        return redirect('home')
    context={'obj':room}
    return render(request,'base/delete.html',context)
