from django import forms
from django.contrib.auth.models import User
from .models import Profile,Message
class UserUpdateForm(forms.ModelForm):

    email=forms.EmailField()

    class Meta:
        model=User 
        fields=['username','email',] 

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields = ['image']

class SendImageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['image']