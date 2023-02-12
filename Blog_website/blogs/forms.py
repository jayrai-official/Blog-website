from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.forms import TextInput,EmailInput,PasswordInput

class signup_form(UserCreationForm):
    password1=forms.CharField(widget=PasswordInput(attrs={'class':'input-field','placeholder':'Enter password'}))
    password2=forms.CharField(widget=PasswordInput(attrs={'class':'input-field','placeholder':'Enter confirm password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={
            'username':TextInput(attrs={'class':'input-field','placeholder':'Enter Username'}),
            'first_name':TextInput(attrs={'class':'input-field','placeholder':'Enter First name'}),
            'last_name':TextInput(attrs={'class':'input-field','placeholder':'Enter Last name'}),
            'email':EmailInput(attrs={'class':'input-field','placeholder':'Enter email'}),
        }
    
class login_form(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={'class':'input-field','placeholder':'Enter Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'input-field','placeholder':'Enter Password'}))
