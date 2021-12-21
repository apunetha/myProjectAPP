from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Room
from django.urls import path
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
    rooms = Room.objects.all()
    context ={'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'rooms':room}
    return render(request,'base/room.html',context)
