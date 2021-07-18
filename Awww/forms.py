from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registration(UserCreationForm):
    email = forms.EmailField(required=True)
      
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
     
class UploadForm(forms.ModelForm):
    class Meta:
        model= Projects
        fields = ('project', 'image', 'description','live_link', 'user')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'user', 'contact_info', 'more_info')
        
class AuthenticationForm(forms.ModelFormm):
    class Meta:
        model = User
        
 