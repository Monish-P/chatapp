from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

def starting(request):
    return render(request,'authentication/starting.html')

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created ')
            return redirect('login')
        else:
            messages.error(request,'Invalid data')
    else:
        form = UserRegisterForm()
    return render(request,'authentication/register.html',{'form':form})
