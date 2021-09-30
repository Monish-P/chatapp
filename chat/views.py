from django.shortcuts import render, redirect
from chat.models import Room, Message,Group,Notification
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,ProfileUpdateForm,SendImageForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DeleteView
from django.urls import reverse
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

@login_required
def profile(request):
    if request.method=='POST':
        u_update=UserUpdateForm(request.POST,instance=request.user)
        p_update=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.Profile)
        if u_update.is_valid() and p_update.is_valid():
            u_update.save()
            p_update.save()
            messages.success(request,'Your details have been updated.')
            return redirect('profile')
    else:
        u_update=UserUpdateForm(instance=request.user)
        p_update=ProfileUpdateForm(instance=request.user.Profile)
    
    context={
        'u_update':u_update,
        'p_update':p_update,
        'notifications':Notification.objects.all(),
        'group':Group.objects.all(),
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
def privatecheckview(request):
    room = request.POST['room_name']
    username = request.user.username
    room1 = room+username
    room2 = username+room
    if Room.objects.filter(name=room1).exists():
        return redirect('privatechat/'+room1+'/'+room+'/?username='+username)
    elif Room.objects.filter(name=room2).exists():
        return redirect('privatechat/'+room2+'/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room1)
        new_room.save()
        return redirect('privatechat/'+room1+'/'+room+'/?username='+username)

def privateroom(request, room, chattinguser):
    username = request.user.username
    room_details = Room.objects.get(name=room)
    other_user = User.objects.get(username=chattinguser)
    if Notification.objects.all().filter(user=chattinguser).exists():
        Notification.objects.get(user=chattinguser).delete()
    return render(request, 'chat/private_chat.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'chattinguser': chattinguser,
        'other_user':other_user
    })
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    med = request.POST['media']
    if med == '':
        new_message = Message.objects.create(value=message, user=username, room=room_id)
    else:
        new_message = Message.objects.create(value=message, user=username, room=room_id,image=med)
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

class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'
    
    def get_queryset(self):
        return Message.objects.filter(user = self.request.user.username, room = self.kwargs['roomid'])
class MessageDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Message
    def get_success_url(self):
        ri = self.kwargs['roomid']
        return reverse('deletemessages',kwargs = {'roomid':ri})
    context_object_name='message'
    def test_func(self):
        message=self.get_object()
        if self.request.user.username==message.user:
            return True
        return False

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):    
    user.Profile.is_online = True
    user.Profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):   
    user.Profile.is_online = False
    user.Profile.save()


def create_group(request):
    return render(request,'chat/group_name.html')

def group_name(request):
    gname = request.POST['group_name']
    g = Group.objects.create(name=gname,user=request.user.username)
    g.save()
    return render(request,'chat/add_users.html',{'gname':gname})
def add_users(request):
    usser = request.POST['add_user']
    gname = request.POST['gname']
    if User.objects.filter(username=usser).exists():
        g = Group.objects.create(name=gname,user=usser)
        g.save()
        messages.success(request,'User added successfully')
    else:
        messages.error(request,'The user does not exist')
    return render(request,'chat/add_users.html',{'gname':gname})
def group(request,group):
    username = request.user.username
    if Room.objects.filter(name=group).exists():
        room_details = Room.objects.get(name=group)
    else:
        r = Room.objects.create(name=group)
        r.save()
        room_details = Room.objects.get(name=group)
    if Notification.objects.all().filter(user=group).exists():
        Notification.objects.get(user=group).delete()
    return render(request, 'chat/group.html', {
        'username': username,
        'room': group,
        'room_details': room_details,
    })
def check_group(request):
    gname = request.POST['check_group']
    if Group.objects.filter(name=gname,user=request.user.username).exists():
        return redirect('group/'+gname)
    else:
        return HttpResponse('You are not a member of mentioned group or the group may not exist')

def exit_group(request,gname):
    Group.objects.get(name=gname,user=request.user.username).delete()
    return redirect('profile')

