from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegistration(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    class Meta:
        model=User
        fields =('username','email','password1','password2')
        
class LoginFom(AuthenticationForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

