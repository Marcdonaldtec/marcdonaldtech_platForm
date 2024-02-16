from django.shortcuts import render,redirect
from .forms import UserRegistration,LoginFom
from django.contrib.auth import login, logout
from django.contrib import messages


def register_user(request):
    if request.method =='POST':
        form = UserRegistration(data=request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
        return redirect('MainApp:home')
    else:
        form = UserRegistration()
    return render(request, 'AuthenticationApp/register.html', {'form':form})
            
def login_user(request):
    if request.method =='POST':
        form = LoginFom(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('MainApp:home')
    else:
        form = LoginFom()
    
    return render(request, 'AuthenticationApp/login.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('MainApp:home')