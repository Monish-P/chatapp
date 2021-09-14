from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

@login_required
def profile(request):
    if request.method=='POST':
        u_update=UserUpdateForm(request.POST,instance=request.user)
        if u_update.is_valid():
            u_update.save()
            messages.success(request,'Your details have been updated.')
            return redirect('profile')
    else:
        u_update=UserUpdateForm(instance=request.user)

    context={
        'u_update':u_update,
    }
    return render(request,'chat/profile.html',context)

def room(request, room):
    username = request.user.username
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.user.username

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

@login_required
def search_users(request):
    username = request.POST['search_user']

    if User.objects.filter(username=username).exists():
        usser = User.objects.get(username=username)
        return render(request, 'chat/profile_view.html',{'usser':usser})
    else:
        messages.error(request,'The user does not exist')
        return HttpResponse("User does not exist")

